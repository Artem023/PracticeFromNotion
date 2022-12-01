number = int (input ("Enter three digits number: "))
num = number

if (99 < num < 1000):
    num = num % 10
    print ("Last digit of number", number, "is", num)
else: print ("You enter wrong number")