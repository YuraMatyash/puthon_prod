
try:
    while True:
        nun1 = float(input('введите первое число: '))
        nun2 = float(input('введите второе число: '))
        print(nun1 / nun2)
        wish = input('хотите продолжить yes/no: ')
        if wish == 'yes':
             continue
        if wish == 'no':
             break
except Exception as e:
    print(e)
