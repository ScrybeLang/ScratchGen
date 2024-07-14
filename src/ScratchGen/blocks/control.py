from ..opcodes import _get
from ..block import Block, CBlock
from ..script import Script
from ..constants import *

class Wait(Block):
    def __init__(self, duration):
        super().__init__(_get(self))
        self._addInput(JSON_POSITIVE, "DURATION", duration)

class Repeat(CBlock):
    def __init__(self, times, *blocks):
        super().__init__(_get(self))
        self._addInput(JSON_WHOLE, "TIMES", times)
        self._addSubstack("SUBSTACK", Script(*blocks))

class Forever(CBlock):
    def __init__(self, *blocks):
        super().__init__(_get(self))
        self._addSubstack("SUBSTACK", Script(*blocks))

class If(CBlock):
    def __init__(self, condition, *blocks):
        super().__init__(_get(self))
        self._addInput(JSON_SPECIAL, "CONDITION", condition)
        self._addSubstack("SUBSTACK", Script(*blocks))

    # Save a class, buy an opcode!
    # Easy to use, fun for the whole family!
    def Else(self, *blocks):
        self.opcode = "control_if_else"
        self._addSubstack("SUBSTACK2", Script(*blocks))

        return self # is this a monad

class WaitUntil(Block):
    def __init__(self, condition):
        super().__init__(_get(self))
        self._addInput(JSON_SPECIAL, "CONDITION", condition)

class RepeatUntil(CBlock):
    def __init__(self, condition, *blocks):
        super().__init__(_get(self))
        self._addInput(JSON_SPECIAL, "CONDITION", condition)
        self._addSubstack("SUBSTACK", Script(*blocks))

class Stop(Block):
    def __init__(self, mode):
        super().__init__(_get(self))
        self._addField("STOP_OPTION", mode)

        self.mutation = {"hasnext": mode == OTHER_SCRIPTS}

class WhenStartAsClone(Block):
    def __init__(self):
        super().__init__(_get(self))

class CreateCloneOf(Block):
    def __init__(self, target):
        super().__init__(_get(self))
        self._addMenu("CLONE_OPTION", target)

class DeleteThisClone(Block):
    def __init__(self):
        super().__init__(_get(self))
