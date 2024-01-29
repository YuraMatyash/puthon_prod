while True:
     try:
        nun1 = float(input('введите первое число: '))
        nun2 = float(input('введите второе число: '))
     except Exception as e:
        print(e)
        continue

     print(nun1 / nun2)
     wish = input('хотите продолжить yes/no: ')
     if wish == 'yes':
        continue
     if wish == 'no':
        break