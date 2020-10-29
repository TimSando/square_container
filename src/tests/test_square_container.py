import pytest
from src.square_container.square_container import demo, demo2


@pytest.mark.parametrize("image,expected", [("X", "Hello World")])
def test_demo(image, expected):
    assert demo(image) == expected


@pytest.mark.parametrize("expected,string", [("Goodbye World", "testing")])
def test_demo2(expected,string):
    assert demo2(string) == expected
