import json

with open("json_file.json", "r") as f:
    my_json = json.load(f)['users']
print(len(my_json))
