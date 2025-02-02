import random
numbers_in_list = random.randint(3, 10)
my_list = [random.randint(1,100) for i in range(numbers_in_list)]
new_list = [my_list[0], my_list[2], my_list[-2]]
print('Початковий список', my_list)
print('Новий  список з першого, третього, і другого з кінця', new_list)