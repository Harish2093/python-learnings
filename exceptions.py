# Errors and exceptions

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(value):
    if value > 100:
        raise ValueTooHighError("Value is too high")
    if value < 5:
        raise ValueTooLowError("Value is too low", value)

try:
    test_value(1000)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.value, e.message)