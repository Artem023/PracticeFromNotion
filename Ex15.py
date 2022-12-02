from random import randint
rnd_number = randint (0, 100000)

if (rnd_number % 7 == 0) and (rnd_number % 23 == 0):
    print ("The number", rnd_number, "is multiply")
else: print ("The number", rnd_number, "isn't multiply")