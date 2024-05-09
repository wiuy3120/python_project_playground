from time import sleep

import pytest

from src import logger
from src.utils.string_utils import format_name


@pytest.fixture
def sleep_fixt():
    logger.warning("Sleeping ...")
    sleep(2)
    yield "Woke up"


@pytest.fixture
def sleep_fn_fixt():
    logger.warning("Sleeping ...")
    sleep(2)


def test_format_name_basic(sleep_fixt):
    logger.info(sleep_fixt)
    input_list = ["Nguyễn Văn A", "phan  Thị B", " a b c ", " đ  ê  á ẩ   "]
    output_list = ["Nguyễn Văn A", "Phan Thị B", "A B C", "Đ Ê Á Ẩ"]
    logger.error([format_name(name) for name in input_list])
    assert [format_name(name) for name in input_list] == output_list


def test_sleep(sleep_fixt):
    logger.info(sleep_fixt)


def test_sleep_fn(sleep_fn_fixt):
    sleep_fn_fixt
