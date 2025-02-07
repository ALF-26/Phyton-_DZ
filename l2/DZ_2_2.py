num = int(input ('введіть 5-ти значне число: '))
n1 = num % 10
num //= 10
n2 = num % 10
num //= 10
n3 = num % 10
num //= 10
n4 = num % 10
num //= 10
n5 = num % 10
reversed_num = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
print ('перевернуте число', reversed_num)