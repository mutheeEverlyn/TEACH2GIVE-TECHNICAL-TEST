"""
question 3:Power of Two
write a program that takes an integer as input and returns true if the input is a power of two
Examples: 
8=> returns true
6=> returns false
"""

number=int(input("enter an integer number: "))
if number>0 and (number &(number-1))==0 :
    print("true")
else:
    print("false")