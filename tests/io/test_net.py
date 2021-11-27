import os
from unittest.mock import patch

import pygemstones.io.file as f
import pygemstones.io.net as n


# -----------------------------------------------------------------------------
class FakeResponseInfo(object):
    def get_all(self, key):
        if key == "Content-Length":
            return [99]


class FakeResponse:
    def __init__(self, resp_data, code=200, msg="OK"):
        self.resp_data = resp_data
        self.code = code
        self.msg = msg
        self.headers = {}
        self.info = lambda: FakeResponseInfo()
        self.resp_sent = False

    def read(self, block_size):
        if self.resp_sent:
            return None

        self.resp_sent = True

        return self.resp_data

    def getcode(self):
        return self.code


# -----------------------------------------------------------------------------
def test_download(tmp_path):
    with patch(
        "urllib.request.urlopen", return_value=FakeResponse("1234567".encode("utf-8"))
    ):
        file_url = "https://site.com/foo.zip"
        file_path = os.path.join(tmp_path, n.get_url_basename(file_url))

        n.download(file_url, file_path)

        assert f.file_exists(file_path)
        assert os.path.getsize(file_path) == 7
