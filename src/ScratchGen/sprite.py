from .target import Target

class Sprite(Target):
    def __init__(self, name, visible, x, y, size, direction,
                 draggable, rotation_style, layer_order):
        super().__init__()

        self.addCostume = self._addCostume

        self.name = name

        # Sprite-specific variables
        self.visible = visible
        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.draggable = draggable
        self.rotation_style = rotation_style
        self.layer_order = max(layer_order, 1)

    def _asFieldValue(self):
        return [self.name, None]

    def _serialize(self):
        dictionary = super()._serialize()

        sprite_specific = {
            "visible": self.visible,
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "direction": self.direction,
            "draggable": self.draggable,
            "rotationStyle": self.rotation_style
        }

        dictionary.update(sprite_specific)
        return dictionary
