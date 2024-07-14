from ..opcodes import _get
from ..block import Block, Reporter
from ..constants import *

class MoveSteps(Block):
    def __init__(self, steps):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "STEPS", steps)

class GoToPosition(Block):
    def __init__(self, x, y):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "X", x)
        self._addInput(JSON_NUMBER, "Y", y)

class GoTo(Block):
    def __init__(self, target):
        super().__init__(_get(self))
        self._addMenu("TO", target)

class TurnRight(Block):
    def __init__(self, degrees):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "DEGREES", degrees)

class TurnLeft(Block):
    def __init__(self, degrees):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "DEGREES", degrees)

class PointInDirection(Block):
    def __init__(self, direction):
        super().__init__(_get(self))
        self._addInput(JSON_ANGLE, "DIRECTION", direction)

class PointTowards(Block):
    def __init__(self, target):
        super().__init__(_get(self))
        self._addMenu("TOWARDS", target)

class GlideToPosition(Block):
    def __init__(self, seconds, x, y):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "SECS", seconds)
        self._addInput(JSON_NUMBER, "X", x)
        self._addInput(JSON_NUMBER, "Y", y)

class GlideTo(Block):
    def __init__(self, seconds, target):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "SECS", seconds)
        self._addMenu("TO", target)

class BounceOffEdge(Block):
    def __init__(self):
        super().__init__(_get(self))

class SetRotationStyle(Block):
    def __init__(self, style):
        super().__init__(_get(self), fields={
            "STYLE": [style, None]
        })

class ChangeX(Block):
    def __init__(self, change):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "DX", change)

class SetX(Block):
    def __init__(self, x):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "X", x)

class ChangeY(Block):
    def __init__(self, change):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "DY", change)

class SetY(Block):
    def __init__(self, y):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "Y", y)

class XPosition(Reporter):
    def __init__(self):
        super().__init__(_get(self))

class YPosition(Reporter):
    def __init__(self):
        super().__init__(_get(self))

class Direction(Reporter):
    def __init__(self):
        super().__init__(_get(self))
