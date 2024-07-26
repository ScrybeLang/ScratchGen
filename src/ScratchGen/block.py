from .ids import generateID
from .opcodes import menu_opcodes

class Block:
    def __init__(self, opcode, generateID=True):
        if generateID: # for custom block parameters
            self._refreshID()

        self.opcode = opcode

        self.contained_blocks = []

        self.inputs = {}
        self.fields = {}
        self.mutation = {}

        self.shadow = False
        self.parent = None
        self.next = None

    def _refreshID(self):
        self.id = generateID("block")

    def _addUnder(self, other_block):
        other_block.parent = self.id
        self.next = other_block.id

    def _addInput(self, type, key, input):
        if isinstance(input, Reporter):
            if not hasattr(input, "id"):
                # "Regenerate" custom block parameters
                input = input._copy()

            self.contained_blocks.append(input)
            input.parent = self.id
            input.shadow = False

            if type == 14: # Boolean
                value = [2, str(input.id)]
            else:
                value = [3, str(input.id), [type, ""]]
        else:
            if isinstance(input, (str, int, float)):
                value = [1, [type, str(input)]]
            else:
                value = input._asInputValue()

        self.inputs[key] = value

    def _addField(self, key, value):
        if isinstance(value, str):
            value = [value, None]
        else:
            value = value._asFieldValue()

        self.fields.update({key: value})

    def _addMenu(self, key, input):
        if isinstance(input, Reporter):
            self.contained_blocks.append(input)
            input.parent = self.parent # not sure why this has to be here

            value = [3, str(input.id)]
        else:
            if not isinstance(input, str):
                input = input.name

            menu = Block(menu_opcodes[self.opcode])
            menu._addField(key, input)
            menu.shadow = True
            self.contained_blocks.append(menu)

            value = [1, str(menu.id)]

        self.inputs[key] = value

    def _serialize(self):
        dictionary = {
            "opcode": self.opcode,
            "next": str(self.next) if self.next else None,
            "parent": str(self.parent) if self.parent else None,
            "inputs": self.inputs,
            "fields": self.fields,
            "shadow": self.shadow,
            "topLevel": not bool(self.parent)
        }

        if self.mutation:
            self.mutation.update({
                "tagName": "mutation",
                "children": []
            })
            dictionary["mutation"] = self.mutation

        dictionary = {self.id: dictionary}

        for sub_block in self.contained_blocks:
            dictionary.update(sub_block._serialize())

        return dictionary

# Name distinction
Reporter = Block
Boolean = Reporter

# Class for blocks that can hold other ones
# Crazy!
class CBlock(Block):
    def __init__(self, opcode):
        super().__init__(opcode)

        self.substacks = []

    def _addSubstack(self, key, script):
        script.blocks[0].parent = self.id
        self.substacks.append(script)
        self._addInput(14, key, script.blocks[0])

    def _serialize(self):
        dictionary = super()._serialize()

        for substack in self.substacks:
            for block in substack.blocks:
                dictionary.update(block._serialize())

        return dictionary
