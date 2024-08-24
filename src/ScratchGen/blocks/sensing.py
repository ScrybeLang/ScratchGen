from ..opcodes import _get
from ..block import Block, Reporter, Boolean
from ..constants import *

class TouchingObject(Boolean):
    def __init__(self, target):
        super().__init__(_get(self))
        self._addMenu("TOUCHINGOBJECTMENU", target)

class TouchingColor(Boolean):
    def __init__(self, hex_code):
        super().__init__(_get(self))
        self._addInput(JSON_COLOR, "COLOR", hex_code)

class ColorTouchingColor(Boolean):
    def __init__(self, hex_code_1, hex_code_2):
        super().__init__(_get(self))
        self._addInput(JSON_COLOR, "COLOR", hex_code_1)
        self._addInput(JSON_COLOR, "COLOR2", hex_code_2)

class DistanceTo(Reporter):
    def __init__(self, target):
        super().__init__(_get(self), number=True)
        self._addMenu("DISTANCETOMENU", target)

class Timer(Reporter):
    def __init__(self):
        super().__init__(_get(self), number=True)

class ResetTimer(Block):
    def __init__(self):
        super().__init__(_get(self))

class GetAttribute(Reporter):
    def __init__(self, attribute, target):
        super().__init__(_get(self))
        self._addField("PROPERTY", attribute)
        self._addMenu("OBJECT", target)

class MouseX(Reporter):
    def __init__(self):
        super().__init__(_get(self), number=True)

class MouseY(Reporter):
    def __init__(self):
        super().__init__(_get(self), number=True)

class SetDragMode(Block):
    def __init__(self, mode):
        super().__init__(_get(self))
        self._addField("DRAG_MODE", mode)

class MouseDown(Boolean):
    def __init__(self):
        super().__init__(_get(self))

class KeyPressed(Boolean):
    def __init__(self, key):
        super().__init__(_get(self))
        self._addMenu("KEY_OPTION", key)

class Current(Reporter):
    def __init__(self, option):
        super().__init__(_get(self), number=True)
        self._addField("CURRENTMENU", option)

class DaysSince2000(Reporter):
    def __init__(self):
        super().__init__(_get(self), number=True)

class Loudness(Reporter):
    def __init__(self):
        super().__init__(_get(self), number=True)

class Loud(Boolean):
    def __init__(self):
        super().__init__(_get(self))

class AskAndWait(Block):
    def __init__(self, question):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "QUESTION", question)

class Answer(Reporter):
    def __init__(self):
        super().__init__(_get(self))

class Username(Reporter):
    def __init__(self):
        super().__init__(_get(self))
