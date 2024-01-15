def person_age(percon):
    percon['age'] += 1
    return percon

person_one = {
    'name': 'bob',
    'age': 21
}
person_age(person_one)

print(person_one)
