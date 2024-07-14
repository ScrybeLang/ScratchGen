from ..opcodes import _get
from ..block import Block, Reporter
from ..constants import *

class Say(Block):
    def __init__(self, message):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "MESSAGE", message)

class SayForSeconds(Block):
    def __init__(self, message, seconds):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "MESSAGE", message)
        self._addInput(JSON_NUMBER, "SECS", seconds)

class Think(Block):
    def __init__(self, message):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "MESSAGE", message)

class ThinkForSeconds(Block):
    def __init__(self, message, seconds):
        super().__init__(_get(self))
        self._addInput(JSON_STRING, "MESSAGE", message)
        self._addInput(JSON_NUMBER, "SECS", seconds)

class Show(Block):
    def __init__(self):
        super().__init__(_get(self))

class Hide(Block):
    def __init__(self):
        super().__init__(_get(self))

class SwitchCostume(Block):
    def __init__(self, costume):
        super().__init__(_get(self))
        self._addMenu("COSTUME", costume)

class SwitchBackdrop(Block):
    def __init__(self, backdrop):
        super().__init__(_get(self))
        self._addMenu("BACKDROP", backdrop)

class SwitchBackdropAndWait(Block):
    def __init__(self, backdrop):
        super().__init__(_get(self))
        self._addMenu("BACKDROP", backdrop)

class NextCostume(Block):
    def __init__(self):
        super().__init__(_get(self))

class NextBackdrop(Block):
    def __init__(self):
        super().__init__(_get(self))

class ChangeGraphicEffect(Block):
    def __init__(self, effect, change):
        super().__init__(_get(self))
        self._addField("EFFECT", effect)
        self._addInput(JSON_NUMBER, "CHANGE", change)

class SetGraphicEffect(Block):
    def __init__(self, effect, value):
        super().__init__(_get(self))
        self._addField("EFFECT", effect)
        self._addInput(JSON_NUMBER, "VALUE", value)

class ClearGraphicEffects(Block):
    def __init__(self):
        super().__init__(_get(self))

class SetSize(Block):
    def __init__(self, size):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "SIZE", size)

class ChangeSize(Block):
    def __init__(self, change):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "CHANGE", change)

class SetLayer(Block):
    def __init__(self, layer):
        super().__init__(_get(self))
        self._addField("FRONT_BACK", layer)

class ChangeLayer(Block):
    def __init__(self, direction, change):
        super().__init__(_get(self))
        self._addField("FORWARD_BACKWARD", direction)
        self._addInput(JSON_INTEGER, "NUM", change)

class Size(Reporter):
    def __init__(self):
        super().__init__(_get(self))

class Costume(Reporter):
    def __init__(self, option):
        super().__init__(_get(self))
        self._addField("NUMBER_NAME", option)

class Backdrop(Reporter):
    def __init__(self, option):
        super().__init__(_get(self))
        self._addField("NUMBER_NAME", option)
