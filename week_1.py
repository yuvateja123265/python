'''
#1.kg to pounds
a=float(input("Enter kg:"))
pounds=a*2.2
print(f"{a} kilograms is equal to {pounds:.2f} pounds")
#print(a*2.2)

#2.Find max number
numbers={10,100,200,3000}
largest=max(numbers)
#print(f"the largest number is {largest} number")
print(largest,"is the largest number")

#2.find max numbers
print("Max of 3 numbers")
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
largest=a if(a>b and a>c) else b if (b>c) else c 
print("Largest=",largest)

#3.prime numbers
print("prime or not")
n=int(input("Enter num:"))
flag=1
for i in range(2,n-1):
      if n%i==0:
          flag=0
          break
if flag==1:
    print(n,"is the prime number")
else:
    print(n,"is not the prime number")


#4.print prime numbers between given range
print("prime numbers between range")
start=int(input("Enter the start of the interval:"))
end=int(input("Enter the end of the interval:"))
print("Prime numbers between",start,"and",end,"are:")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
            
#4.arithmetic operators
print("To perform arithmetic operators")
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
print("Addition:",a+b)        
print("Subtraction:",a-b)    
print("Multiplication:",a*b) 
print("Division:",a/b)        
print("Modulus:",a%b)         
print("Exponentiation:",a**b) 
print("Floor Division:",a//b)

#5.print days
print("print days")
def day(day_number):
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if 1<=day_number<=7:
        return days[day_number]
    else:
        return("Invalid day number")
num=int(input("Enter a valid number:"))
dd=day(num)
print("Day:",dd)
print("Day:",day(num))

#6.odd or even
print("odd or even")
num=int(input("Enter a number:"))
if num%2==0:
        print("number is even")
else:
        print("number is odd")

#7.turple
print("Conacatenating turple")
mem1=("Nikhita",18,"Eluru","aditya university")
mem2=("Vijaya",19,"Dharmavaram","aditya university")
turple=mem1+mem2
print("Conacatenated turple:",turple)

#8.creating a dictionary
print("creating a dicictionary")
student = {"name": "John", "age": 20, "grade": "A"}
print("Name:", student["name"])
student["city"] = "Hyderabad"
student["age"] = 21
del student["grade"]
print("Student Details:", student)

#9.My set
print("Set and operations")
set={1,2,3,4,5,5,7,3}
set.add(6)
print("My set:",set)
set.remove(2)
print("My set:",set)
print(2 in set)
'''
for num in range(8, 101,3):
    print(num,end=' ')
print()
'''
S = "Python" 
C = list(S)
print(C) 

# Get the largest number from a list
numbers = [12, 45, 2, 98, 23, 67, 89]
largest = max(numbers) 
print("The largest number in the list is:", largest)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")
        
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")
car1 = Car("Toyota", "Camry", 2022)
car1.start()
car1.stop()
'''
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

# Example Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()
dog.bark()
cat.eat()
cat.meow()

'''
try: 
    num1=int(input("enter num1:"))
    num2=int(input("enter num2:"))
    result=num1/num2 
    print(f"result:{result}")
except ZeroDivisionError: 
    print("Error : Cannot divide by zero!")
except ValueError: 
    print("Error : Please enter valid integers!")


#1.kg to pounds
a=float(input("Enter kg:"))
pounds=a*2.2
print(f"{a} kilograms is equal to {pounds:.2f} pounds")

# 2.Program to split a string into array of characters
text = input("Enter a string: ")
chars = list(text)  
print(chars,"Array of characters:")

# 3.Sample list (you can also take input from user)
numbers = [12, 45, 7, 89, 34, 23]
largest = max(numbers)  
print("The largest number in the list is:", largest) 


n = int(input("Enter the number of elements: "))
numbers = []  
# Input numbers one by one
for i in range(n):  
    num = int(input(f"Enter number {i+1}: "))  
    numbers.append(num)  
  
# Find the largest number manually 
largest = numbers[0]
for j in numbers:
    if j > largest:         
        largest = j
print("The largest number in the list is:", largest)  

'''











 
    
      
