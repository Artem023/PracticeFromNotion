from random import randint
random_number = randint(100, 999)

num1 = random_number // 100
num2 = random_number // 10 % 10
num3 = random_number % 10
new_number = num1 * 10 + num3

print (random_number, "without second digit -->", new_number )