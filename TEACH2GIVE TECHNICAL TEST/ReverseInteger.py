"""
Question 5: Reverse Integer
Write a program that takes an integer as input and returns an integer with reversed digit 
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.
"""
number=int(input("enter an integer number: "))
reverseNumber=0
sign=1
if number<0:
     sign=-1
     number =number * -1
      
while number > 0:
      value=number % 10
      reverseNumber=reverseNumber * 10 + value
      number =number // 10

if not -2147483648<reverseNumber<2147483647:
      print(0)
print (sign * reverseNumber)
