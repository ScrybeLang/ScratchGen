from .ids import generateID
from .constants import JSON_VARIABLE, JSON_LIST
from .block import _NumericalBinops

class DataContainer(_NumericalBinops):
    def __init__(self, name, value, type):
        self.id = generateID(type)

        self.name = name
        self.value = value
        self.json_type = JSON_VARIABLE if "v" in type else JSON_LIST

    def _asInputValue(self):
        return [3, [self.json_type] + self._asFieldValue()]

    def _asFieldValue(self):
        return [self.name, f"{self.id}-{self.name}"]

    def _serialize(self):
        return {
            f"{self.id}-{self.name}": [
                self.name, self.value
            ]
        }

class Variable(DataContainer):
    def __init__(self, name, value):
        super().__init__(name, value, "variable")
        self.type = "string"

class List(DataContainer):
    def __init__(self, name, entries):
        super().__init__(name, entries, "list")
        self.type = "list"
