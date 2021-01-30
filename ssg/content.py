import re
from typing import Iterator, _T_co

from yaml import (load, FullLoader)
from collections.abc import Mapping


class Content(Mapping):

    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = Content.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data += {"content": content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    @type.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)
