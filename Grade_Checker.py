# 1. Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : “A”
# 80–89 : “B”
# 70–79 : “C”
# 60–69 : “D”
# Below 60 : “F”
# Use a basic if / else statement to determine the grade.


score = float(input("Enter the score: "))       # Student enter the score

if score<=0 or score>100:                       # check if the score is valid or not
    print("Enter valid score")
elif score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
elif score>=60:
    print("Grade D")
else:
    print("Grade F")