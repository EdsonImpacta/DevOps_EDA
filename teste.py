import pytest
from principal import somar


def test_soma():
    assert somar(2, 3) == 5
