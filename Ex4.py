num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))
num3 = int (input ("Enter fird number: "))

if (num1 > num2):
    max = num1
else: max = num2

if max > num3:
    print(max)
else:
    max = num3
    print (max)