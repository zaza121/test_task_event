from models import Registry, Registrant
from tools import *

def getRegistrantFromJson(json_data):
    pass

# init data
environment = Registry()
result = None
registrantList = []

print("TEST SAVE REGISTRANT")
print("====================")

number_of_contact_before = len(environment.contacts.getAll())
number_of_lead_before = len(environment.leads.getAll())
print("before test: %d contacts" % number_of_contact_before)
print("before test: %d lead" % number_of_lead_before)



json_test = """
[
{
  "registrant":
     {
        "name": "Lucy Liu",
        "email": "lucy@liu.com",
        "phone": ""
     }
},

{
  "registrant":
     {
        "name": "Doug",
        "email": "doug@emmy.com",
        "phone": "4564445556"
     }
},

{
  "registrant":
     {
        "name": "Uma Thurman",
        "email": "uma@thurs.com",
        "phone": ""
     }
}

]
"""

registrantList = transformJsonToObject(json_test)

for registrant_dict in registrantList:

    # convert dict to Registrant
    registrant = Registrant(registrant_dict)
    registrant.save(environment)

print("-----------------------")
print("-----------------------")

number_of_contact_after = len(environment.contacts.getAll())
number_of_lead_after = len(environment.leads.getAll())
print("after test: %d contacts" % number_of_contact_after)
print("after test: %d leads" % number_of_lead_after)


answer = environment.contacts.findContactByEmail("uma@thurs.com")
assert answer[0].name == "Uma Thurman"
