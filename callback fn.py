def informat(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")


def outformat(num, callback_fn):
    callback_fn(num)  # функция вызывается внутри другой функции (получается тут )


entered_number = int(input('any number to enter: '))

outformat(entered_number, informat)