import os
import sys

# add "pygemstones" to sys.path to import with "from pygemstones.sub_package import xyz"
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pygemstones"))
)
