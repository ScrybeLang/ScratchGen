from ..opcodes import _get
from ..block import Reporter, Boolean
from ..constants import *

class Add(Reporter):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "NUM1", a)
        self._addInput(JSON_NUMBER, "NUM2", b)

class Subtract(Reporter):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "NUM1", a)
        self._addInput(JSON_NUMBER, "NUM2", b)

class Multiply(Reporter):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "NUM1", a)
        self._addInput(JSON_NUMBER, "NUM2", b)

class Divide(Reporter):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "NUM1", a)
        self._addInput(JSON_NUMBER, "NUM2", b)

class LessThan(Boolean):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "OPERAND1", a)
        self._addInput(JSON_NUMBER, "OPERAND2", b)

class Equals(Boolean):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "OPERAND1", a)
        self._addInput(JSON_NUMBER, "OPERAND2", b)

class GreaterThan(Boolean):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "OPERAND1", a)
        self._addInput(JSON_NUMBER, "OPERAND2", b)

class And(Boolean):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_SPECIAL, "OPERAND1", a)
        self._addInput(JSON_SPECIAL, "OPERAND2", b)

class Or(Boolean):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_SPECIAL, "OPERAND1", a)
        self._addInput(JSON_SPECIAL, "OPERAND2", b)

class Not(Boolean):
    def __init__(self, condition):
        super().__init__(_get(self))
        self._addInput(JSON_SPECIAL, "OPERAND", condition)

class PickRandom(Reporter):
    def __init__(self, start, end):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "FROM", start)
        self._addInput(JSON_NUMBER, "TO", end)

class Join(Reporter):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "STRING1", a)
        self._addInput(JSON_STRING, "STRING2", b)

class LetterOf(Reporter):
    def __init__(self, position, string):
        super().__init__(_get(self))
        self._addInput(JSON_WHOLE, "LETTER", position)
        self._addInput(JSON_STRING, "STRING", string)

class LengthOf(Reporter):
    def __init__(self, string):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "STRING", string)

class Contains(Boolean):
    def __init__(self, string, substring):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "STRING1", string)
        self._addInput(JSON_STRING, "STRING2", substring)

class Modulo(Reporter):
    def __init__(self, a, b):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "NUM1", a)
        self._addInput(JSON_NUMBER, "NUM2", b)

class Round(Reporter):
    def __init__(self, value):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "NUM", value)

class Operation(Reporter):
    def __init__(self, operation, value):
        super().__init__(_get(self))
        self._addField("OPERATOR", operation)
        self._addInput(JSON_NUMBER, "NUM", value)
