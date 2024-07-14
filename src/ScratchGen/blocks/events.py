from ..opcodes import _get
from ..block import Block
from ..constants import *

class WhenFlagClicked(Block):
    def __init__(self):
        super().__init__(_get(self))

class WhenKeyPressed(Block):
    def __init__(self, key):
        super().__init__(_get(self))
        self._addField("KEY_OPTION", key)

class WhenThisSpriteClicked(Block):
    def __init__(self):
        super().__init__(_get(self))

class WhenBackdropSwitchesTo(Block):
    def __init__(self, backdrop):
        super().__init__(_get(self))
        self._addField("BACKDROP", backdrop)

class WhenGreaterThan(Block):
    def __init__(self, value, threshold):
        super().__init__(_get(self))
        self._addField("WHENGREATERTHANMENU", value)
        self._addInput(JSON_NUMBER, "VALUE", threshold)

class WhenBroadcastReceived(Block):
    def __init__(self, broadcast):
        super().__init__(_get(self))
        self._addField("BROADCAST_OPTION", broadcast)

class Broadcast(Block):
    def __init__(self, broadcast):
        super().__init__(_get(self))
        self._addInput(JSON_BROADCAST, "BROADCAST_INPUT", broadcast)

class BroadcastAndWait(Block):
    def __init__(self, broadcast):
        super().__init__(_get(self))
        self._addInput(JSON_BROADCAST, "BROADCAST_INPUT", broadcast)
