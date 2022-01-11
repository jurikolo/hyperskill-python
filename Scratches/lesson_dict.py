fav_flowers = {'Alex': 'field flowers', 'Kate': 'daffodil', 'Eva': 'artichoke flower', 'Daniel': 'tulip'}
fav_flowers['Alice'] = 'govno'
print(fav_flowers)

asdf = dict({43:'Omm', 45:'Bomm', '12':'Bimm'})
# asdf2 = dict(43=='Omm', 45=='Bomm', 12=='Bimm')
print("=====")
print("=====")
first_family = {"wife": "Janet", "wife's mother": "Katie", "wife's father": "George"}
second_family = {"husband": "Leon", "husband's mother": "Eva", "husband's father": "Gaspard", "husband's sister": "Isabelle"}
first_family.update(second_family)
print(first_family)

print("=====")
print("=====")
meals = [
    {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
    {"title": "Italian salad with fusilli and ham", "kcal": 320},
    {"title": "Bulgur with vegetables", "kcal": 350},
    {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
    {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
for x in meals:
    print(x.get("kcal"))

print("=====")
print("=====")
planets_diameter_km = {'Earth': 12742, 'Mars': 6779}

# correct but long way
planets_diameter_mile = {}
for key, value in planets_diameter_km.items():
    planets_diameter_mile[key] = round(value / 1.60934, 2)
# alt way: planets_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in planets_diameter_km.items()}
print(planets_diameter_mile)  # {'Mars': 4212.29, 'Earth': 7917.53}

print("=====")
print("=====")
user_input = "a aa abC aa ac abc bcd a".lower().split(" ")
my_dict = {}
for x in user_input:
    if x not in my_dict.keys():
        my_dict.update({x: 1})
    else:
        val = my_dict.get(x)
        my_dict.update({x: val + 1})

# my_dict = {x for x in user_input}
for key, value in my_dict.items():
    print(key)

print("=====")
print("=====")
potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"},
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]

result = []
for x in potential_dates:
    if x.get("age") >= 30 and "art" in x.get("hobbies") and x.get("city") == "Berlin":
        result.append(x.get('name'))
print(", ".join(result))

print("=====")
print("=====")
my_dict = {"a": 43, "b": 1233, "c": 8}
first_item = my_dict.popitem()
result_dict = {"min_key": first_item[0], "min_value": first_item[1], "max_key": first_item[0], "max_value": first_item[1]}
for key, value in my_dict.items():
    if value > result_dict["max_value"]:
        result_dict.update({"max_key": key})
        result_dict.update({"max_value": value})
    if value < result_dict["min_value"]:
        result_dict.update({"min_key": key})
        result_dict.update({"min_value": value})
print(f"min: {result_dict.get('min_key')}")
print(f"max : {result_dict.get('max_key')}")
