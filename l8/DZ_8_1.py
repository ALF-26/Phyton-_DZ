def add_one(some_list):
   number = "".join([str(i) for i in some_list])
   number = int(number) + 1
   new_str = str(number)
   new_list = []
   i = 0
   while i < len(new_str):
       new_list.append(int(new_str[i]))
       i = i + 1
   return new_list

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")