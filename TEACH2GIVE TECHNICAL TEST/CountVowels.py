"""
Question 6: Count Vowels
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
"""
sentence=input("Enter a sentence : ")
sentence_lower=sentence.lower()
vowels="aeiou"
count=0
for i in sentence_lower:
    if i in vowels:
        count+=1
print("number of vowels are : ",count)