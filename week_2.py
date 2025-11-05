#write a function to check the number is even or odd
def even(n):
    if n%2==0:
        return 0;
    else:
        return 1;
n=int(input("Enter number:"));
if even(n):
    print("odd");
else:
    print("even");
    
#write a function to find factorial of a agiven number
def fact(n):
    if n==1:
        return 1;
    else:
        return n*fact(n-1);
num=int(input("Enter number:"));
print("The factorial of ",num,"is ",fact(num));

#write a function to take number as input and print its square values
def squ(n):
    print("The square of ",n," is ",n*n);
n=int(input("Enter number:"));
squ(n);

#write a python program using functions to perform arithmetic operations
def add(a,b):
    print( a+b);
def sub(a,b):
    print(a-b);
def mul(a,b):
    print(a*b);
def div(a,b):
    print(a/b);
num1=int(input("Enter number1:"));
num2=int(input("Enter number2:"));
print("1.add\n2.sub\n3.mul\n4.div");
ch=int(input("Enter your choice"));
if ch==1:
    add(num1,num2);
elif ch==2:
    sub(num1,num2);
elif ch==3:
    mul(num1,num2);
elif ch==4:
     div(num1,num2);
else:
    prin("Enter valid number to perform operations");
    
    
