import json 

# JavaScript Object Notation

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "603-472-3721",
            "emails": ["johnsmith@outlook.com", "john.sm@gmail.com"],
            "has_license": false
        },
          {
            "name": "Harry Lias",
            "phone": "923-521-9533",
            "emails": ["harry342@outlook.com", "harrylias@gmail.com"],
            "has_license": true
        }
    ]
}
'''

# USE LOADS AND DUMPS WHEN WORKING WITH STRINGS /// USE LOAD AND DUMP WHEN WORKING WITH FILES

# use the loads method to convert a json object into a python dictionary
data = json.loads(people_string)

# now can loop through all information
# for person in data['people']:
#     print(person)

# remove the phone numbers from all entries and convert it back into a json string
for person in data['people']:
    del person['phone']

# use the json dumps to convert it all back into a string
new_string = json.dumps(data, indent=2, sort_keys=True) # format the json nicely by using the indent key (can also use sortkeys to sort all the keys alphabetically)

print(new_string)



# print(data)
# print(type(data))
# print(type(data['people']))