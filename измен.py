def person_age(percon):
    percon['age'] += 1
    return percon

person_one = {
    'name': 'bob',
    'age': 21
}
person_age(person_one)

print(person_one)
# добавление изменяемых объектов
# функция персон аге ссылается на персон оне и при этом аге +1
# как бы мы не меняли персон оне, персон аге будет зависить от изменений персон оне