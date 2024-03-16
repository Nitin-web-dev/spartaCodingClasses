num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]


# Find the largest number in a list

max_value = 0

for num in num_list:
    if num > max_value:
        max_value = num


print(max_value)