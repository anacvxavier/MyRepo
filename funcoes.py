def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

fuel_report(main=100, external=100, emergency= 50)