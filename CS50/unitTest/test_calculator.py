from calculator import square
import pytest

def main():
    test_square()

# def test_square():
#     if square(10) != 100:
#         raise Exception("Test failed")
#     if square(0) != 0:
#         raise Exception("Test failed")

# def test_square():
#     try:
#         assert square(10) == 100
#     except AssertionError:
#         print("Test failed")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("Test failed")
#     try:
#         assert square(1) == 1
#     except AssertionError:
#         print("Test failed")
#     try:
#         assert square(-1) == 1
#     except AssertionError:
#         print("Test failed")


def test_positive():
    assert square(2) == 4
    assert square(10) == 100
    assert square(1) == 1

def test_negative():
    assert square(-1) == 1
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0

def test_string():
    with pytest.raises(TypeError):
        square("cat")

def test_float():
    assert square(1.5) == 2.25


if __name__ == "__main__":
    main()