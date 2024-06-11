"""
Write a program that works wether if a given year is a leap year. A leap year have 366 days, with an extra day in February.
A year divisible by 4 with no remmainder, except every year that is divisible by 100 with no remimainder unless the year is also divisible by 400 with no remainder

"""
year = int(input("Please input a year: "))
if (year%4) == 0: 
    if (year%100) == 0:
        if (year%400) ==0:
            print("leap year")
        else: 
            print('Not leap year')
    else:
        print('leap year')
else: 
    print('Its not a leap year')

