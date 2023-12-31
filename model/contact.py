from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, all_phones_from_home_page=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 email=None, email2=None, email3=None, address=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s%s:%s:%s:%s%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename,
                                                   self.address, self.mobilephone, self.workphone,
                                                   self.secondaryphone, self.email, self.email2, self.email3)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id)
                and self.firstname == other.firstname and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
