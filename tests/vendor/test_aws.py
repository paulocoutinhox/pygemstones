import os

import boto3
import pytest
from moto import mock_s3

import pygemstones.io.file as f
import pygemstones.vendor.aws as a


# -----------------------------------------------------------------------------
@pytest.fixture(scope="function")
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


# -----------------------------------------------------------------------------
@pytest.fixture(scope="function")
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")


# -----------------------------------------------------------------------------
@mock_s3
def test_key_exists(s3):
    bukcet_name = "my-bucket"

    s3.create_bucket(Bucket=bukcet_name)

    exists = a.s3_key_exists(s3, bukcet_name, "path1/path2")
    assert exists == False

    s3.put_object(Bucket=bukcet_name, Key="path1/path2")

    exists = a.s3_key_exists(s3, bukcet_name, "path1/path2")
    assert exists


# -----------------------------------------------------------------------------
@mock_s3
def test_create_path(s3):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    s3.create_bucket(Bucket=bucket_name)

    exists = a.s3_key_exists(s3, bucket_name, key_name)
    assert exists == False

    a.s3_create_path(s3, bucket_name, key_name)

    exists = a.s3_path_exists(s3, bucket_name, key_name)
    assert exists


# -----------------------------------------------------------------------------
@mock_s3
def test_delete_path(s3):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    s3.create_bucket(Bucket=bucket_name)
    a.s3_create_path(s3, bucket_name, key_name)

    exists = a.s3_path_exists(s3, bucket_name, key_name)
    assert exists

    a.s3_delete_path(s3, bucket_name, key_name)

    exists = a.s3_path_exists(s3, bucket_name, key_name)
    assert exists == False


# -----------------------------------------------------------------------------
@mock_s3
def test_delete_key(s3):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    s3.create_bucket(Bucket=bucket_name)
    s3.put_object(Bucket=bucket_name, Key=key_name, Body=b"test")

    exists = a.s3_key_exists(s3, bucket_name, key_name)
    assert exists

    a.s3_delete_key(s3, bucket_name, key_name)

    exists = a.s3_key_exists(s3, bucket_name, key_name)
    assert exists == False


# -----------------------------------------------------------------------------
@mock_s3
def test_upload(s3, tmp_path):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "test")

    s3.create_bucket(Bucket=bucket_name)

    a.s3_upload(file_path, bucket_name, key_name, force=False)

    exists = a.s3_key_exists(s3, bucket_name, key_name)
    assert exists


# -----------------------------------------------------------------------------
@mock_s3
def test_upload_invalid_file(s3, tmp_path):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file.txt")

    s3.create_bucket(Bucket=bucket_name)

    with pytest.raises(SystemExit) as info:
        a.s3_upload(file_path, bucket_name, key_name, force=False)

        assert info.value.args[0] == 10
        assert "not exists" in info.value.args[1]


# -----------------------------------------------------------------------------
@mock_s3
def test_upload_already_existing_key(s3, tmp_path):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "test")

    s3.create_bucket(Bucket=bucket_name)

    a.s3_upload(file_path, bucket_name, key_name, force=False)

    with pytest.raises(SystemExit) as info:
        a.s3_upload(file_path, bucket_name, key_name, force=False)

        assert info.value.args[0] == 10
        assert "already exists" in info.value.args[1]


# -----------------------------------------------------------------------------
@mock_s3
def test_upload_force_replace(s3, tmp_path):
    bucket_name = "my-bucket"
    key_name = "path1/path2"

    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "test")

    s3.create_bucket(Bucket=bucket_name)

    a.s3_upload(file_path, bucket_name, key_name, force=False)
    a.s3_upload(file_path, bucket_name, key_name, force=True)

    exists = a.s3_key_exists(s3, bucket_name, key_name)
    assert exists
