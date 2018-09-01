from __future__ import unicode_literals
import re
import json

# This ensures that we use 'str' in Python 3, and 'unicode' in Python 2
PythonString = "".__class__


class JsonTraverseParser:
    def __init__(self, fptr, custom_json_impl=None):
        if fptr and not isinstance(fptr, PythonString):
            raise TypeError("the 'file pointer' argument must be {}, not '{}'".format(PythonString, type(fptr)))

        try:
            with open(fptr, "r+") as jsonFile:
                json_impl = custom_json_impl or json
                self.data = json_impl.load(jsonFile) if jsonFile else None

        except FileNotFoundError:
            raise FileNotFoundError('the file named {} has not been found'.format(fptr))

    def traverse(self, path, force_list=False):
        if not isinstance(path, PythonString):
            raise TypeError("the 'path' argument must be {}, not '{}'".format(PythonString, type(path)))

        reduced = []

        if self.data:
            reduced.append(self.data)

        if path:
            for item in path.split("."):
                print(item)
                list_reduced = list(reduced)
                # index for a list
                if self.is_valid_index(item):
                    print("VALID INDEX")
                    list_reduced = self.reduce_list(reduced, item)

                dict_reduced = self.flatten(reduced)
                if not list_reduced or list_reduced == reduced:
                    dict_reduced = self.reduce_dict(dict_reduced, item)

                if list_reduced and list_reduced != reduced:
                    reduced = list_reduced
                elif dict_reduced and dict_reduced != self.flatten(reduced):
                    reduced = dict_reduced
                else:
                    reduced = []

        if isinstance(reduced, list) and len(reduced) == 1:
            reduced = reduced[0]

        if isinstance(reduced, list) and len(reduced) == 0:
            reduced = None

        if force_list and not isinstance(reduced, list):
            if reduced is None:
                reduced = []
            else:
                reduced = [reduced]

        return reduced

    def reduce_list(self, reduced, item):
        outputs = []

        for value in reduced:
            try:
                outputs.append(value[int(item)])
            except (ValueError, IndexError, KeyError, TypeError):
                pass

        return outputs

    def reduce_dict(self, reduced, item):
        outputs = []

        for value in reduced:
            try:
                outputs.append(value[item])
            except (KeyError, TypeError):
                pass

        return outputs

    # returns only lists found in the reduced input
    def flatten(self, reduced):
        flattened = []
        for value_or_sublist in reduced:
            if isinstance(value_or_sublist, list):
                flattened += value_or_sublist
            else:
                flattened.append(value_or_sublist)
        return flattened

    def is_valid_index(self, string):
        return re.match(r"^(0|[1-9][0-9]*)$", string)
