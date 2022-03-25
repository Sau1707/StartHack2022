# libraries
import json

from scipy.fft import idct
'''
{
    "datasetid": { "properties-social-assistance-recipient-city-st-gallen", // Not useful
    "fields": {
        "age_categories": "46-55",
        "dossier_art": "Ausl\u00c3\u00a4nder/innen",
        "id": "id01115",
        "in_ch_seit_geb": "FALSE",
        "last_occupation_category": "sales_force",
        "national_categories": "EU / EFTA",
        "persons_in_household_total": "single household",
        "person_household_subsistence_unit": "1",
        "person_category": "Single",
        "product_last_dossier_version": "social_assistance_benefit",
        "civil_status": "divorced"
    },
    "record_timestamp": "2022-03-23T17:23:20.019+01:00", // not useful
    "recordid": "729b30cf6324e9c17bccd1e4970e5164f36fac53" //not useful, or?
}
'''
# fancy print 
def fprint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))


with open("data.json") as file:
    data = json.loads(file.read())

types = {}
for d in data:
    for i in d["fields"]:
        if i not in types: types[i] = []
        if d["fields"][i] not in types[i]:
            types[i].append(d["fields"][i])

for key in types.copy():
    print("-------------------")
    if len(types[key]) > 40: 
        print(key, "longer than 20")
        del types[key]
        continue
    print(key, "-->", types[key])

with open("value.txt","w") as file:
    for key in types:
        file.write(key)
        file.write("\n")
        file.write(f"0) Not avable")
        file.write("\n")
        for i,e in enumerate(types[key]):
            file.write(f"{i+1}) {e}")
            file.write("\n")
        file.write("\n")
        file.write("\n")


'''
Convert the file

'''

fany = []
for d in data:
    row = d["fields"]["id"]
    print(row)
    for type in types:
        if type not in d["fields"]: 
            row += ",0"
            continue
        if type == "erwerbssituation":
            if (types[type].index(d["fields"][type]) + 1) == 15:
                row += ",6"
                continue
            if (types[type].index(d["fields"][type]) + 1) == 16:
                row += ",6"
                continue
            if (types[type].index(d["fields"][type]) + 1) == 17:
                row += ",3"
                continue
            if (types[type].index(d["fields"][type]) + 1) == 19:
                row += ",13"
                continue
            if (types[type].index(d["fields"][type]) + 1) == 20:
                row += ",17"
                continue
            if (types[type].index(d["fields"][type]) + 1) == 22:
                row += ",2"
                continue
        row += "," + str(types[type].index(d["fields"][type]) + 1) 
    if "letzte_berufliche_tatigkeit_kategorie" not in d["fields"]: row += ",0"
    elif d["fields"]["letzte_berufliche_tatigkeit_kategorie"].strip() == "" or d["fields"]["letzte_berufliche_tatigkeit_kategorie"] == "kein | keine":
        row += ",1"
    else:
        row += ",0"
    if "erlernter_beruf_kategorie" not in d["fields"]: row += ",0"
    elif d["fields"]["erlernter_beruf_kategorie"].strip() == "" or d["fields"]["erlernter_beruf_kategorie"] == "kein | keine":
        row += ",1"
    else:
        row += ",0"
    fany.append(row)

with open("data.csv","w") as file:
    for el in fany:
        file.write(el)  
        file.write("\n")
