import json
import sys

tests = sys.argv[1]
values = sys.argv[2]

with open(tests, 'r') as file:
    tests = json.load(file)

with open(values, 'r') as file:
    valies = json.load(file)

val = {}
for i in valies['values']:
    val[i['id']] = i['value']
    
def rput(arr, val):
    for i in arr:
        i['value'] = val[i['id']]
        if 'values' in i.keys():
            i['values'] = rput(i['values'], val)
    return arr

tests['tests'] = rput(tests['tests'], val)

print(tests)
