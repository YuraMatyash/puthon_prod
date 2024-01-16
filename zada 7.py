def merge_lists_to_dict(**arg):
    print(arg)
    my_zip = arg['list1']
    my_dict = arg['list2']
    return my_zip,my_dict
# если так задавать то только квадратные скобки
print(merge_lists_to_dict(list1=[1, 2, 3],list2=[4, 5, 5]))

