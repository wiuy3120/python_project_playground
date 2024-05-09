import os
import sys

import pytest

from configs import conf

TEST_DATA_DIR = conf.DATA_DIR / "test_data"
# # each test runs on cwd to its temp dir
# @pytest.fixture(autouse=True)
# def go_to_tmpdir(request):
#     # Get the fixture dynamically by its name.
#     tmpdir = request.getfixturevalue("tmpdir")
#     # ensure local test created packages can be imported
#     sys.path.insert(0, str(tmpdir))
#     # Chdir only for the duration of the test.
#     with tmpdir.as_cwd():
#         yield


# each test runs on cwd to its temp dir
@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    # Get the fixture dynamically by its name.
    prev_cwd = os.getcwd()
    tmpdir = TEST_DATA_DIR
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # Chdir only for the duration of the test.
    os.chdir(tmpdir)
    yield
    os.chdir(prev_cwd)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.section("conftest durations")
    terminalreporter.write("conftest measure time")
    terminalreporter.currentfspath = 1
    terminalreporter.ensure_newline()
