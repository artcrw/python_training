from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_number(maxlen):
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))]) + "@gmail.com"


testdata = [Contact(firstname="", middlename="", lastname="", mobilephone="")] + [
    Contact(firstname=random_string("first", 10), middlename=random_string("middle", 10),
            lastname=random_string("last", 10), address=random_string("addr1", 10),
            mobilephone=random_number(10), workphone=random_number(10), secondaryphone=random_number(10),
            email=random_email(10), email2=random_email(10), email3=random_email(10))
    for _ in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))