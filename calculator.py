import sys
from Tkinter import *
import math

calculatorGUI = Tk()
calculatorGUI.geometry("350x400+200+200")
calculatorGUI.title("Calculator V1.0")
welcomLabel = Label(calculatorGUI, text='Welcome to calculator V1.1', fg='#447bd4').pack()

num1, num2, action, result = '0', '0', '', '0'
point = False
error_message = ''

def change_number1():
	return change_number('1')
def change_number2():
	return change_number('2')
def change_number3():
	return change_number('3')
def change_number4():
	return change_number('4')
def change_number5():
	return change_number('5')
def change_number6():
	return change_number('6')
def change_number7():
	return change_number('7')
def change_number8():
	return change_number('8')
def change_number9():
	return change_number('9')
def change_number0():
	return change_number('0')
def change_decimal():
	return change_number('.')

def change_number(n):
	global num1
	global num2
	global num1Label
	global num2Label
	if action == '':
		if num1 == '0':
			num1 = ''
		num1 = num1 + n
		num1Label.config(text = num1)
	else:
		if num2 == '0':
			num2 = ''
		num2 = num2 + n
		num2Label.config(text = num2)

def change_action_plus():
	return change_action('+')
def change_action_minus():
	return change_action('-')
def change_action_multiply():
	return change_action('*')
def change_action_divide():
	return change_action('/')
def change_action_power():
	return change_action('^')
def change_action_sqrt():
	global num1, num2, action, result
	global num1Label, num2Label, actionLabel, resultLabel, errorLabel
	result = str(math.sqrt(float(num1)))
	error_message = ''
	num1 = num2 = '0'
	action = ''
	num1Label.config(text = num1)
	num2Label.config(text = num2)
	resultLabel.config(text = result)
	actionLabel.config(text = action)
	errorLabel.config(text = error_message)


def change_action(act):
	global action
	global actionLabel
	action = act
	actionLabel.config(text = action)

def get_result():
	global num1, num2, action, result
	global num1Label, num2Label, actionLabel, resultLabel, errorLabel
	if action == '+':
		result = str(float(num1) + float(num2))
		error_message = ''
	if action == '-':
		result = str(float(num1) - float(num2))
		error_message = ''
	if action == '*':
		result = str(float(num1) * float(num2))
		error_message = ''
	if action == '/':
		if float(num2) == 0:
			error_message = 'Cannot divide by zero!!!'
		else:
			result = str(float(num1) / float(num2))
			error_message = ''
	if action == '^':
		result = str(float(num1) ** float(num2))
		error_message = ''
	num1 = num2 = '0'
	action = ''
	num1Label.config(text = num1)
	num2Label.config(text = num2)
	resultLabel.config(text = result)
	actionLabel.config(text = action)
	errorLabel.config(text = error_message)

def clear():
	global num1, num2, action, result
	global num1Label, num2Label, actionLabel, resultLabel, errorLabel
	num1 = num2 = result = '0'
	action = error_message = ''
	num1Label.config(text = num1)
	num2Label.config(text = num2)
	resultLabel.config(text = result)
	actionLabel.config(text = action)
	errorLabel.config(text = error_message)

num1Label = Label(calculatorGUI, text = num1)
actionLabel = Label(calculatorGUI, text = action)
num2Label = Label(calculatorGUI, text = num2)
resultLabel = Label(calculatorGUI, text = result)
errorLabel = Label(calculatorGUI, text = error_message)

num1Label.pack()
actionLabel.pack()
num2Label.pack()
resultLabel.pack()
errorLabel.pack()

button1 = Button(calculatorGUI, width = 4, text='1', command = change_number1)
button2 = Button(calculatorGUI, width = 4, text='2', command = change_number2)
button3 = Button(calculatorGUI, width = 4, text='3', command = change_number3)
button4 = Button(calculatorGUI, width = 4, text='4', command = change_number4)
button5 = Button(calculatorGUI, width = 4, text='5', command = change_number5)
button6 = Button(calculatorGUI, width = 4, text='6', command = change_number6)
button7 = Button(calculatorGUI, width = 4, text='7', command = change_number7)
button8 = Button(calculatorGUI, width = 4, text='8', command = change_number8)
button9 = Button(calculatorGUI, width = 4, text='9', command = change_number9)
button0 = Button(calculatorGUI, width = 10, text='0', command = change_number0)

button_plus = Button(calculatorGUI, width = 4, height = 3, text='+', command = change_action_plus)
button_minus = Button(calculatorGUI, width = 4, text='-', command = change_action_minus)
button_multiply = Button(calculatorGUI, width = 4, text='*', command = change_action_multiply)
button_divide = Button(calculatorGUI, width = 4, text='/', command = change_action_divide)
button_power = Button(calculatorGUI, width = 4, text='^', command = change_action_power)
button_sqrt = Button(calculatorGUI, width = 4, text='sqrt', command = change_action_sqrt)
button_decimal = Button(calculatorGUI, width = 4, text = '.', command = change_decimal)
button_equal = Button(calculatorGUI, width = 4, height = 3, text='=', command = get_result)
button_clear = Button(calculatorGUI, width = 4, text = 'C', command = clear)

button1.place(x=100, y=260)
button2.place(x=140, y=260)
button3.place(x=180, y=260)
button4.place(x=100, y=230)
button5.place(x=140, y=230)
button6.place(x=180, y=230)
button7.place(x=100, y=200)
button8.place(x=140, y=200)
button9.place(x=180, y=200)
button0.place(x=100, y=290)
button_plus.place(x=220, y=200)
button_minus.place(x=220, y=170)
button_multiply.place(x=180, y=170)
button_divide.place(x=140, y=170)
button_decimal.place(x=180, y=290)
button_power.place(x=60, y=170)
button_sqrt.place(x=60, y=200)
button_equal.place(x=220, y=260)
button_clear.place(x=100, y=170)



calculatorGUI.mainloop()