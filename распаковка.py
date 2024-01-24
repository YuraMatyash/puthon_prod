my_fryts = ['aplle', 'limon', 'banana']

my_aplle, my_limon, my_banana = my_fryts #порядок следования очснь выжен
my_aple,*ostatkins = my_fryts # другой вариант распаковки также и с картэжам
print(my_aplle)
print(my_limon)
print(my_banana)
print(my_aple)
print(ostatkins)
# также можно и картэжи
my_taple = ('ded', 'nusb', 'dasha')

my_ded, my_nusb, my_dasha = my_taple

print(my_ded)
print(my_nusb)
print(my_dasha)


user_profile = {
    'name': 'Yura',
    'comments_qty': 22,
}
def user_info (name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(**user_profile)) #распаковка словаря в функцию можно только либо 1 либо 2 аргумента передавать