lst = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
#lst = [1, 2, 3] #=> [[1, 2], [3]]
#lst = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#lst = [1] #=> [[1], []]
#lst = [] #=> [[], []]

if len(lst) % 2 == 0:
    mid = len(lst) // 2
    new_list = [lst[:mid], lst[mid:]]
else:
    mid = len(lst) // 2 + 1
    new_list = [lst[:mid], lst[mid:]]

print(new_list)