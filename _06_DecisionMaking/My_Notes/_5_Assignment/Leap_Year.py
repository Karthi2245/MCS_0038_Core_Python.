
year = int(input("Enter a Year"))
if year % 4 == 0:

    if year % 100 == 0:

        if year % 400 == 0:
            print("The given number is Leap Year")
        else:
            print("The Given year is not a leap year")
    else:
        print("The Given year is a Leap year")
else:
    print("The Given Year is not a Leap Year")


