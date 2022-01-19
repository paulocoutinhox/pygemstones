import os

import pygemstones.io.file as f


# -----------------------------------------------------------------------------
def test_create_dir(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(target_path)
    assert f.dir_exists(target_path)


# -----------------------------------------------------------------------------
def test_create_dir_that_already_exists(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(target_path)
    f.create_dir(target_path)

    assert f.dir_exists(target_path)


# -----------------------------------------------------------------------------
def test_remove_dir(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(target_path)
    assert f.dir_exists(target_path)

    f.remove_dir(target_path)
    assert f.dir_exists(target_path) == False


# -----------------------------------------------------------------------------
def test_remove_dir_that_not_exists(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    assert f.dir_exists(target_path) == False
    f.remove_dir(target_path)


# -----------------------------------------------------------------------------
def test_recreate_dir(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.recreate_dir(target_path)
    assert f.dir_exists(target_path)


# -----------------------------------------------------------------------------
def test_create_file(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    target_file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(target_file_path, "test")

    assert f.file_exists(target_file_path)


# -----------------------------------------------------------------------------
def test_remove_file(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    target_file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(target_file_path, "test")
    assert f.file_exists(target_file_path)

    f.remove_file(target_file_path)
    assert f.file_exists(target_file_path) == False


# -----------------------------------------------------------------------------
def test_remove_file_that_not_exists(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    target_file_path = os.path.join(target_path, "file1.txt")

    assert f.file_exists(target_file_path) == False
    f.remove_file(target_path)


# -----------------------------------------------------------------------------
def test_remove_files(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")

    files = f.find_files(target_path, "*.txt")
    assert len(files) == 2

    f.remove_files(target_path, "file1.txt")
    files = f.find_files(target_path, "*.txt")
    assert len(files) == 1

    f.remove_files(target_path, "*")
    files = f.find_files(target_path, "*")
    assert len(files) == 0

    f.set_file_content(os.path.join(target_path, "file3.pdf"), "test")

    f.remove_files(target_path, "*.pdf")
    files = f.find_files(target_path, "*")
    assert len(files) == 0


# -----------------------------------------------------------------------------
def test_remove_files_with_pattern_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")
    f.set_file_content(os.path.join(target_path, "other_file.txt"), "test")

    files = f.find_files(target_path, "*.txt")
    assert len(files) == 3

    f.remove_files(target_path, ["file*.txt", "file2.txt"])
    files = f.find_files(target_path, "*.txt")
    assert len(files) == 1


# -----------------------------------------------------------------------------
def test_remove_files_recursive(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "A", "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "B", "file2.txt"), "test")
    f.set_file_content(os.path.join(target_path, "C", "file3.txt"), "test")

    files = f.find_files(target_path, "file*.txt", recursive=True)
    assert len(files) == 3

    f.remove_files(target_path, "file*.txt", recursive=True)
    files = f.find_files(target_path, "*.txt", recursive=True)
    assert len(files) == 0


# -----------------------------------------------------------------------------
def test_remove_files_recursive_with_pattern_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "A", "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "B", "file2.txt"), "test")
    f.set_file_content(os.path.join(target_path, "C", "other_file.txt"), "test")

    files = f.find_files(target_path, "*.txt", recursive=True)
    assert len(files) == 3

    f.remove_files(target_path, ["file*.txt", "file2.txt"], recursive=True)
    files = f.find_files(target_path, "*.txt", recursive=True)
    assert len(files) == 1


# -----------------------------------------------------------------------------
def test_find_files(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")

    files = f.find_files(target_path, "*.txt")
    assert len(files) == 2


# -----------------------------------------------------------------------------
def test_find_files_as_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "file1_1.f1"), "test")
    f.set_file_content(os.path.join(target_path, "file1_2.f1"), "test")
    f.set_file_content(os.path.join(target_path, "file3_3.f1"), "test")
    f.set_file_content(os.path.join(target_path, "file2_1.f2"), "test")
    f.set_file_content(os.path.join(target_path, "file2_2.f2"), "test")
    f.set_file_content(os.path.join(target_path, "file3_1.f3"), "test")

    files = f.find_files(target_path, ["*.f2", "*.f3"])
    assert len(files) == 3


# -----------------------------------------------------------------------------
def test_find_files_recursive(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "A", "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "B", "file2.txt"), "test")

    files = f.find_files(target_path, "*.txt", recursive=True)
    assert len(files) == 2


# -----------------------------------------------------------------------------
def test_find_files_recursive_as_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.set_file_content(os.path.join(target_path, "A", "file1_1.f1"), "test")
    f.set_file_content(os.path.join(target_path, "A", "file1_2.f1"), "test")
    f.set_file_content(os.path.join(target_path, "A", "file1_3.f1"), "test")
    f.set_file_content(os.path.join(target_path, "B", "file2_1.f2"), "test")
    f.set_file_content(os.path.join(target_path, "B", "file2_2.f2"), "test")
    f.set_file_content(os.path.join(target_path, "C", "file3_1.f3"), "test")

    files = f.find_files(target_path, ["*.f2", "*.f3"], recursive=True)
    assert len(files) == 3


# -----------------------------------------------------------------------------
def test_find_dirs(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "new-dir-1"))
    f.create_dir(os.path.join(target_path, "new-dir-2"))
    f.create_dir(os.path.join(target_path, "new-dir-3"))

    dir_list = f.find_dirs(target_path, "*dir*")
    assert len(dir_list) == 3

    dir_list = f.find_dirs(target_path, "new*")
    assert len(dir_list) == 3


# -----------------------------------------------------------------------------
def test_find_dirs_as_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "abc1"))
    f.create_dir(os.path.join(target_path, "abc2"))
    f.create_dir(os.path.join(target_path, "xyz1"))
    f.create_dir(os.path.join(target_path, "xyz2"))
    f.create_dir(os.path.join(target_path, "jkl1"))
    f.create_dir(os.path.join(target_path, "wer1"))

    dir_list = f.find_dirs(target_path, ["*abc*", "jkl*"])
    assert len(dir_list) == 3

    dir_list = f.find_dirs(target_path, "xyz*")
    assert len(dir_list) == 2


# -----------------------------------------------------------------------------
def test_find_dirs_recursive(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "A", "new-dir-a"))
    f.create_dir(os.path.join(target_path, "B", "new-dir-b"))
    f.create_dir(os.path.join(target_path, "C", "new-dir-c"))

    dir_list = f.find_dirs(target_path, "new-dir*", recursive=True)
    assert len(dir_list) == 3


# -----------------------------------------------------------------------------
def test_find_dirs_recursive_as_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "A", "new-dir-a-1"))
    f.create_dir(os.path.join(target_path, "A", "new-dir-a-2"))
    f.create_dir(os.path.join(target_path, "A", "new-dir-a-3"))
    f.create_dir(os.path.join(target_path, "B", "new-dir-b-1"))
    f.create_dir(os.path.join(target_path, "B", "new-dir-b-2"))
    f.create_dir(os.path.join(target_path, "C", "new-dir-c-1"))

    dir_list = f.find_dirs(target_path, ["new-dir-b*", "new-dir-c*"], recursive=True)
    assert len(dir_list) == 3

    dir_list = f.find_dirs(target_path, ["new*", "*xyz*"], recursive=True)
    assert len(dir_list) == 6


# -----------------------------------------------------------------------------
def test_remove_dirs(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "new-dir-1"))
    f.create_dir(os.path.join(target_path, "new-dir-2"))
    f.create_dir(os.path.join(target_path, "new-dir-3"))

    dir_list = f.find_dirs(target_path, "*dir*")
    assert len(dir_list) == 3

    f.remove_dirs(target_path, "*dir*")

    dir_list = f.find_dirs(target_path, "*dir*")
    assert len(dir_list) == 0


# -----------------------------------------------------------------------------
def test_remove_dirs_with_pattern_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "new-dir-1"))
    f.create_dir(os.path.join(target_path, "new-dir-2"))
    f.create_dir(os.path.join(target_path, "new-dir-3"))

    dir_list = f.find_dirs(target_path, "*dir*")
    assert len(dir_list) == 3

    f.remove_dirs(target_path, ["*dir-1*", "*dir-2*"])

    dir_list = f.find_dirs(target_path, "*dir*")
    assert len(dir_list) == 1


# -----------------------------------------------------------------------------
def test_remove_dirs_recursive(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "A", "abc-dir-1"))
    f.create_dir(os.path.join(target_path, "B", "efg-dir-2"))
    f.create_dir(os.path.join(target_path, "C", "abc-dir-3"))

    dir_list = f.find_dirs(target_path, "*dir*", recursive=True)
    assert len(dir_list) == 3

    f.remove_dirs(target_path, "*abc-dir*", recursive=True)

    dir_list = f.find_dirs(target_path, "*dir*", recursive=True)
    assert len(dir_list) == 1


# -----------------------------------------------------------------------------
def test_remove_dirs_recursive_with_pattern_list(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")

    f.create_dir(os.path.join(target_path, "A", "abc-dir-1"))
    f.create_dir(os.path.join(target_path, "B", "efg-dir-2"))
    f.create_dir(os.path.join(target_path, "C", "abc-dir-3"))

    dir_list = f.find_dirs(target_path, "*dir*", recursive=True)
    assert len(dir_list) == 3

    f.remove_dirs(target_path, ["*abc-dir-*"], recursive=True)

    dir_list = f.find_dirs(target_path, "*dir*", recursive=True)
    assert len(dir_list) == 1


# -----------------------------------------------------------------------------
def test_current_dir():
    cur_dir = f.current_dir()
    assert len(cur_dir) > 0


# -----------------------------------------------------------------------------
def test_normalize_path():
    path = "/my-path\\my-other-path/my-path-2"
    norm_path = f.normalize_path(path)
    assert norm_path == "/my-path/my-other-path/my-path-2"

    path = None
    norm_path = f.normalize_path(path)
    assert norm_path == ""


# -----------------------------------------------------------------------------
def test_get_file_contents(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "my\ncontent")

    contents = f.get_file_contents(file_path)
    assert contents == "my\ncontent"


# -----------------------------------------------------------------------------
def test_file_has_content(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")
    contents = "my\ncontent"

    f.set_file_content(file_path, contents)

    assert f.file_has_content(file_path, contents)
    assert f.file_has_content(file_path, "xyz") == False


# -----------------------------------------------------------------------------
def test_copy_file(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")
    dst_path = os.path.join(target_path, "file2.txt")

    f.set_file_content(file_path, "test")

    f.copy_file(file_path, dst_path)
    assert f.file_exists(dst_path)


# -----------------------------------------------------------------------------
def test_copy_files(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")
    target_path = os.path.join(tmp_path, "target-dir")

    f.set_file_content(os.path.join(source_path, "file1_1.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file1_2.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file1_3.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file2_1.f2"), "test")
    f.set_file_content(os.path.join(source_path, "file2_2.f2"), "test")
    f.set_file_content(os.path.join(source_path, "file3_1.f3"), "test")
    os.symlink(
        os.path.join(source_path, "file2_1.f2"),
        os.path.join(source_path, "file2_symbolic.f2"),
    )

    f.copy_files(source_path, target_path, "*.f2")

    file_list = f.find_files(target_path, "*")

    assert len(file_list) == 3


# -----------------------------------------------------------------------------
def test_copy_files_with_pattern_list(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")
    target_path = os.path.join(tmp_path, "target-dir")

    f.set_file_content(os.path.join(source_path, "file1_1.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file1_2.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file1_3.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file2_1.f2"), "test")
    f.set_file_content(os.path.join(source_path, "file2_2.f2"), "test")
    f.set_file_content(os.path.join(source_path, "file3_1.f3"), "test")
    os.symlink(
        os.path.join(source_path, "file2_1.f2"),
        os.path.join(source_path, "file2_symbolic.f2"),
    )

    f.copy_files(source_path, target_path, ["*.f2", "*.f3"])

    file_list = f.find_files(target_path, "*")

    assert len(file_list) == 4


# -----------------------------------------------------------------------------
def test_copy_all(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")
    target_path = os.path.join(tmp_path, "target-dir")

    f.set_file_content(os.path.join(source_path, "file1_1.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file1_2.f1"), "test")
    f.set_file_content(os.path.join(source_path, "file1_3.f1"), "test")
    f.set_file_content(os.path.join(source_path, "B", "file2_1.f2"), "test")
    f.set_file_content(os.path.join(source_path, "B", "file2_2.f2"), "test")
    f.set_file_content(os.path.join(source_path, "C", "C" "file3_1.f3"), "test")
    os.symlink(
        os.path.join(source_path, "B", "file2_1.f2"),
        os.path.join(source_path, "B", "file2_symbolic.f2"),
    )

    f.copy_all(source_path, target_path)

    assert f.file_exists(os.path.join(source_path, "file1_1.f1"))
    assert f.file_exists(os.path.join(source_path, "file1_2.f1"))
    assert f.file_exists(os.path.join(source_path, "file1_3.f1"))
    assert f.file_exists(os.path.join(source_path, "B", "file2_1.f2"))
    assert f.file_exists(os.path.join(source_path, "B", "file2_2.f2"))
    assert f.file_exists(os.path.join(source_path, "C", "C" "file3_1.f3"))
    assert f.file_exists(os.path.join(source_path, "B", "file2_symbolic.f2"))

    file_list = f.find_files(target_path, "*", recursive=True)

    assert len(file_list) == 7


# -----------------------------------------------------------------------------
def test_home_dir():
    home_dir = f.home_dir()
    assert len(home_dir) > 0


# -----------------------------------------------------------------------------
def test_prepend_to_file(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "my-content")
    f.prepend_to_file(file_path, "pre-")

    contents = f.get_file_contents(file_path)
    assert contents == "pre-my-content"


# -----------------------------------------------------------------------------
def test_append_to_file(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "my-content")
    f.append_to_file(file_path, "-pos")

    contents = f.get_file_contents(file_path)
    assert contents == "my-content-pos"


# -----------------------------------------------------------------------------
def test_replace_in_file(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "my-content")
    f.replace_in_file(file_path, "my-content", "new-content")

    contents = f.get_file_contents(file_path)
    assert contents == "new-content"

    f.replace_in_file(file_path, "my-content", "abc")

    contents = f.get_file_contents(file_path)
    assert contents == "new-content"


# -----------------------------------------------------------------------------
def test_set_file_line_content(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3")
    f.set_file_line_content(file_path, 2, "line x\n")

    contents = f.get_file_line_contents(file_path, 2)
    assert contents.strip() == "line x"


# -----------------------------------------------------------------------------
def test_file_line_has_content(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3")

    assert f.file_line_has_content(file_path, 2, "line 2", strip=True)
    assert f.file_line_has_content(file_path, 2, "line 2") == False


# -----------------------------------------------------------------------------
def test_prepend_to_file_line(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3\nline 4\nline 5")

    f.prepend_to_file_line(file_path, 2, "//")
    f.prepend_to_file_line(file_path, 3, "//")
    f.prepend_to_file_line(file_path, 4, "//")

    assert f.file_line_has_content(file_path, 1, "line 1", strip=True)
    assert f.file_line_has_content(file_path, 2, "//line 2", strip=True)
    assert f.file_line_has_content(file_path, 3, "//line 3", strip=True)
    assert f.file_line_has_content(file_path, 4, "//line 4", strip=True)
    assert f.file_line_has_content(file_path, 5, "line 5", strip=True)


# -----------------------------------------------------------------------------
def test_prepend_to_file_line_range(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3\nline 4\nline 5")

    f.prepend_to_file_line_range(file_path, 2, 4, "//")

    assert f.file_line_has_content(file_path, 1, "line 1", strip=True)
    assert f.file_line_has_content(file_path, 2, "//line 2", strip=True)
    assert f.file_line_has_content(file_path, 3, "//line 3", strip=True)
    assert f.file_line_has_content(file_path, 4, "//line 4", strip=True)
    assert f.file_line_has_content(file_path, 5, "line 5", strip=True)


# -----------------------------------------------------------------------------
def test_copy_dir(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")
    os.symlink(
        os.path.join(target_path, "file1.txt"),
        os.path.join(target_path, "file1-symbolic.txt"),
    )

    f.copy_dir(target_path, dst_path, symlinks=False)

    file_list = f.find_files(dst_path, "*")

    assert len(file_list) == 2


# -----------------------------------------------------------------------------
def test_copy_dir_with_symbolic_links(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")
    os.symlink(
        os.path.join(target_path, "file1.txt"),
        os.path.join(target_path, "file1-symbolic.txt"),
    )

    f.copy_dir(target_path, dst_path, symlinks=True)

    file_list = f.find_files(dst_path, "*")

    assert len(file_list) == 3


# -----------------------------------------------------------------------------
def test_copy_dir_with_symbolic_links_as_directory(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")
    f.create_dir(os.path.join(target_path, "my-folder"))
    os.symlink(
        os.path.join(target_path, "my-folder"),
        os.path.join(target_path, "my-symbolic-folder"),
    )

    f.copy_dir(target_path, dst_path, symlinks=True)

    path_is_link = os.path.islink(os.path.join(dst_path, "my-symbolic-folder"))
    path_is_dir = os.path.isdir(os.path.join(dst_path, "my-symbolic-folder"))

    assert path_is_link
    assert path_is_dir

    path_is_link = os.path.islink(os.path.join(dst_path, "my-folder"))
    path_is_dir = os.path.isdir(os.path.join(dst_path, "my-folder"))

    assert path_is_dir
    assert path_is_link == False


# -----------------------------------------------------------------------------
def test_copy_dir_with_ignore_and_symbolic_links(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")
    os.symlink(
        os.path.join(target_path, "file1.txt"),
        os.path.join(target_path, "file1-symbolic.txt"),
    )

    def my_ignore_func(src, lst):
        new_list = []

        for item in lst:
            if "file1-symbolic.txt" in item:
                new_list.append(item)

        return new_list

    f.copy_dir(target_path, dst_path, symlinks=True, ignore=my_ignore_func)

    file_list = f.find_files(dst_path, "*")

    assert len(file_list) == 2


# -----------------------------------------------------------------------------
def test_copy_dir_with_ignore_file_and_symbolic_links(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "file2.txt"), "test")
    os.symlink(
        os.path.join(target_path, "file1.txt"),
        os.path.join(target_path, "file1-symbolic.txt"),
    )

    def my_ignore_func(file_path):
        print("ignore? ", file_path)
        if "symbolic" in file_path:
            return True

        return False

    f.copy_dir(target_path, dst_path, symlinks=True, ignore_file=my_ignore_func)

    file_list = f.find_files(dst_path, "*")

    assert len(file_list) == 2


# -----------------------------------------------------------------------------
def test_copy_dir_with_sub_dirs(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "A", "file1.txt"), "test")
    f.set_file_content(os.path.join(target_path, "B", "file2.txt"), "test")
    os.symlink(
        os.path.join(target_path, "A", "file1.txt"),
        os.path.join(target_path, "B", "file1-symbolic.txt"),
    )

    f.copy_dir(target_path, dst_path, symlinks=True)

    file_list = f.find_files(dst_path, "*", recursive=True)

    assert len(file_list) == 3


# -----------------------------------------------------------------------------
def test_copy_dir_with_already_exists_symbolic_link(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "A", "file1.txt"), "test")
    os.symlink(
        os.path.join(target_path, "A", "file1.txt"),
        os.path.join(target_path, "A", "file1-symbolic.txt"),
    )

    f.set_file_content(os.path.join(dst_path, "A", "file1-symbolic.txt"), "test")

    f.copy_dir(target_path, dst_path, symlinks=True)

    file_list = f.find_files(dst_path, "*", recursive=True)

    assert len(file_list) == 2


# -----------------------------------------------------------------------------
def test_copy_dir_with_symbolic_link_disabled(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    dst_path = os.path.join(tmp_path, "dst-dir")

    f.set_file_content(os.path.join(target_path, "file1.txt"), "test")
    os.symlink(
        os.path.join(target_path, "file1.txt"),
        os.path.join(target_path, "file1-symbolic.txt"),
    )

    f.copy_dir(target_path, dst_path, symlinks=False)

    file_list = f.find_files(dst_path, "*", recursive=True)

    assert len(file_list) == 1


# -----------------------------------------------------------------------------
def test_get_file_line_number_with_content(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3\nline 4\nline 5")

    line_number = f.get_file_line_number_with_content(file_path, "line 3\n")

    assert line_number == 3


# -----------------------------------------------------------------------------
def test_get_file_line_number_with_content_with_strip(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3\nline 4\nline 5")

    line_number = f.get_file_line_number_with_content(file_path, "line 4", strip=True)

    assert line_number == 4


# -----------------------------------------------------------------------------
def test_get_file_line_number_with_content_with_match(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3\nline 4\nline 5")

    line_number = f.get_file_line_number_with_content(file_path, "line 3*", match=True)

    assert line_number == 3


# -----------------------------------------------------------------------------
def test_get_file_line_number_with_content_with_strip_and_match(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(file_path, "line 1\nline 2\nline 3\nline 4\nline 5")

    line_number = f.get_file_line_number_with_content(
        file_path, "line 3", strip=True, match=True
    )

    assert line_number == 3


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_content(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(
        file_path, "line 1\nline 2\nline 3\nline 1\nline 4\nline 5\nline 1\n"
    )

    line_numbers = f.get_file_line_numbers_with_content(file_path, "line 1\n")

    assert len(line_numbers) == 3


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_content_with_strip(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(
        file_path, "line 1\nline 2\nline 3\nline 1\nline 4\nline 5\nline 1\n"
    )

    line_numbers = f.get_file_line_numbers_with_content(file_path, "line 1", strip=True)

    assert len(line_numbers) == 3


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_content_with_match(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(
        file_path, "line 1\nline 2\nline 3\nline 1\nline 4\nline 5\nline 1\n"
    )

    line_numbers = f.get_file_line_numbers_with_content(
        file_path, "line 1*", match=True
    )

    assert len(line_numbers) == 3


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_content_with_strip_and_match(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(
        file_path, "line 1\nline 2\nline 3\nline 1\nline 4\nline 5\nline 1\n"
    )

    line_numbers = f.get_file_line_numbers_with_content(
        file_path, "line 1", strip=True, match=True
    )

    assert len(line_numbers) == 3


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_content_not_found(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    f.set_file_content(
        file_path, "line 1\nline 2\nline 3\nline 1\nline 4\nline 5\nline 1\n"
    )

    line_numbers = f.get_file_line_numbers_with_content(file_path, "line 5")

    assert line_numbers == None


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_enclosing_tags_start(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    contents = """{-}
    my_first_function() {
        my_first_sub_function() {

        }

        a = []
        b = ()
        c = {}

        my_other_first_sub_function() {

        }
    }

    my_second_function() {
        my_other_second_sub_function() {

        }
    }
    {-}
    """

    f.set_file_content(file_path, contents)

    line_numbers = f.get_file_line_numbers_with_enclosing_tags(
        file_path, "{", "}", start_from=1
    )

    assert line_numbers[0] == 1
    assert line_numbers[1] == 1


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_enclosing_tags_first_function(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    contents = """{-}
    my_first_function() {
        my_first_sub_function() {

        }

        a = []
        b = ()
        c = {}

        my_other_first_sub_function() {

        }
    }

    my_second_function() {
        my_other_second_sub_function() {

        }
    }
    {-}
    """

    f.set_file_content(file_path, contents)

    line_numbers = f.get_file_line_numbers_with_enclosing_tags(
        file_path, "{", "}", start_from=2
    )

    assert line_numbers[0] == 2
    assert line_numbers[1] == 14


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_enclosing_tags_second_function(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    contents = """{-}
    my_first_function() {
        my_first_sub_function() {

        }

        a = []
        b = ()
        c = {}

        my_other_first_sub_function() {

        }
    }

    my_second_function() {
        my_other_second_sub_function() {

        }
    }
    {-}
    """

    f.set_file_content(file_path, contents)

    line_numbers = f.get_file_line_numbers_with_enclosing_tags(
        file_path, "{", "}", start_from=16
    )

    assert line_numbers[0] == 16
    assert line_numbers[1] == 20


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_enclosing_tags_end(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    contents = """{-}
    my_first_function() {
        my_first_sub_function() {

        }

        a = []
        b = ()
        c = {}

        my_other_first_sub_function() {

        }
    }

    my_second_function() {
        my_other_second_sub_function() {

        }
    }
    {-}
    """

    f.set_file_content(file_path, contents)

    line_numbers = f.get_file_line_numbers_with_enclosing_tags(
        file_path, "{", "}", start_from=21
    )

    assert line_numbers[0] == 21
    assert line_numbers[1] == 21


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_enclosing_tags_with_error(tmp_path):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    contents = """{-}
    my_first_function() {
        my_first_sub_function() {

        }

        a = []
        b = ()
        c = {}

        my_other_first_sub_function() {

        }
    }

    my_second_function() {
        my_other_second_sub_function() {

        }
    }
    {-}
    """

    f.set_file_content(file_path, contents)

    line_numbers = f.get_file_line_numbers_with_enclosing_tags(
        file_path, "{", "}", start_from=5
    )

    assert line_numbers == None


# -----------------------------------------------------------------------------
def test_get_file_line_numbers_with_enclosing_tags_with_more_end_than_start_tags(
    tmp_path,
):
    target_path = os.path.join(tmp_path, "new-dir")
    file_path = os.path.join(target_path, "file1.txt")

    contents = """{
        my_first_function() {
            }
            }
            }
        }
    }

    my_second_function() {
        my_other_second_sub_function() {

        }
    }
    """

    f.set_file_content(file_path, contents)

    line_numbers = f.get_file_line_numbers_with_enclosing_tags(file_path, "{", "}")

    assert line_numbers[0] == 1
    assert line_numbers[1] == 4


# -----------------------------------------------------------------------------
def test_create_symbolic_link(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")

    f.set_file_content(os.path.join(source_path, "file.txt"), "test")
    f.symlink(
        os.path.join(source_path, "file.txt"),
        os.path.join(source_path, "file_symbolic.txt"),
    )

    is_link = os.path.islink(os.path.join(source_path, "file_symbolic.txt"))

    assert is_link


# -----------------------------------------------------------------------------
def test_create_symbolic_link_with_error(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")

    f.set_file_content(os.path.join(source_path, "file.txt"), "test")
    f.set_file_content(os.path.join(source_path, "file_symbolic.txt"), "test")

    f.symlink(
        os.path.join(source_path, "file.txt"),
        os.path.join(source_path, "file_symbolic.txt"),
    )

    is_link = os.path.islink(os.path.join(source_path, "file_symbolic.txt"))

    assert is_link == False


# -----------------------------------------------------------------------------
def test_recreate_symbolic_link(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")

    f.set_file_content(os.path.join(source_path, "file.txt"), "test")
    f.symlink(
        os.path.join(source_path, "file.txt"),
        os.path.join(source_path, "file_symbolic.txt"),
    )
    f.symlink(
        os.path.join(source_path, "file.txt"),
        os.path.join(source_path, "file_symbolic.txt"),
        recreate=True,
    )

    is_link = os.path.islink(os.path.join(source_path, "file_symbolic.txt"))

    assert is_link


# -----------------------------------------------------------------------------
def test_remove_symbolic_link(tmp_path):
    source_path = os.path.join(tmp_path, "source-dir")

    f.set_file_content(os.path.join(source_path, "file.txt"), "test")
    f.symlink(
        os.path.join(source_path, "file.txt"),
        os.path.join(source_path, "file_symbolic.txt"),
    )

    is_link = os.path.islink(os.path.join(source_path, "file_symbolic.txt"))
    assert is_link

    f.unlink(os.path.join(source_path, "file_symbolic.txt"))

    is_link = os.path.islink(os.path.join(source_path, "file_symbolic.txt"))
    assert is_link == False
