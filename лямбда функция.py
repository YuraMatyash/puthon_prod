def greeting(greet):
    return lambda name:f"{greet},{name}"

morning_griting = greeting('Hello')  # эта переменна стала тоже функцией

print(morning_griting('Yura')) # и тут мы можем передавать ей значение

privet = greeting('Hello World')

print(privet('Yuru'))