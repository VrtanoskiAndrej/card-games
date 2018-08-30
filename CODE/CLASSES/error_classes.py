"""
TWO WAYS TO CALL ERROR:
* 1
try:
    raise TypeClassError("MESSAGE")
except TypeClassError as e:
    print("TypeClassError Exception!", e.error)

OUTPUT:
CustomValueError Exception! MESSAGE

* 2
raise TypeClassError("MESSAGE")

OUTPUT:
Traceback (most recent call last):
    raise TypeClassError("WRONG CLASS TYPE")
__main__.TypeClassError: WRONG CLASS TYPE
"""


class TypeClassError(RuntimeError):
    def __init__(self, arg):
        self.error = arg
        self.args = {arg}


class InvalidInputError(TypeError):
    def __init__(self, arg):
        self.error = arg
        self.args = {arg}
