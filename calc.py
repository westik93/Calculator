# Калькулятор 

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK)
print(Back.GREEN)

what = input('Какую математическую операцию хотите произвести? (+, -, *, /):')

print(Back.CYAN)

a = float(input('Введите первое число: '))
print(Back.RED)
b = float(input('Введите второе число: '))

print(Back.YELLOW)

if what == '+':
	c = a + b
	print('Результат: ' + str(c))
elif what == '-':
	c = a - b
	print('Результат: ' + str(c))
elif what == '*':
	c = a * b
	print('Результат: ' + str(c))
elif what == '/':
	c = a / b
	print('Результат: ' + str(c))
else:
	print('Выбрана неверная операция!')

input()
