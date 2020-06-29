import pytest


def example_function(a, b):
    return a + b


def test_example_function():
    # arrange
    a = 1
    b = 2

    # act
    ret = example_function(a, b)

    # assert
    assert ret == 3
