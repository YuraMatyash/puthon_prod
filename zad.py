def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

new_list = 10
new_der = 5

res = my_fn(new_list, new_der)

print(res)

print(new_list)
# передача неизменяемых объектов (а) ссылается к ссылке new_list а (b) к new_der