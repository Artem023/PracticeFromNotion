from random import randint
random_number = randint(10, 99)
print(random_number)

number1 = random_number % 10
number2 = random_number // 10

if (number1 > number2):
    max = number1
else: max = number2

print ("The largest digit of the number", random_number, "is", max)
