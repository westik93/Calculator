# Калькулятор 

what = input('Какую математическую операцию хотите произвести? (+, -, *, /):')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

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
