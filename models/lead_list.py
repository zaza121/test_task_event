from .lead import *


class LeadList:
    """Lead List Class."""
    default_database = [
        {"name": None, "email": "kevin@keith.com", "phone": None},
        {"name": "Lucy", "email": "lucy@liu.com", "phone": "3210001112"},
        {"name": "Mary Middle", "email": "mary@middle.com", "phone": "3331112223"},
        {"name": None, "email": None, "phone": "4442223334"},
        {"name": None, "email": "ole@olson.com", "phone": None},
        {"name": "Tom Jones","email": "","phone": "3211234567",} # test purpose
    ]
    leadDatabase = []

    def __init__(self):

        for elt in self.default_database:
            lead = Lead(elt.get("name"), elt.get("email"), elt.get("phone"))
            self.leadDatabase.append(lead)

    def findLeadByEmail(self, email):
        """Return all lead with this email."""
        return [ld for ld in self.leadDatabase if ld.email == email]

    def findLeadByPhone(self, phone):
        """Return all lead with this phone number."""
        return [ld for ld in self.leadDatabase if ld.phone == phone]

    def getAll(self):
        """Get all elements in database."""
        return self.leadDatabase

    def deleteLeadByEmail(self, email):
        """Delete a elt based on email."""
        result = self.findLeadByEmail(email)
        if result:
            self.leadDatabase = [elt for elt in self.leadDatabase if elt.email != email]

    def deleteLeadByPhone(self, phone):
        """Delete a elt based on phone."""
        result = self.findLeadByPhone(phone)
        if result:
            self.leadDatabase = [elt for elt in self.leadDatabase if elt.phone != phone]
