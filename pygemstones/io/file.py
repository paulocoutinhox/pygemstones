import fnmatch
import os
import shutil
import stat


# -----------------------------------------------------------------------------
def remove_dir(path):
    """
    Remove directory with all errors and exceptions ignored.

    Arguments:
        path : str

    Returns:
        None
    """

    try:
        shutil.rmtree(path)
    except Exception:
        pass


# -----------------------------------------------------------------------------
def remove_file(path):
    """
    Remove file with all errors and exceptions ignored.

    Arguments:
        path : str

    Returns:
        None
    """

    if os.path.isfile(path):
        os.remove(path)


# -----------------------------------------------------------------------------
def remove_files(path, pattern):
    """
    Remove files with pattern with all errors and exceptions ignored.

    Arguments:
        path : str

        pattern : str

    Returns:
        None
    """

    for root, _, files in os.walk(path, topdown=False):
        for name in files:
            base_path = os.path.join(root, name)
            filename = os.path.basename(base_path)

            if fnmatch.fnmatch(filename, pattern):
                os.remove(base_path)


# -----------------------------------------------------------------------------
def remove_dirs(path, pattern):
    """
    Remove directories with pattern with all errors and exceptions ignored.

    Arguments:
        path : str

        pattern : str

    Returns:
        None
    """

    for root, dirs, _ in os.walk(path, topdown=False):
        for name in dirs:
            base_path = os.path.join(root, name)
            dirname = os.path.basename(base_path)

            if fnmatch.fnmatch(dirname, pattern):
                remove_dir(base_path)


# -----------------------------------------------------------------------------
def find_files(path, pattern, recursive=False):
    """
    Find all files which match the pattern.

    The search algorithm can find files recursively if enabled by the parameter.

    Arguments:
        path : str

        pattern : str

        recursive : bool

    Returns:
        list[str]
    """

    results = []

    if recursive:
        for root, _, files in os.walk(path, topdown=False):
            for name in files:
                base_path = os.path.join(root, name)
                filename = os.path.basename(base_path)

                if pattern == "*" or fnmatch.fnmatch(filename, pattern):
                    results.append(base_path)
    else:
        for item in os.listdir(path):
            base_path = os.path.join(path, item)

            if os.path.isfile(base_path):
                filename = os.path.basename(base_path)

                if pattern == "*" or fnmatch.fnmatch(filename, pattern):
                    results.append(base_path)

    return results


# -----------------------------------------------------------------------------
def find_dirs(path, pattern, recursive=False):
    """
    Find all directories which match the pattern.

    The search algorithm can find directories recursively if enabled by the parameter.

    Arguments:
        path : str

        pattern : str

        recursive : bool

    Returns:
        list[str]
    """

    results = []

    if recursive:
        for root, dirs, _ in os.walk(path, topdown=False):
            for name in dirs:
                base_path = os.path.join(root, name)
                dirname = os.path.basename(base_path)

                if pattern == "*" or fnmatch.fnmatch(dirname, pattern):
                    results.append(base_path)
    else:
        for item in os.listdir(path):
            base_path = os.path.join(path, item)

            if os.path.isdir(base_path):
                if pattern == "*" or fnmatch.fnmatch(item, pattern):
                    results.append(base_path)

    return results


# -----------------------------------------------------------------------------
def current_dir():
    """
    Get current directory with path normalized.

    Arguments:
        None

    Returns:
        str
    """

    return normalize_path(os.getcwd())


# -----------------------------------------------------------------------------
def normalize_path(path):
    """
    Get path normalized to unix pattern.

    Arguments:
        path : str

    Returns:
        str
    """

    if path:
        path = path.replace("\\", "/")
        return path
    else:
        return ""


# -----------------------------------------------------------------------------
def create_dir(path):
    """
    Create directory and all intermediate ones with all errors ignored.

    Arguments:
        path : str

    Returns:
        None
    """

    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


# -----------------------------------------------------------------------------
def set_file_content(file_path, content, method="w"):
    """
    Set file content creating directory and file, if not exists.

    Arguments:
        file_path : str

        contents : str

        method : str

    Returns:
        None
    """

    file_dir = os.path.dirname(file_path)

    remove_file(file_path)
    create_dir(file_dir)

    with open(file_path, method) as f:
        f.write(content)
        f.close()


# -----------------------------------------------------------------------------
def get_file_contents(file_path, method="r"):
    """
    Get file contents.

    Arguments:
        file_path : str

        method : str

    Returns:
        str
    """

    with open(file_path, method) as f:
        contents = f.read()
        f.close()

    return contents


# -----------------------------------------------------------------------------
def copy_file(from_path, to_path):
    """
    Copy file from one path to other, creating the target directory if not exists.

    Arguments:
        from_path : str

        to_path : str

    Returns:
        None
    """

    create_dir(os.path.dirname(to_path))
    shutil.copyfile(from_path, to_path)


# -----------------------------------------------------------------------------
def home_dir():
    """
    Get the user home directory.

    Arguments:
        None

    Returns:
        str
    """

    return os.path.expanduser("~")


# -----------------------------------------------------------------------------
def file_exists(path):
    """
    Check and return if a file exists or not.

    Arguments:
        path : str

    Returns:
        bool
    """

    if os.path.exists(path) and os.path.isfile(path):
        return True

    return False


# -----------------------------------------------------------------------------
def dir_exists(path):
    """
    Check and return if a directory exists or not.

    Arguments:
        path : str

    Returns:
        bool
    """

    if os.path.exists(path) and os.path.isdir(path):
        return True

    return False


# -----------------------------------------------------------------------------
def recreate_dir(path):
    """
    Remove directory and create a new one.

    Arguments:
        path : str

    Returns:
        None
    """

    remove_dir(path)
    create_dir(path)


# -----------------------------------------------------------------------------
def copy_dir(src, dst, symlinks=False, ignore=None, ignore_file=None):
    """
    Copy a directory from one path to other.

    Symbolic links can be copied too.

    A function can be used in ignore parameter to check if files from a directory will be ignored or not.

    A function can be used in ignore_file parameter to check if individual files will be ignored or not.

    Arguments:
        src : str

        dst : str

        symlinks : bool

        ignore: function

        ignore_file: function

    Returns:
        None
    """

    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)

    lst = os.listdir(src)

    if ignore:
        excl = ignore(src, lst)
        lst = [x for x in lst if x not in excl]

    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)

        if os.path.isdir(s):
            copy_dir(s, d, symlinks, ignore, ignore_file)
        else:
            if os.path.islink(s):
                if symlinks:
                    if ignore_file is None:
                        ignored_file = False
                    else:
                        ignored_file = ignore_file(s)

                    if not ignored_file:
                        if os.path.lexists(d):
                            os.remove(d)

                        os.symlink(os.readlink(s), d)

                        try:
                            st = os.lstat(s)
                            mode = stat.S_IMODE(st.st_mode)
                            os.lchmod(d, mode)
                        except:
                            # lchmod not available
                            pass
                else:
                    continue

            if ignore_file is None:
                ignored_file = False
            else:
                ignored_file = ignore_file(s)

            if not ignored_file:
                try:
                    shutil.copy2(s, d)
                except:
                    # ignore some errors
                    pass


# -----------------------------------------------------------------------------
def file_has_content(file, content, encoding="utf-8"):
    """
    Check and return if a file has a content inside.

    Arguments:
        file : str

        content : str

    Returns:
        bool
    """

    with open(file, encoding=encoding) as f:
        if content in f.read():
            return True

    return False


# -----------------------------------------------------------------------------
def prepend_to_file(file, content):
    """
    Add a content before current file content.

    Arguments:
        file : str

        content : str

    Returns:
        None
    """

    file_content = content + get_file_contents(file)
    file_dest = open(file, "w")
    file_dest.write(file_content)
    file_dest.close()


# -----------------------------------------------------------------------------
def append_to_file(file, content):
    """
    Add a content after current file content.

    Arguments:
        file : str

        content : str

    Returns:
        None
    """

    file_content = get_file_contents(file) + content
    file_dest = open(file, "w")
    file_dest.write(file_content)
    file_dest.close()


# -----------------------------------------------------------------------------
def replace_in_file(file, old_string, new_string, encoding="utf-8"):
    """
    Replace an old string by a new string inside a file.

    Arguments:
        file : str

        old_string : str

        new_string : str

    Returns:
        None
    """

    with open(file, encoding=encoding) as f:
        s = f.read()

    with open(file, "w", encoding=encoding) as f:
        s = s.replace(old_string, new_string)
        f.write(s)
        f.close()


# -----------------------------------------------------------------------------
def set_file_line_content(file, line, content, new_line=False, encoding="utf-8"):
    """
    Replace a line content inside a file by it number.

    A break line can be added at the end using new_line parameter.

    Arguments:
        file : str

        line : int

        content : str

        new_line: bool

    Returns:
        None
    """

    with open(file, encoding=encoding) as f:
        lines = f.readlines()
        lines[line - 1] = content + ("\n" if new_line else "")
        f.close()

        with open(file, "w", encoding=encoding) as f:
            f.writelines(lines)
            f.close()


# -----------------------------------------------------------------------------
def get_file_line_contents(file, line, encoding="utf-8"):
    """
    Get file line contents by it number.

    Arguments:
        file : str

        line : int

    Returns:
        str
    """

    with open(file, encoding=encoding) as f:
        lines = f.readlines()
        contents = lines[line - 1]
        f.close()

        return contents


# -----------------------------------------------------------------------------
def file_line_has_content(file, line, content, strip=False):
    """
    Check and return if a file line has a content by it number.

    The line can be stripped before check with strip parameter.

    Arguments:
        file : str

        line : int

        content : str

        strip : bool

    Returns:
        bool
    """

    line_contents = get_file_line_contents(file, line)

    if strip:
        return line_contents.strip() == content
    else:
        return line_contents == content


# -----------------------------------------------------------------------------
def prepend_to_file_line(file, line, content):
    """
    Add a content before a line content from file by it number.

    Arguments:
        file : str

        line : int

        content : str

    Returns:
        None
    """

    line_contents = get_file_line_contents(file, line)
    set_file_line_content(file, line, content + line_contents)


# -----------------------------------------------------------------------------
def prepend_to_file_line_range(file, line_start, line_end, content):
    """
    Add a content before a line content from a range of line numbers.

    Arguments:
        file : str

        line_start : int

        line_end : int

        content : str

    Returns:
        None
    """

    for x in range(line_start, line_end + 1):
        prepend_to_file_line(file, x, content)


# -----------------------------------------------------------------------------
def get_file_line_number_with_content(
    file, content, strip=False, match=False, encoding="utf-8"
):
    """
    Get a file line number that has a content.

    The lines can be stripped before check using strip parameter.

    The fnmatch function can be used to check using match parameter.

    Arguments:
        file : str

        content : str

        strip : bool

        match: bool

    Returns:
        int
    """

    with open(file, encoding=encoding) as f:
        lines = f.readlines()

        result = None

        for line_number, line in enumerate(lines):
            if strip:
                line = line.strip()

            if match:
                if fnmatch.fnmatch(line, content):
                    result = line_number + 1
                    break

            else:
                if line == content:
                    result = line_number + 1
                    break

        f.close()

        return result


# -----------------------------------------------------------------------------
def get_file_line_numbers_with_enclosing_tags(
    file, start_tag, end_tag, start_from=1, encoding="utf-8"
):
    """
    Get file line numbers that has start enclosing tag and end enclosing tags.

    Using a simple parser algorithm this function search for the enclosing tags and return the start and end line numbers where it start and finish.

    Arguments:
        file : str

        start_tag : str

        end_tag : str

        start_from : int

    Returns:
        list[int]
    """

    with open(file, encoding=encoding) as f:
        lines = f.readlines()

        result = None
        start_tag_count = 0
        end_tag_count = 0
        finish = False
        start_line_found = 0
        end_line_found = 0

        for line_number, line in enumerate(lines):
            if (line_number + 1) >= start_from:
                for line_char in line:
                    if line_char == start_tag:  # start tag
                        start_tag_count += 1

                        if start_line_found == 0:
                            # store first line with start tag
                            start_line_found = line_number + 1
                    elif line_char == end_tag:  # end tag
                        if start_line_found == 0:
                            # end tag cannot come before start tag, stop
                            finish = True

                        end_tag_count += 1

                    if start_line_found > 0:  # initialization
                        if start_tag_count == end_tag_count:  # count match
                            # the numbers of found tags was initialized and match
                            finish = True

                            end_line_found = line_number + 1
                            result = [start_line_found, end_line_found]

                            break

            if finish:
                break

        f.close()

        return result
