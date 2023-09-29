from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="", port=3307)

try:
    l = db.get_contacts_not_in_group(Group(id="184"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
