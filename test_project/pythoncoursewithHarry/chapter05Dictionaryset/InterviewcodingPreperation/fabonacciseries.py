# Python program to print Fibonacci series
# program in using Iterative methods
first,second = 0,1
n = int(input("Please given a number for fabonacci series:"))
print("fibonacci series are:")
for i in range(0,n):
    if i<=1:
        result=i
    else:
        result = first+second
        first = second
        second = result
    print(result)
