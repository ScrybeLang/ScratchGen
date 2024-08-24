from ..opcodes import _get
from ..block import Block, Reporter
from ..constants import *
from ..ids import generateID
from json import dumps

def JSONify(array):
    array = [str(item) for item in array]
    return dumps(array)

class CustomBlock(Block):
    def __init__(self, proccode, run_without_screen_refresh):
        super().__init__(_get(self))
        self.proccode = proccode
        self.run_without_screen_refresh = str(run_without_screen_refresh).lower() # because Python title-cases booleans

        self.prototype = CustomBlockPrototype(self.proccode, self.run_without_screen_refresh)
        self.prototype.parent = self.id
        self.prototype.shadow = True
        self.inputs = {"custom_block": [1, str(self.prototype.id)]}
        self.contained_blocks.append(self.prototype)

    def getParameters(self):
        self.parameters = []
        # List of "s" and/or "b"
        parameter_types = [i[0] for i in self.proccode.split("%")[1:]]
        argumentdefaults = []

        for parameter_type in parameter_types:
            parameter = CustomBlockReporter(parameter_type)
            parameter.parent = self.prototype.id
            parameter.shadow = True
            self.parameters.append(parameter)

            # Honestly I think this list is useless but it has to exist or else it doesn't work
            argumentdefaults.append("" if parameter_type == "s" else False)

        self.argumentids = [parameter.argument_id for parameter in self.parameters]
        self.argumentnames = [parameter.name for parameter in self.parameters]
        self.prototype.mutation.update({
            "argumentids": JSONify(self.argumentids),
            "argumentnames": JSONify(self.argumentnames),
            "argumentdefaults": JSONify(argumentdefaults)
        })

        return self.parameters if len(self.parameters) != 1 else self.parameters[0]

    def setScript(self, *args):
        for block in args:
            self.parent_script._addBlock(block)

        return self._callable()

    def _callable(self):
        proccode = self.proccode
        argumentids = self.argumentids
        parameters = self.parameters
        run_without_screen_refresh = self.run_without_screen_refresh

        # Making closures is so satisfying when you get the chance
        class CustomBlockCallable(Block):
            def __init__(self, *args):
                super().__init__(_get(self))

                self.arguments = args

                for parameter, argument in zip(parameters, args):
                    self._addInput(parameter.json_type, str(parameter.argument_id), argument)

                self.mutation = {
                    "proccode": proccode,
                    "argumentids": JSONify(argumentids),
                    "warp": run_without_screen_refresh
                }

        return CustomBlockCallable

class CustomBlockPrototype(Block):
    def __init__(self, proccode, run_without_screen_refresh):
        super().__init__(_get(self))
        self.mutation = {
            "proccode": proccode,
            "warp": run_without_screen_refresh
        }

class CustomBlockReporter(Reporter):
    def __init__(self, type, generateArgumentID=True):
        super().__init__(_get(type), generateID=False)
        if generateArgumentID:
            self.argument_id = generateID("argument ID")

        self.type_argument = type
        self.json_type = JSON_STRING if type == "s" else JSON_SPECIAL

        self.name = str(generateID("argument name"))
        self._addField("VALUE", self.name)

    def _asInputValue(self):
        return [3, self.id]

    # This reporter is semi-initialized because a new ID is generated
    # each time its referenced, so we do a little copying
    def _copy(self):
        new_instance = self.__class__(self.type_argument, False)
        new_instance.__dict__.update(self.__dict__)
        new_instance._refreshID()

        return new_instance
