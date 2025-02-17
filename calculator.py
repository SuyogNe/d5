def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print("1. Addition", add(num1,num2))
print("2. Subtraction", sub(num1,num2))
print("3. Multiplication", mul(num1,num2))
print("4. Division", div(num1,num2))