# write a program to reverse number

# n = int(input("enter given a number:"))
# print("before reverse your number is: %d" %n)
# reverse = 0
# while n!=0:
#    reverse = reverse*10 + n%10
#    n = (n//10)
#print("After reverse : %d" %reverse)

# Program to check a number is Armstrong
# or not in python programming language
i = 0
result = 0
n = int(input("please given a number:"))
number1 = n
temp = n
while n!=0:
    n = (n//10)
    i = i+1
while number1!=0:
    n = number1%10
    result = result+pow(n,i)
    number1=number1//10
if temp==result:
    print("number is armstrong")
else:
    print("number is not armstrong")


