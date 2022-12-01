from random import randint
random_number = randint(0, 100)
print (random_number)

number = int (input ("Enter a number: "))

if (random_number % number == 0):
    print ("Число кратно")
else: print ("Остаток = ", random_number % number )