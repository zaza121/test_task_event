from .contact import *

class ContactList:
    """Contact List Class."""
    default_database = [
        {"name": "Alice Brown", "email": None, "phone": "1231112223"},
        {"name": "Bob Crown", "email": "bob@crowns.com", "phone": None},
        {"name": "Carlos Drew", "email": "carl@drewess.com", "phone": "3453334445"},
        {"name": "Doug Emerty", "email": None, "phone": "1231112223"},
        {"name": "Egan Fair", "email": "eg@fairness.com", "phone": "5675556667"},
        {"name": "Tom Jones","email": None,"phone": None,} # test purpose
    ]
    contactDatabase = []

    def __init__(self):

        for elt in self.default_database:
            contact = Contact(elt.get("name"), elt.get("email"), elt.get("phone"))
            self.contactDatabase.append(contact)

    def findContactByEmail(self, email):
        """Return all contact with this email."""
        return [ctct for ctct in self.contactDatabase if ctct.email == email]

    def findContactByPhone(self, phone):
        """Return all contact with this phone number."""
        return [ctct for ctct in self.contactDatabase if ctct.phone == phone]

    def getAll(self):
        """Get all elements in database."""
        return self.contactDatabase

    def addContact(self, new_contact):
        """Add contact in database."""
        self.contactDatabase.append(new_contact)
