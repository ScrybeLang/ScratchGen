from ..opcodes import _get
from ..block import Block, Reporter
from ..constants import *

class Play(Block):
    def __init__(self, sound):
        super().__init__(_get(self))
        self._addMenu("SOUND_MENU", sound)

class PlayUntilDone(Block):
    def __init__(self, sound):
        super().__init__(_get(self))
        self._addMenu("SOUND_MENU", sound)

class StopSounds(Block):
    def __init__(self):
        super().__init__(_get(self))

class SetSoundEffect(Block):
    def __init__(self, effect, value):
        super().__init__(_get(self))
        self._addField("EFFECT", effect)
        self._addInput(JSON_NUMBER, "VALUE", value)

class ChangeSoundEffect(Block):
    def __init__(self, effect, change):
        super().__init__(_get(self))
        self._addField("EFFECT", effect)
        self._addInput(JSON_NUMBER, "VALUE", change)

class ClearSoundEffects(Block):
    def __init__(self):
        super().__init__(_get(self))

class SetVolume(Block):
    def __init__(self, volume):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "VOLUME", volume)

class ChangeVolume(Block):
    def __init__(self, change):
        super().__init__(_get(self))
        self._addInput(JSON_NUMBER, "VOLUME", change)

class Volume(Reporter):
    def __init__(self):
        super().__init__(_get(self), number=True)
