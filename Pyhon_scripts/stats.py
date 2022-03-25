import json


with open("data.json") as file:
    data = json.loads(file.read())
    people = {} 
    for d in data:
        i = data[d]["fields"]["id"]
        for k in data[d]["fields"]:
            if k == "id": continue
            people[i][k] = data[d]["fields"][k]

print(people[0])
            
