from ..opcodes import _get
from ..block import Block, Reporter
from ..constants import *

class SetVariable(Block):
    def __init__(self, variable, value):
        super().__init__(_get(self))
        self._addField("VARIABLE", variable)
        self._addInput(JSON_STRING, "VALUE", value)

class ChangeVariable(Block):
    def __init__(self, variable, change):
        super().__init__(_get(self))
        self._addField("VARIABLE", variable)
        self._addInput(JSON_STRING, "VALUE", change)

class HideVariable(Block):
    def __init__(self, variable):
        super().__init__(_get(self))
        self._addField("VARIABLE", variable)

class ShowVariable(Block):
    def __init__(self, variable):
        super().__init__(_get(self))
        self._addField("VARIABLE", variable)

class AddToList(Block):
    def __init__(self, item, list):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_STRING, "ITEM", item)

class DeleteOfList(Block):
    def __init__(self, index, list):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_INTEGER, "INDEX", index)

class ClearList(Block):
    def __init__(self, list):
        super().__init__(_get(self))
        self._addField("LIST", list)

class InsertIntoList(Block):
    def __init__(self, item, index, list):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_STRING, "ITEM", item)
        self._addInput(JSON_INTEGER, "INDEX", index)

class ReplaceInList(Block):
    def __init__(self, index, list, item):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_STRING, "ITEM", item)
        self._addInput(JSON_INTEGER, "INDEX", index)

class ItemOfList(Reporter):
    def __init__(self, index, list):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_INTEGER, "INDEX", index)

class ListIndexOf(Reporter):
    def __init__(self, item, list):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_STRING, "ITEM", item)

class ListLength(Reporter):
    def __init__(self, list):
        super().__init__(_get(self))
        self._addField("LIST", list)

class ListContains(Reporter):
    def __init__(self, list, item):
        super().__init__(_get(self))
        self._addField("LIST", list)
        self._addInput(JSON_STRING, "ITEM", item)

class HideList(Block):
    def __init__(self, list):
        super().__init__(_get(self))
        self._addField("LIST", list)

class ShowList(Block):
    def __init__(self, list):
        super().__init__(_get(self))
        self._addField("LIST", list)
