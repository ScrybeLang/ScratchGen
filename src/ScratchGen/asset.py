import hashlib
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

class Asset:
    def __init__(self, *args):
        self.name, self.file_path = parsePath(*args)

        self.format = os.path.splitext(self.file_path)[1][1:]

        with open(self.file_path, "rb") as handle:
            self.data = handle.read()

        # Asset filename is its own checksum
        self.md5 = hashlib.md5(self.data).hexdigest()
        self.md5ext = f"{self.md5}.{self.format}"

    def _asFieldValue(self):
        return [self.name, None]

    def _serialize(self):
        return {
            "name": self.name,
            "dataFormat": self.format,
            "assetId": self.md5,
            "md5ext": self.md5ext
        }
