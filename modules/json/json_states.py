import json

# working with files with JSON

# use json load, with files and use json loads with strings
f = open('states.json', 'r')
data = json.load(f)
f.close()

# loop through the dictionary
for info in data['states']:
    print(info['name'], info['abbreviation'])
    del info['area_codes'] # delete all key and value pair with the area code
    print(info)
    
    
# convert all the data into a JSON File
f = open('new_states.json', 'w')
json.dump(data,f, indent=2) # indent if you want
f.close()