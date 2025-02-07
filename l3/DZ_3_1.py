print ('Калькулятор')
n1 = int (input('Введіть число 1: '))
n2 = int (input('Введіть число 2: '))

x = input ('Яку операцію виконати?, +, -, *, / ')

if x == "+":
    result = n1 + n2
    addition = 'додавання'
    action = addition
if x == "-":
    result = n1 - n2
    subtraction = 'віднімання'
    action = subtraction
if x == "/":
    result = float(n1 / n2)
    division = 'ділення'
    action = division
if x == "*":
    result = n1 * n2
    multiplication = 'множення'
    action = multiplication
print ('Результат ' ,action,' = ',result)