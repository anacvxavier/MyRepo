rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# impime os itens do docionario
'''
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
'''
# Because december exists, the value will be 3.1
'''
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
'''

# june não existe, então vai acrescentar e atribuir um valor
if 'june' in rainfall:
    rainfall['june'] = rainfall['june'] + 1
else:
    rainfall['june'] = 1

# usar values() para determinar o volume total de chuva:
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall} cm in the last quarter.')

