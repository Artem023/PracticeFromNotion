number = int (input ("Enter a number: "))
num = number

if (99 < number < 1000):
    number = number % 100 // 10
    print ("The second digit of number", num, "=", number)
else: print ("You enter wrong number")