
num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))

import math
if (num1 > 0) or (num2 > 0):
    if (math.sqrt(num1) == num2) or (math.sqrt(num2) == num1):
        print ("Является квадратом числа")
    else: print ("Не является квадратом числа")
else: print ("Введите новое число")