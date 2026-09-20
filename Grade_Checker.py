# 1. Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : “A”
# 80–89 : “B”
# 70–79 : “C”
# 60–69 : “D”
# Below 60 : “F”
# Use a basic if / else statement to determine the grade.


def addition(a,b,c):
    add = a + b + c
    return add


def multiplication(add):
    multi = add * 100
    return multi

def division(multi):
    dive = multi/300
    return dive

def grade(dive):
    if dive<=0 or dive>100:                       # check if the score is valid or not
        print("Enter valid score")
    elif dive >= 90:
        print("Grade A")
    elif dive>=80:
        print("Grade B")
    elif dive>=70:
        print("Grade C")
    elif dive>=60:
        print("Grade D")
    else:
        return "Grade F"  

math = int(input("Enter the math score: "))
sci = int(input("Enter the science score: "))
eng = int(input("Enter the English score: "))

add = addition(math, sci, eng)
print(f"your total score is {add} out of 300.")

multi = multiplication(add)

dive = int(division(multi))
print(f"you percentage is {dive}")

grade(dive)