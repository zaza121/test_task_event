
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

        # clean number
        if phone:
            phone = str(phone)
            phone = phone.replace('(', '')
            phone = phone.replace(')', '')
            phone = phone.replace('-', '')
            phone = phone.replace(' ', '')

            if len(phone) > 10:
                raise ValueError("10 digits only for numbers")

            try:
                phone = int(phone)
            except:
                raise ValueError("Number format not correct")

        self.name = name
        self.email = email
        self.phone = phone
