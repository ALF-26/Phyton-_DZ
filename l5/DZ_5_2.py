print ('Вітаю в калькуляторі!')
while True:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operator = input("Яку операцію виконати? (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "На нуль ділити не можна!"
    else:
        result = "Невідома операція"
    print ('Результат операції ', result)

    continue_calc = input("Бажаєте продовжити? (y/n): ").lower()
    if continue_calc != 'y' and continue_calc != 'yes':
        print("Дякую, калькулятор завершив роботу!")
        break