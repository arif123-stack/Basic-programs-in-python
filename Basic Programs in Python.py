#Addition of two number:
num1 = input("enter a number")
num2 = input("enter a number")
sum = int(num1)+int(num2)
print("the addition of two number is {0}".format(sum))


#check maximum between two number:
a=int(input("enter a number"))
b=int(input("enter a number"))
if(a>=b):
    print(" a is maximum {0}".format(a))
else:
    print(" b is maximum {1}".format(b))


#factorial number:
num=int(input("enter the number"))
fact=1
i=1
for i in range(1,num+1):
    fact=fact*i
print("factorials is",fact)

#find simple interest:
p = int(input("enter the principle amount"))
t = int(input("enter the time"))
r = int(input("enter the rate"))
simpleinterest=(p*t*r)/100
print("the simple interest is ", simpleinterest)

#check whether the number is armstrong number or not:
n=int(input("enter a number"))
sum=0
i=1
copy_n=n
order=len(str(n))
for i in range(1,n+1):
    digit=n%10
    sum=sum+digit**order
    n=n//10
if(sum==copy_n):
    print(" it is Armstrong number",copy_n)
else:
    print(" it is not a Armstrong number",copy_n)
    

#check whether a number is prime or not:
n=int(input("enter a number"))
count=0
i=1
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime number")
else:
    print("not a prime number")

# Program to generate a random number between 0 and 9
# importing the random module
import random

print(random.randint(0,9))

# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))





