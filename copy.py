def person_age(percon):
    person_copy = percon.copy()
    person_copy['age'] += 1
    return person_copy

person_one = {
    'name': 'bob',
    'age': 21
}

person_new = person_age(person_one)

print(person_new)

print(person_one)
# создали копию персон оне для того чтобы в функции её можно было изменить и не затронуть аригинал персон оне