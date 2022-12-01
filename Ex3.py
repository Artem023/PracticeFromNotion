num_day = int (input ("Enter random day of the week: "))
day_of_week = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
index = 0
size = len(day_of_week)

while (index < size):
    if num_day - 1 == day_of_week[index]:
        print(day_of_week[index])

    else: index += 1
