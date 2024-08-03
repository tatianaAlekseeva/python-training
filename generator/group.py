import os
import getopt
import sys
import jsonpickle
from generator.data_generators import random_string_with_prefix
from model.group import Group


def usage():
    print("Usage: script.py -n <number of groups> -f <file>")
    print("Options:")
    print("  -n, --number   Specify the number of groups")
    print("  -f, --file     Specify the file name")


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string_with_prefix("name", 10), header=random_string_with_prefix("header", 20),
          footer=random_string_with_prefix("footer", 15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
