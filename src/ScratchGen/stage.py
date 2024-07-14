from .target import Target
from .broadcast import Broadcast

class Stage(Target):
    def __init__(self):
        super().__init__()

        self.addBackdrop = self._addCostume

        # Stage-specific changes
        self._is_stage = True
        self.name = "Stage"

        self._broadcasts = []

        # Stage-specific variables
        self.tempo = 60
        self.video_transparency = 50
        self.video_state = "on"
        self.tts_language = None

    def _createBroadcast(self, name: str) -> Broadcast:
        broadcast = Broadcast(name)
        self._broadcasts.append(broadcast)

        return broadcast

    def addBackdrop(self, *args):
        self._addCostume(*args)

    def _serialize(self):
        dictionary = super()._serialize()

        stage_specific = {
            "broadcasts": {},
            "tempo": self.tempo,
            "videoTransparency": self.video_transparency,
            "videoState": self.video_state,
            "textToSpeechLanguage": self.tts_language
        }

        for broadcast in self._broadcasts:
            stage_specific["broadcasts"].update(broadcast._serialize())

        dictionary.update(stage_specific)
        return dictionary
