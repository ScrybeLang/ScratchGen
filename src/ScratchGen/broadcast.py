from .ids import generateID
from .constants import JSON_BROADCAST

class Broadcast:
    def __init__(self, name):
        self.id = generateID("broadcast")

        self.name = name
        self.json_type = JSON_BROADCAST

    def _asInputValue(self):
        return [1, [self.json_type, self.name, str(self.id)]]

    def _asFieldValue(self):
        return [self.name, str(self.id)]

    def _serialize(self):
        return {str(self.id): self.name}
