num1 = int (input ("Enter a number: "))
num2 = 1

if (num1 > 1):
    print (num2, end = " ")
    while (num2 <= num1):
        if (num2 % 2 == 0):
            print (num2, end = " ")
            num2 += 1
        else: num2 += 1
else: print ("You enter wrong number!")
