import random
my_list = [random.randint(1, 100) for i in range(random.randint(1, 10))]
sum = 0
for i in my_list:
    if i % 2 == 0: sum += i*my_list[-1]
print ('Вхідний масив', my_list)
print ('Останній елемент', my_list[-1])
print ('Результат парні числа * останній елемент', sum)