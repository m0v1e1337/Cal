from tkinter import *


def is_letter(character):
    if character.isalpha() or (character.isalnum() and not character.isdigit()):
        return True
    else:
        return False


def calculate():
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    result = ''

    if is_letter(num1):
        result = 'Ошибка: введите числовое значение для Числа 1'
    elif is_letter(num2):
        result = 'Ошибка: введите числовое значение для Числа 2'
    else:
        num1 = float(num1)
        num2 = float(num2)
        operation = options.get()

        if operation == 'Сложение':
            result = num1 + num2
        elif operation == 'Вычитание':
            result = num1 - num2
        elif operation == 'Умножение':
            result = num1 * num2
        elif operation == 'Деление':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Ошибка: деление на ноль'
        elif operation == 'Корень':
            result = num1 ** 0.5
        elif operation == 'Факториал':
            fact = 1
            for i in range(1, int(num1) + 1):
                fact *= i
            result = fact
        elif operation == 'Возведение в степень':
            result = num1 ** num2
        elif operation == 'Синус':
            import math
            result = math.sin(num1)
        elif operation == 'Косинус':
            import math
            result = math.cos(num1)
        elif operation == 'Тангенс':
            import math
            result = math.tan(num1)
        else:
            result = 'Ошибка: неверная операция'

    label_result.config(text='Результат: {}'.format(result))


# окно
root = Tk()
root.title('Калькулятор')

# виджеты
frame = Frame(root)
frame.pack(pady=20)

# ввод чисел
label_num1 = Label(frame, text='Число 1:')
label_num1.grid(row=0, column=0)
entry_num1 = Entry(frame)
entry_num1.grid(row=0, column=1)

label_num2 = Label(frame, text='Число 2:')
label_num2.grid(row=1, column=0)
entry_num2 = Entry(frame)
entry_num2.grid(row=1, column=1)

# список операций
options = StringVar(root)
options.set("Сложение")  # Значение по умолчанию
operations_menu = OptionMenu(root, options, "Сложение", "Вычитание", "Умножение", "Деление", "Корень", "Факториал",
                             "Возведение в степень", "Синус", "Косинус", "Тангенс")
operations_menu.pack(pady=10)

# кнопка выполнения
button_calculate = Button(root, text="Вычислить", command=calculate)
button_calculate.pack()

# метка вывода
label_result = Label(root, text='Результат:')
label_result.pack(pady=10)

# вывод
root.mainloop()