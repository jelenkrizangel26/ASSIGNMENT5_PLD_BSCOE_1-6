# Program 1: PUP Grading System
# Section 8 of ThePUPStudentHandbook2014.pdf
# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

import math 
grd_ = float(input("Grade: "))
grd = math.ceil (grd_)

if grd >= 97 and grd <= 100:
    print("Excellent! Your grade is 1.0!")
elif grd >= 94 and grd <= 96:
    print("Excellent! Your grade is 1.25!")
elif grd >= 91 and grd <= 93:
    print("Very Good! Your grade is 1.5!")