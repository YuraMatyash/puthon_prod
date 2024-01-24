try:
    print(10 / 0)
except ZeroDivisionError as e:  #обработка ошибок заключается в точм что мы прописываем ошибку и выводим текст в терминал
    print(e) # а тут мы создали переменную и в этой переменной хранится текс об ошибке для того чтобы мы не прописывали её сами
    print('Error-Division by zero')

print('Completed')  # и продолжаем код дальше но пользывателю была показана ошибка
def nums (a, d):
    if d == 0:
        raise TypeError('Number') # с помощью раисе сы создали свой текс в ошибке можно написать что хочешь
    return a / d  # возврат суммы а дилённое на д

try:
    nums(10, 0)
except Exception as e:  # универсальная ошибка
    print(e)


print('Completed')