import getopt
import os
import sys
import jsonpickle
from generator.data_generators import *
from model.contact import Contact


def usage():
    print("Usage: script.py -n <number of groups> -f <file>")
    print("Options:")
    print("  -n, --number   Specify the number of contacts")
    print("  -f, --file     Specify the file name")


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata = [
    Contact(lastname=random_name(6), firstname=random_name(12), address=random_string(10),
            email=random_email(6, "bor.com"), email2=random_email(7, "@test"),
            email3=random_email(10, "@kom.biz"), homephone=random_phone("+381", 7),
            mobilephone=random_phone("+7(952)", 8), workphone=random_phone("+7-981", 4),
            fax=random_phone("9-1-2", 8))
    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata, unpicklable=False, indent=2))
