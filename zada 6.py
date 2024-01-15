def merge_lists_to_dict(list1, list2):
    my_zip = zip(list1,list2)
    my_dict = dict(my_zip)
    return my_dict

list1 = ['apple', 'banana', 'fryts']

list2 = [20, 50, 100]

print(merge_lists_to_dict(list1, list2))