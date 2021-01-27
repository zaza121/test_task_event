

class Lead:
    """Lead Class."""
    name = ""
    email = ""
    phone = ""

    def __init__(self, name="", email="", phone=""):

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
