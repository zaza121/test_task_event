from . import Contact


class Registrant:
    """Contact Class."""

    name = ""
    email = ""
    phone = ""

    def __init__(self, dict_value=""):

        self.name = dict_value.get("name")
        self.email = dict_value.get("email")
        self.phone = dict_value.get("phone")

    def save(self, environment):
        """Save the registrant."""
        # 1) Try to match registrant's email to our Contacts list
        result = environment.contacts.findContactByEmail(self.email)

        # 2) If not matched, try to match registrant's phone to our Contacts list
        if not result:
            result = environment.contacts.findContactByPhone(self.phone)

        # Otherwise try to match our LeadsList with email
        if not result:
            result = environment.leads.findLeadByEmail(self.email)

            # (if Lead is matched, remove it from LeadsList and add to ContactsList)
            if result:

                lead = result[0]
                environment.leads.deleteLeadByEmail(lead.email)
                new_contact = Contact(lead.name, lead.email, lead.phone)
                environment.contacts.addContact(new_contact)

        # Else match our Leads with phone (same rule as above applies)
        if not result:
            result = environment.leads.findLeadByPhone(self.phone)
            # (if Lead is matched, remove it from LeadsList and add to ContactsList)
            if result:
                lead = result[0]
                environment.leads.deleteLeadByPhone(lead.phone)
                new_contact = Contact(lead.name, lead.email, lead.phone)
                environment.contacts.addContact(new_contact)

        # If not matched, simply add it to ContactsList
        if not result:
            new_contact = Contact(self.name, self.email, self.phone)
            environment.contacts.addContact(new_contact)
