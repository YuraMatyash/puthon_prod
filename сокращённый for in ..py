all_nums = [23, 43, -433, 4, -6]

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)

print(all_nums)
# пример для наборов
my_set = {1, 10, 15}

new_set = {val * val for val in my_set}

print(new_set)
print(my_set)
# также можно и словари
my_scores = {
    'a': 1,
    'b': 2,
    's': 10
}
new_scores = {k: v * 10 for k, v in my_scores.items()}
print(new_scores)