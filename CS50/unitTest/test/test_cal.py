from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(10) == 100
    assert square(1) == 1