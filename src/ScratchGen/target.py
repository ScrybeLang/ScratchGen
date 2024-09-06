from .asset import Asset
from .datacontainer import Variable, List
from .script import Script
from .blocks import CustomBlock
import os

# 1 argument - File path (name determined from file name)
#   Example: parsePath("image.png") -> ("image", ".../.../image.png")
# 2 arguments - Name and file path
#   Example: parsePath("name", "sound.mp3") -> ("name", ".../.../sound.mp3")
# Returns asset name and absolute path
def parsePath(*args):
    if len(args) == 1:
        file_path = args[0]
        name = os.path.splitext(os.path.basename(file_path))[0]
    elif len(args) == 2:
        name, file_path = args

    file_path = os.path.abspath(file_path)

    return name, file_path

class Target:
    def __init__(self):
        self._is_stage = False
        self.name = ""

        self._variables = []
        self._lists = []
        self._broadcasts = []

        self.current_costume = 0
        self._asset_names = []
        self._assets = {
            "images": [],
            "sounds": []
        }

        self._scripts = []

        self.volume = 100
        self.layer_order = 0

    def _addAsset(self, type, *args):
        name, file_path = parsePath(*args)
        asset_name = os.path.basename(file_path)
        if asset_name in self._asset_names: return
        self._asset_names.append(asset_name)
        asset = Asset(name, file_path)
        self._assets[type].append(asset)

        return asset

    def _addCostume(self, *args) -> Asset:
        return self._addAsset("images", *args)

    def addSound(self, *args) -> Asset:
        return self._addAsset("sounds", *args)

    def createVariable(self, name: str, value = 0) -> Variable:
        variable = Variable(name, value)
        self._variables.append(variable)

        return variable

    def createList(self, name: str, entries: tuple = ()) -> List:
        _list = List(name, entries)
        self._lists.append(_list)

        return _list

    def createScript(self, *args) -> Script:
        script = Script(*args)
        self._scripts.append(script)

        return script

    def createCustomBlock(self,
            proccode: str,
            run_without_screen_refresh: bool = True):
        custom_block = CustomBlock(proccode, run_without_screen_refresh)
        script = Script(custom_block)
        self._scripts.append(script)

        custom_block.parent_script = script
        return custom_block

    def _serialize(self):
        dictionary = {
            "isStage": self._is_stage,
            "name": self.name,
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": self.current_costume,
            "costumes": [asset._serialize() for asset in self._assets["images"]],
            "sounds": [asset._serialize() for asset in self._assets["sounds"]],
            "layerOrder": self.layer_order,
            "volume": self.volume
        }

        for variable in self._variables:
            dictionary["variables"].update(variable._serialize())

        for _list in self._lists:
            dictionary["lists"].update(_list._serialize())

        for script in self._scripts:
            dictionary["blocks"].update(script._serialize())

        return dictionary
