from random import randint
random_number = randint(0, 100000)

if random_number < 100:
    print ("Number", random_number, "don't have third digit")
    
else:
    print("Third digit of number", random_number, "-->", end = " ")
    while (random_number > 999):
        random_number /= 10

random_number = random_number % 10 

print (int(random_number))