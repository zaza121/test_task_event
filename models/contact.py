
NAME_VALUE_NULL = "Name of a contact cannot be empty"

class Contact:
    """Contact Class."""
    name = ""
    email = ""
    phone = ""

    def __init__(self, name="", email="", phone=""):

        if not name:
            print(name)
            raise ValueError(NAME_VALUE_NULL)

        self.name = name
        self.email = email
        self.phone = phone
