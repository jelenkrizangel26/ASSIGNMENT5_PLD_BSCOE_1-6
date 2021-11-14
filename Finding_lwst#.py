# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

print("Hi! I am Krizzy and I will help you to find the lowest number that you have. Just please give the things that will ask. Thank you")

your_1stNO = float(input("Please enter your first number: "))
your_2ndNO = float(input("Please enter your second number: "))
your_3rdNO = float(input("Please enter your third number: "))

name1 = input("Please put the name of 1st number owner: ")
name2 = input("Please put the name of 2st number owner: ")
name3 = input("Please put the name of 3rd number owner: ")

def display_nmbr(Amnt1, Amnt2, Amnt3):
    if Amnt1 < Amnt2 and Amnt1 < Amnt3:
        return Amnt1
    elif Amnt2 < Amnt1 and Amnt2 < Amnt3:
        return Amnt2
    elif Amnt3 < Amnt1 and Amnt3 < Amnt2:
        return Amnt3

def display_names(naMe1, naMe2, naMe3):
    if naMe1 <= name1:
        return naMe1
    elif naMe2 <= name2:
        return naMe2
    elif naMe2 <= name3:
        return naMe3

lowest_nmbr = display_nmbr(Amnt1 = your_1stNO, Amnt2 = your_2ndNO, Amnt3 = your_3rdNO)
names = display_names(naMe1 = name1 , naMe2 = name2, naMe3 = name3)

def display_own(own1, own2, own3):
    if own1 <= name1  <= your_1stNO:
        return own1
    if own2 <= name2 <= your_2ndNO:
        return own2
    if own3 <= name3 <= your_3rdNO:
        return own2

owner = display_own(own1 = name1, own2 = name2, own3 = name3)

print(f"{owner} has the lowest input number which is {lowest_nmbr}.")
