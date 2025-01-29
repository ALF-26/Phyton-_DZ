print ('Калькулятор')
n1 = int (input('Введіть число 1: '))
n2 = int (input('Введіть число 2: '))

x = int (input('Яку операцію виконати? \n 1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n'))

if x == 1:
    result = n1 + n2
    addition = 'додавання'
    action = addition
if x == 2:
    result = n1 - n2
    subtraction = 'віднімання'
    action = subtraction
if x == 3:
    result = float(n1 / n2)
    division = 'ділення'
    action = division
if x == 4:
    result = n1 * n2
    multiplication = 'множення'
    action = multiplication
print ('Результат ' ,action,' = ',result)