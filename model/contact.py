from sys import maxsize


class Contact:

    def __init__(self, lastname=None, firstname=None, email=None, contact_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.contact_id = contact_id

    def __repr__(self):
        return "Contact(%s: %s %s)" % (self.contact_id, self.lastname, self.firstname)

    def __eq__(self, other):
        return ((self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)
                and self.lastname == other.lastname and self.firstname == other.firstname)

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
