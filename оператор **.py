button = {
    'width': 200,
    'height': 50,
}

red_button = {
    **button,  #расспаковка словаря баттон и добавление ещё одного ключа
    'color':'red'
}

print(red_button)

print(button)

green_button = {
    'wid': 2004,
    'color': 'green'
}


error_button = {
    **button,  #расспаковка словаря баттон
    **green_button # расспаковка словаря грен батон и втоже время обединение двух словарей
}

edinarog = button | green_button # можно обединить и так но тут важен порядок

print(edinarog)

print(error_button)