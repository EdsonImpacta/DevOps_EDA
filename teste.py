import pytest
from principal import somar
from principal import subtrair


def test_soma():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(5, 2) == 3
