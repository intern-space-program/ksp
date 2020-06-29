import pytest

from src.commander import check_status
from src.util.commander.constants import *


def test_check_status_SMOOTH_FLYING():
    # arrange
    status = SMOOTH_FLYING

    # act
    ret = check_status(status)

    # assert
    assert ret == 0


def test_check_status_NOT_SMOOTH_FLYING():
    # arrange
    status = SMOOTH_FLYING + 1

    # act
    ret = check_status(status)

    # assert
    assert ret == 1
