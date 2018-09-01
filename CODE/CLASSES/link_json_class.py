import json


class Link(object):
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = json.load(open(json_file))

    def load_template(self):
        template = {"stock": [], "tableau": [[], [], [], [], [], [], []],
                    "foundation": {"Hearts": [], "Spades": [], "Diamonds": [], "Clubs": []}, "waste": []}
        j = json.dumps(template, indent=4)
        f = open(self.json_file, 'w')
        print(j, file=f)
        f.close()

    def insert_to_file(self, where, info):
        with open(self.json_file, "r+") as jsonFile:
            data = json.load(jsonFile)
            assert isinstance(data, object)
            data[where].append(info)
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile, indent=4)
            jsonFile.truncate()

    @staticmethod
    def recursive_iter(obj):
        if isinstance(obj, dict):
            for thing in obj.values():
                yield from Link.recursive_iter(thing)
        elif any(isinstance(obj, t) for t in (list, tuple)):
            for thing in obj:
                yield from Link.recursive_iter(thing)
        else:
            yield obj

    def iter_through(self):
        for item in Link.recursive_iter(self.data):
            print(item)

    def __str__(self):
        return "{}".format(self.data)
