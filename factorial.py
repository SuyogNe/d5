def rfact(n):
    if n==1:
        return 1
    else:
        return n * rfact(n-1)

num=int(input("Enter a number: "))

if num<=0:
    print("no existing factorial")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ",num," is ",rfact(num))