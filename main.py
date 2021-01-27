from models import Registry, Registrant
from tools import *

def getRegistrantFromJson(json_data):
    pass

# init data
environment = Registry()
result = None
registrantList = []

# get the json data
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
# registrantList.append(Registrant(json_test))

for registrant_dict in registrantList:

    # convert dict to Registrant
    registrant = Registrant(registrant_dict)
    registrant.save(environment)
