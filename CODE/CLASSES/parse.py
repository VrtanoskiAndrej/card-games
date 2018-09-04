from __future__ import unicode_literals
import re
import json

# This ensures that we use 'str' in Python 3, and 'unicode' in Python 2
PythonString = "".__class__


class JParser(object):
    def __init__(self, fptr):
        if fptr and not isinstance(fptr, PythonString):
            raise TypeError("the 'file pointer' argument must be {}, not '{}'".format(PythonString, type(fptr)))

        try:
            with open(fptr, "r+") as jsonFile:
                self.fptr = fptr
                self.data = json.load(jsonFile) if jsonFile else None

        except FileNotFoundError:
            raise FileNotFoundError('the file named {} has not been found'.format(fptr))

    def change(self, path, info):
        if not isinstance(path, PythonString) or not isinstance(info, PythonString):
            raise TypeError("the 'path' and 'info' arguments must both be {},"
                            " not '{}' and '{}' ".format(PythonString, type(path), type(info)))
        path_list = []

        for item in path.split("."):
            if self.is_valid_index(item):
                path_list.append('[{}]'.format(item))
            else:
                path_list.append('["{}"]'.format(item))

        try:
            traverse = "self.data{} = '{}'".format("".join(str(x) for x in path_list), info)
            exec(traverse)
        except IndexError:
            raise IndexError("".join(str(x) for x in path_list))
        except KeyError:
            raise IndexError("".join(str(x) for x in path_list))
        self._update()

    def is_valid_index(self, string):
        return re.match(r"^(0|[1-9][0-9]*)$", string)

    def _update(self):
        with open(self.fptr, "r+") as jsonFile:
            data = json.load(jsonFile)
            assert isinstance(data, object)
            jsonFile.seek(0)  # rewind
            json.dump(self.data, jsonFile, indent=4)
            jsonFile.truncate()

    def insert(self, path, info):
        if not isinstance(path, PythonString):
            raise TypeError("the 'path' arguments must be {}, not '{}'".format(PythonString, type(path)))
        path_list = []

        for item in path.split("."):
            if self.is_valid_index(item):
                path_list.append('[{}]'.format(item))
            else:
                path_list.append('["{}"]'.format(item))

        try:
            traverse = "self.data{}.append('{}')".format("".join(str(x) for x in path_list), info)
            exec(traverse)
        except IndexError:
            raise IndexError("".join(str(x) for x in path_list))
        except KeyError:
            raise IndexError("".join(str(x) for x in path_list))
        self._update()

    def __recursive_iter(self, obj):
        if isinstance(obj, dict):
            for thing in obj.values():
                yield from self.__recursive_iter(thing)
        elif any(isinstance(obj, t) for t in (list, tuple)):
            for thing in obj:
                yield from self.__recursive_iter(thing)
        else:
            yield obj

    def iter_through(self):
        for item in self.__recursive_iter(self.data):
            print(item)

    def count(self):
        item_list = []
        for item in self.__recursive_iter(self.data):
            item_list.append(item)
        return len(item_list)

    def __str__(self):
        return "{}".format(self.data)

    def swap(self, path_a, path_b):
        if not isinstance(path_a, PythonString) or not isinstance(path_b, PythonString):
            raise TypeError("the 'path' arguments must both be {}, not '{}'".format(PythonString, type(path)))
        path_list_a = []
        path_list_b = []

        for item in path_a.split("."):
            if self.is_valid_index(item):
                path_list_a.append('[{}]'.format(item))
            else:
                path_list_a.append('["{}"]'.format(item))

        for item in path_b.split("."):
            if self.is_valid_index(item):
                path_list_b.append('[{}]'.format(item))
            else:
                path_list_b.append('["{}"]'.format(item))

        try:
            traverse = "self.data{}, self.data{} = self.data{}, self.data{}".format(
                "".join(str(x) for x in path_list_a), "".join(str(x) for x in path_list_b),
                "".join(str(x) for x in path_list_b), "".join(str(x) for x in path_list_a))
            exec(traverse)
        except IndexError:
            raise IndexError("".join(str(x) for x in path_list_a), "".join(str(x) for x in path_list_b))
        except KeyError:
            raise IndexError("".join(str(x) for x in path_list_a), "".join(str(x) for x in path_list_b))
        self._update()
