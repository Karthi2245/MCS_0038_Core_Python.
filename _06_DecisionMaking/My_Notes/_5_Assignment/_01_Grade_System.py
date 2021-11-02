
# Grade System:
marks = int(input("Enter the marks? "))
if marks >= 80:
    print("Congrats ! you scored grade A+...")
elif marks > 60 and marks < 80:
    print("You scored grade A ...")
elif marks >50 and marks <= 60:
    print("You scored grade B ...")
elif marks >= 40 and marks <= 50:
    print("You scored grade C ...")
elif marks >= 35:
    print(" You are Just Pass")
else:
    print("Sorry you are fail ?")
