import hashlib
import os

image_extensions = ("png", "jpg", "jpeg", "gif", "bmp", "webp")

class Asset:
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        self.format = os.path.splitext(self.file_path)[1][1:]

        with open(self.file_path, "rb") as handle:
            self.data = handle.read()

        # Asset filename is its own checksum
        self.md5 = hashlib.md5(self.data).hexdigest()
        self.md5ext = f"{self.md5}.{self.format}"

    def _asFieldValue(self):
        return [self.name, None]

    def _serialize(self):
        dictionary = {
            "name": self.name,
            "dataFormat": self.format,
            "assetId": self.md5,
            "md5ext": self.md5ext
        }

        if self.format in image_extensions:
            dictionary.update({"bitmapResolution": 1})

        return dictionary
