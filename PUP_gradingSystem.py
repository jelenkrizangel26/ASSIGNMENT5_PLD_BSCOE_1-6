# Program 1: PUP Grading System
# Section 8 of ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

grd_ = float(input("Grade: "))
grd = round(grd_)

if grd >= 97 and grd <= 100:
    print("Excellent! Your grade is 1.0!")
elif grd >= 94 and grd <= 96:
    print("Excellent! Your grade is 1.25!")
elif grd >= 91 and grd <= 93:
    print("Very Good! Your grade is 1.5!")

elif grd >= 88 and grd <= 90:
    print("Very Good! Your grade is 1.75!")
elif grd >= 85 and grd <= 87:
    print("Good! Your grade is 2.0!")
elif grd >= 82 and grd <= 84:
    print("Good! Your grade is 2.25!")
elif grd >= 79 and grd <= 81:
    print("Satisfactory! Your grade is 2.50")
elif grd >= 76 and grd <= 78:
    print("Satisfactory! Your grade is 2.75!")
elif grd >= 75:
    print("Passing! Your grade is 3.0")
elif grd >= 65 and grd <= 74:
    print("Failure! Your grade is 5.0 :)")
else:
    print("Your are either Incomplete (Inc), Withdrawn (W), or Dropped (D) ")

print("Your grade is already recorded. Soar high and keep fighting!")