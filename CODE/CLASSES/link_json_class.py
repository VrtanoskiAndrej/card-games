import json
from parse import JParser
""" https://github.com/EmilStenstrom/json-traverse/ --- Special Thanks"""


class Link(object):

    def __init__(self, json_file):
        self.json_file = json_file
        try:
            self.data = json.load(open(json_file))
        except FileNotFoundError:
            open(json_file, "w")
        self.setup_jparce()

    def setup_jparce(self):
        jparce = JParser(self.json_file)
        return

    def load_template(self):
        template = {"stock": [], "tableau": [[], [], [], [], [], [], []],
                    "foundation": {"Hearts": [], "Spades": [], "Diamonds": [], "Clubs": []}, "waste": []}
        j = json.dumps(template, indent=4)
        f = open(self.json_file, 'w')
        print(j, file=f)
        f.close()

    def insert_to_file(self, where, info):
        jparce

    def __str__(self):
        return "{}".format(self.data)
