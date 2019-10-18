a = int(input("enter the year"))
if a == 0:
    
    print("this year is not there")

elif a%400 == 0:

    print("this is not a leap year")

elif a%4 == 0:

    print("this is a leap year")

else :

    print("this is not a leap year")    
