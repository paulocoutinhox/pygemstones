import os

import pytest

import pygemstones.io.file as f
import pygemstones.io.pack as p


# -----------------------------------------------------------------------------
def test_unpack_zip(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")

    pack_file_path = os.path.join(tmp_path, "file.zip")

    p.zip_dir(pack_file_path, pack_path)
    assert f.file_exists(pack_file_path)

    p.unpack(pack_file_path, unpack_path)
    assert f.dir_exists(unpack_path)

    files_unpacked = f.find_files(os.path.join(unpack_path, "pack"), "*.*")
    assert len(files_unpacked) == 2


# -----------------------------------------------------------------------------
def test_unpack_tgz(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")

    pack_file_path = os.path.join(tmp_path, "file.tgz")

    p.tar_dir(pack_file_path, pack_path)
    assert f.file_exists(pack_file_path)

    p.unpack(pack_file_path, unpack_path)
    assert f.dir_exists(unpack_path)

    files_unpacked = f.find_files(os.path.join(unpack_path, "pack"), "*.*")
    assert len(files_unpacked) == 2


# -----------------------------------------------------------------------------
def test_unpack_tar_gz(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")

    pack_file_path = os.path.join(tmp_path, "file.tar.gz")

    p.tar_dir(pack_file_path, pack_path)
    assert f.file_exists(pack_file_path)

    p.unpack(pack_file_path, unpack_path)
    assert f.dir_exists(unpack_path)

    files_unpacked = f.find_files(os.path.join(unpack_path, "pack"), "*.*")
    assert len(files_unpacked) == 2


# -----------------------------------------------------------------------------
def test_unpack_unknown_format(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")

    pack_file_path = os.path.join(tmp_path, "file.abc")

    p.tar_dir(pack_file_path, pack_path)
    assert f.file_exists(pack_file_path)

    with pytest.raises(Exception) as info:
        p.unpack(pack_file_path, unpack_path)

    assert info.value.args[0] == "File format not supported: .abc"


# -----------------------------------------------------------------------------
def test_zip_empty_dir_and_ignore_files(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")
    f.set_file_content(os.path.join(pack_path, "Thumbs.db"), "")
    f.set_file_content(os.path.join(pack_path, ".DS_Store"), "")
    f.create_dir(os.path.join(pack_path, "empty-dir"))

    pack_file_path = os.path.join(tmp_path, "file.zip")

    p.zip_dir(pack_file_path, pack_path)
    assert f.file_exists(pack_file_path)

    p.unpack(pack_file_path, unpack_path)
    assert f.dir_exists(unpack_path)

    files_unpacked = f.find_files(os.path.join(unpack_path, "pack"), "*.*")
    assert len(files_unpacked) == 2


# -----------------------------------------------------------------------------
def test_zip_symbolic_link(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")

    os.symlink(
        os.path.join(pack_path, "file1.py"), os.path.join(pack_path, "file-symbolic.py")
    )

    pack_file_path = os.path.join(tmp_path, "file.zip")

    p.zip_dir(pack_file_path, pack_path)
    assert f.file_exists(pack_file_path)

    p.unpack(pack_file_path, unpack_path)
    assert f.dir_exists(unpack_path)

    files_unpacked = f.find_files(os.path.join(unpack_path, "pack"), "*.*")
    assert len(files_unpacked) == 3


# -----------------------------------------------------------------------------
def test_tar_files(tmp_path):
    pack_path = os.path.join(tmp_path, "pack")
    unpack_path = os.path.join(tmp_path, "unpack")
    f.create_dir(pack_path)

    f.set_file_content(os.path.join(pack_path, "file1.py"), "")
    f.set_file_content(os.path.join(pack_path, "file2.py"), "")
    f.set_file_content(os.path.join(pack_path, "Thumbs.db"), "")
    f.set_file_content(os.path.join(pack_path, ".DS_Store"), "")

    pack_file_path = os.path.join(tmp_path, "file.tgz")

    p.tar_files(
        pack_file_path,
        [
            {"path": os.path.join(pack_path, "file1.py"), "arcname": "file1.py"},
            {"path": os.path.join(pack_path, "file2.py"), "arcname": "file2.py"},
            {"path": os.path.join(pack_path, "Thumbs.db"), "arcname": "Thumbs.db"},
            {"path": os.path.join(pack_path, ".DS_Store"), "arcname": ".DS_Store"},
        ],
    )

    assert f.file_exists(pack_file_path)

    p.unpack(pack_file_path, unpack_path)
    assert f.dir_exists(unpack_path)

    files_unpacked = f.find_files(os.path.join(unpack_path), "*.*")
    assert len(files_unpacked) == 2
