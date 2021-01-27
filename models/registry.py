from .contact_list import *
from .lead_list import *

class Registry:
    """Registry Class."""

    leads = None
    contacts = None

    def __init__(self):

        self.contacts = ContactList()
        self.leads = LeadList()
