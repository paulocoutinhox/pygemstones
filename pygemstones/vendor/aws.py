import os
import sys
import threading

import boto3
from botocore.exceptions import ClientError

from pygemstones.util import log as l


# -----------------------------------------------------------------------------
def s3_upload(
    file_path,
    aws_bucket_name,
    aws_bucket_key,
    force=False,
    aws_key_id=None,
    aws_secret_key=None,
):
    """
    Upload a file to AWS S3 bucket.

    Arguments:
        file_path : str

        aws_bucket_name : str

        aws_bucket_key: str

        force: bool

        aws_key_id : str

        aws_secret_key : str

    Returns:
        None
    """

    # prepare to upload
    if not os.path.isfile(file_path):
        l.e("File not exists: {0}".format(file_path))

    # prepare aws sdk
    l.i("Initializing AWS bucket and SDK...")

    s3_client = boto3.client(
        service_name="s3",
        aws_secret_access_key=aws_secret_key,
        aws_access_key_id=aws_key_id,
    )

    # checking for existing version
    l.i("Checking if key exists...")

    key_exists = s3_key_exists(s3_client, aws_bucket_name, aws_bucket_key)

    if key_exists:
        if force:
            l.i('The key "{0}" already exists, removing...'.format(aws_bucket_key))

            s3_delete_path(
                s3_client,
                aws_bucket_name,
                aws_bucket_key,
            )
        else:
            l.e('The key "{0}" already exists'.format(aws_bucket_key))

    # upload
    l.i('Uploading file "{0}" to S3 bucket "{1}"...'.format(file_path, aws_bucket_name))

    s3_client.upload_file(
        file_path,
        aws_bucket_name,
        aws_bucket_key,
        ExtraArgs={"ACL": "public-read"},
        Callback=ProgressPercentage(file_path),
    )

    l.ok()


# -----------------------------------------------------------------------------
def s3_key_exists(s3, bucket, key):
    """
    Check and return if AWS S3 key existing in a bucket.

    Arguments:
        s3 : boto3.session.Session.client

        bucket : str

        key: str

    Returns:
        bool
    """

    from botocore.exceptions import ClientError

    try:
        s3.head_object(Bucket=bucket, Key=key)
    except ClientError as e:
        error_code = int(e.response["Error"]["Code"])

        if error_code >= 400 and error_code <= 499:
            return False

    return True


# -----------------------------------------------------------------------------
def s3_create_path(s3, bucket, key):
    """
    Create a path in AWS S3 bucket.

    Arguments:
        s3 : boto3.session.Session.client

        bucket : str

        key: str

    Returns:
        bool
    """

    try:
        s3.put_object(Bucket=bucket, Key=(key + "/"))
    except Exception as e:
        l.e('Failed to create path "{0}" on AWS S3: {1}'.format(key, e))

    return True


# -----------------------------------------------------------------------------
def s3_delete_key(s3, bucket, key):
    """
    Delete a key from AWS S3 bucket.

    Arguments:
        s3 : boto3.session.Session.client

        bucket : str

        key: str

    Returns:
        bool
    """

    try:
        s3.delete_objects(Bucket=bucket, Delete={"Objects": [{"Key": key}]})
    except Exception as e:
        l.e('Failed to delete key "{0}" from AWS S3: {1}'.format(key, e))

    return True


# -----------------------------------------------------------------------------
def s3_delete_path(s3, bucket, key):
    """
    Delete a path from AWS S3 bucket.

    Arguments:
        s3 : boto3.session.Session.client

        bucket : str

        key: str

    Returns:
        bool
    """

    try:
        s3.delete_objects(Bucket=bucket, Delete={"Objects": [{"Key": (key + "/")}]})
    except Exception as e:
        l.e('Failed to delete path "{0}" from AWS S3: {1}'.format(key, e))

    return True


# -----------------------------------------------------------------------------
def s3_path_exists(s3, bucket, key):
    """
    Check and return if AWS S3 key path exists in a bucket or not.

    Arguments:
        s3 : boto3.session.Session.client

        bucket : str

        key: str

    Returns:
        bool
    """

    try:
        s3.head_object(Bucket=bucket, Key=key + "/")
    except ClientError as e:
        error_code = int(e.response["Error"]["Code"])

        if error_code >= 400 and error_code <= 499:
            return False

    return True


# -----------------------------------------------------------------------------
class ProgressPercentage(object):
    """
    Class that show a percentage of progress of uploaded data.
    """

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %d  (%.2f%%)\n"
                % (
                    os.path.basename(self._filename),
                    self._seen_so_far,
                    self._size,
                    percentage,
                )
            )
            sys.stdout.flush()
