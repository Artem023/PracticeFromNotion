number = int (input ("Enter the number of the day of the week: "))

if (number > 0) and (number < 8):
    if (number == 6) or (number == 7):
        print("It's the weekend!")
    else: print ("It's not the weekend")
else: print ("This day of the week doesn't exist")