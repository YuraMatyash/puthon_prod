def filter_list(lst, typ):
    deder = []
    for i in lst:
        if type(i) == typ:
            deder.append(i)
    return (deder)

print(filter_list([35, True, 'ads',10], int))