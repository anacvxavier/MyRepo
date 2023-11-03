'''
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=100, external=100, emergency= 50)
'''

'''
def contador (*num):
    print (num)

contador(1, 2, 3, 4, 5)
contador(10, 37, 48)
contador(35, 400, 276, 347, 190)
'''

def soma (*valores):
    s=0
    for num in valores:
        s+=num
    print(s)

soma(2, 4)
soma(2, 5, 6)