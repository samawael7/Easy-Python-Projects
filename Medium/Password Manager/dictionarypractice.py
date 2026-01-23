human = {
    'name' : 'sama',
    'age' : 22,
    'major' : 'data engineering'
}

print(human)
print(human.items())
print(human.keys())
print(human.values())

human['sex'] = 'female'
print(human)
print(human['name'])
print(human['age'],human['sex'])

human_set = set(human)
print(human_set)

human_set_vals = set(human.values())
print(human_set_vals)

print(human)

# nested dictionary

human2 = {
    'name2' : 'omnia',
    'age2' : 25,
    'languages' : ['arabic', 'english']
}

print(human2)
print(human2.values())
print(human2['languages'])
print(human2['languages'][0])


employees = {
    1 : {'name' : 'sama', 'age' : '22', 'role' : 'data eng'},
    2 : {'name' : 'israa', 'age' : '23', 'role' : 'ai eng'}
}

print(employees[1])
print(employees[1]['name'])

employees[3] = {'name' : 'omnia', 'age' : '25', 'role' : 'real state'}
print(employees) 
del employees[2]['role']
print(employees)