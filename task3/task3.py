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

#В ТЗ не указано как формируется файл tests.json
#Насколько я понимаю из примера получить доступ к значению можно так:
#tests['tests'][0]['values'][1]['values'][0] ... ['values'][n]
    
def rput(arr, val):
    for elem in arr:
        if elem['id'] in val:
            #Проверка на случай если нет информации для id
            elem['value'] = val[elem['id']]
        if 'values' in elem:
            elem['values'] = rput(elem['values'], val)
    return arr

tests['tests'] = rput(tests['tests'], val)

with open('report.json', 'w') as file:
    json.dump(tests, file)
