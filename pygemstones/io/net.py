import os
import sys
import urllib.request as urllib2
from urllib.parse import urlparse

import pygemstones.system.settings as st
import pygemstones.type.string as s
import pygemstones.util.log as l


# -----------------------------------------------------------------------------
def download(url, dst_file):
    """
    Download a file by URL and save locally.

    Arguments:
        url : str

        dst_file : str

    Returns:
        None
    """

    req = urllib2.Request(url, headers=st.request_headers)
    req_handle = urllib2.urlopen(req)

    with open(dst_file, "wb") as f:
        meta = req_handle.info()
        meta_func = meta.getheaders if hasattr(meta, "getheaders") else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None

        if meta_length:
            file_size = int(meta_length[0])

        if file_size:
            l.i("Download file size: {0}".format(s.readable_file_size(file_size)))

        file_size_dl = 0
        block_sz = st.download_block_size
        block_count = 0

        while True:
            dbuffer = req_handle.read(block_sz)

            if not dbuffer:
                break

            dbuffer_len = len(dbuffer)
            file_size_dl += dbuffer_len
            block_count += 1

            f.write(dbuffer)

            download_hook(block_count, block_sz, file_size)
            sys.stdout.flush()

        l.d("")


# -----------------------------------------------------------------------------
def download_hook(count, block_size, total_size):
    """
    Download hook that receive downloaded data and show it progress.

    Arguments:
        count : int

        block_size : int

        total_size : int

    Returns:
        None
    """

    percent = int(count * block_size * 100 / total_size)

    msg = "\rDownloading: {0}% - {1}".format(
        percent, s.readable_file_size(count * block_size)
    ).ljust(80)

    sys.stdout.write(msg)


# -----------------------------------------------------------------------------
def get_url_basename(url):
    """
    Get the filename from a URL.

    Arguments:
        url : str

    Returns:
        str
    """

    url_data = urlparse(url)
    return os.path.basename(url_data.path)
