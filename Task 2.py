#Grade Checker
marks = int(input("Enter a marks:"))
if marks < 0 or marks > 100:
    print("Invaild marks entered")
elif marks >= 90 and marks <= 100:
    print("Grade A")
    print("Remark: Outstanding!")
elif marks >= 80and marks <= 89:
    print("Grade B ")
    print("Remark: Excellent!")
elif marks >= 70 and marks <= 79:
    print("Grade C")
    print("Remark: Good")
elif marks >= 60 and marks <= 69:
    print("Grade D")
    print("Remark: Fair, needs improvement")
elif marks >= 50 and marks <= 59:
    print("Grade E")
    print("Remark: Poor, needs serious improvement")
else:
    print("Grade F")
    print("Remark: Failed, needs to reappear")

#Even-odd Checker
    num = int(input("Enter a number: "))
if num == 0:
    print("Zero is neither even nor odd")
elif num < 0:
    if num % 2 == 0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")
else:
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

#Season checker
month = int(input("Enter month number:"))
if month == 12 or month == 1 or month == 2:
    print("Season: Winter")
elif month == 3 or month == 4 or month == 6:
    print("Season: Spring")
elif month == 6 or month == 7 or month == 8:
    print("Season: Summer")
elif month == 9 or month == 10 or month == 11:
    print("Season: Autumn")
else:
    print("Invalid month entered")



print("done")



















        
