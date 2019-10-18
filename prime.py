a = int(input("enter the number"))

half = int(a/2)

if a>1:
    for i in range(2,half):
        if a%i == 0:
   
            print("it is not a prime no")
            break

    else:

        print("it is a prime no")


