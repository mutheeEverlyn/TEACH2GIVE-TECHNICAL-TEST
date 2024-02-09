"""
Question 2:Fibonacci sequence
write a program to generate the Fibonacci sequence up to 100
"""
num1=0
num2=1
sum=0
print(num1)
print(num2)

while sum<100:
        sum=num1+num2
        num1=num2
        num2=sum
        print(sum )
        sum +=1