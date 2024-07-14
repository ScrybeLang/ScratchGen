class Script:
    def __init__(self, *args):
        self.blocks = list(args)

        for i in range(max(len(self.blocks) - 1, 0)):
            self.blocks[i]._addUnder(self.blocks[i + 1])

    def _addBlock(self, block):
        self.blocks[-1]._addUnder(block)
        self.blocks.append(block)

    def _serialize(self):
        dictionary = {}

        for block in self.blocks:
            dictionary.update(block._serialize())

        return dictionary
