from .stage import Stage
from .sprite import Sprite
import json
import zipfile

class Project:
    def __init__(self, agent="ScratchGen"):
        self.stage = Stage()

        self.addBackdrop = self.stage.addBackdrop
        self.createGlobalVariable = self.stage.createVariable
        self.createGlobalList = self.stage.createList
        self.createBroadcast = self.stage._createBroadcast

        self._targets = [self.stage]
        self._monitors = []
        self._extensions = []

        self.meta = {
            "semver": "3.0.0",
            "vm": "0.2.0",
            "agent": agent
        }

    def _serialize(self):
        dictionary = {
            "targets": [target._serialize() for target in self._targets],
            "monitors": [monitor._serialize() for monitor in self._monitors],
            "extensions": [extension.name for extension in self._extensions],
        }
        dictionary.update({"meta": self.meta})

        return dictionary

    def save(self, name: str):
        # Specify separators so output is minified (no whitespace)
        json_data = json.dumps(self._serialize(), separators=(',', ':'))

        written_assets = []
        with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED, compresslevel=5) as file:
            # Add all assets to ZIP file
            for target in self._targets:
                assets = target._assets["images"] + target._assets["sounds"]

                for asset in assets:
                    filename = asset.md5ext
                    if filename not in written_assets:
                        # Prevent duplicate assets
                        file.writestr(filename, asset.data)

                    written_assets.append(filename)

            file.writestr("project.json", json_data)

    def createSprite(self,
            name: str = "",
            visible: bool = True,
            x: int = 0,
            y: int = 0,
            size: int = 100,
            direction: int = 90,
            draggable: bool = False,
            rotation_style: str = "all around",
            layer_order: int = 1) -> Sprite:
        self._targets.append(Sprite(
            name, visible, x, y, size, direction,
            draggable, rotation_style, layer_order
        ))

        return self._targets[-1]
