import json
#
# data = '''{
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false,
#       "salary": 1500
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true,
#       "salary": 1700
#     },
#     {
#       "name": "Steven Cooke",
#       "phone": null,
#       "emails": "stevencooke@example.com",
#       "has_licence": true,
#       "salary": 2500
#     }
#   ]
# }'''
#
# js_data = json.loads(data)
# print(js_data)
# print(type(js_data))
# del js_data['people'][1]['name']   #udalajet imja
#
# new_json = json.dumps(js_data, indent=2)
# print(new_json)

with open('data.json', 'r', encoding='UTF8') as file:
    data = json.load(file)
    print(data)

for person in data['people']:
    if person['has_licence'] == False:
        del person['has_licence']

with open('new_data.json', 'w', encoding='UTF8') as file:
    json.dump(data, file, indent=4)
