import os
import tarfile
import zipfile

import pygemstones.system.settings as s


# -----------------------------------------------------------------------------
def unpack(src_path, dst_path):
    """
    Unpack a file from source path to target path, detecting the format by it extension.

    Will throw exception extension are unknown.

    Arguments:
        src_path : str

        dst_path : str

    Returns:
        None
    """

    _, file_extension = os.path.splitext(src_path)

    if file_extension in [".zip"]:
        with zipfile.ZipFile(src_path, "r") as archive:
            archive.extractall(dst_path)
            archive.close()
    elif file_extension in [".tgz", ".bz2", ".tar.gz", ".tbz2", ".tar.bz2", ".tar"]:
        with tarfile.open(src_path, "r:*") as archive:
            archive.extractall(dst_path)
            archive.close()
    else:
        raise Exception("File format not supported")


# -----------------------------------------------------------------------------
def zip_dir(output_file_path, source_dir, ignore_file_list=s.system_ignore_file_list):
    """
    Pack a directory using ZIP format.

    Some trash files are already ignored by ignore_file_list parameter.

    Arguments:
        output_file_path : str

        source_dir : str

        ignore_file_list : list[str]

    Returns:
        None
    """

    zip_out = zipfile.ZipFile(output_file_path, "w", compression=zipfile.ZIP_DEFLATED)
    root_len = len(os.path.dirname(source_dir))

    def archive_directory(parent_directory):
        contents = os.listdir(parent_directory)

        if not contents:
            archive_root = parent_directory[root_len:].replace("\\", "/").lstrip("/")
            zip_info = zipfile.ZipInfo(archive_root + "/")
            zip_out.writestr(zip_info, "")

        for item in contents:
            if item in ignore_file_list:
                continue

            full_path = os.path.join(parent_directory, item)

            if os.path.isdir(full_path) and not os.path.islink(full_path):
                archive_directory(full_path)
            else:
                archive_root = full_path[root_len:].replace("\\", "/").lstrip("/")

                if os.path.islink(full_path):
                    zip_info = zipfile.ZipInfo(archive_root)
                    zip_info.create_system = 3
                    zip_info.external_attr = 0xA1ED0000
                    zip_out.writestr(zip_info, os.readlink(full_path))
                else:
                    zip_out.write(full_path, archive_root, zipfile.ZIP_DEFLATED)

    archive_directory(source_dir)

    zip_out.close()


# -----------------------------------------------------------------------------
def tar_dir(output_file_path, source_dir, ignore_file_list=s.system_ignore_file_list):
    """
    Pack a directory using TAR format.

    Some trash files are already ignored by ignore_file_list parameter.

    Arguments:
        output_file_path : str

        source_dir : str

        ignore_file_list : list[str]

    Returns:
        None
    """

    tar_out = tarfile.open(output_file_path, "w:gz")
    tar_out.add(
        source_dir,
        arcname=os.path.basename(source_dir),
        filter=lambda x: None if x.name in ignore_file_list else x,
    )
    tar_out.close()


# -----------------------------------------------------------------------------
def tar_files(
    output_file_path, source_files, ignore_file_list=s.system_ignore_file_list
):
    """
    Pack a list of files using TAR format.

    Some trash files are already ignored by ignore_file_list parameter.

    Arguments:
        output_file_path : str

        source_files : list[dict]

        ignore_file_list : list[str]

    Returns:
        None
    """

    tar_out = tarfile.open(output_file_path, "w:gz")

    for source_file in source_files:
        tar_out.add(
            source_file["path"],
            arcname=source_file["arcname"],
            filter=lambda x: None if x.name in ignore_file_list else x,
        )

    tar_out.close()
