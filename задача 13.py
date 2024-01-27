def dict_to_list (dict):
    deder = []
    for k, v in dict.items():
        if type(v) == int:
            v *= 2
        deder.append((k, v))
    return (deder)

print(dict_to_list({'ded': 324, 'id' :True}))