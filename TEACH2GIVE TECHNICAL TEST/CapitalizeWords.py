"""
Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string.
Examples: 
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming"
"""
string=input("enter a string of words")
capitalized_string=string.title()
print("the new string is: ",capitalized_string)
