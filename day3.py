#input formatting --->Accepting input from the user --->input()
#Accepting integer input from user
#by default input() accepts any input -->str
#int(input()) --->will accept only integers
'''
age  = int(input('Enter the age: '))
print(age)
print(type(age))

#float(input()) ---->accepts integers, float values
age = float(input('Enter the age: '))
print(age)
print(type(age))

#Accepting string input from user
name = input('Enter the name: ')
print(name)
print(type(name))

#marks = int(input('Enter the marks: ')).split()
print(marks)

a = input().split()#by default split() has space
print(a)

#space separated values
a = input(). split() #now you enter spaces in output
print(a)
#comma separated values
a = input('Enter the values:').split(',')
print(a)

#List of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)

#Now we want to accept 2 values from user
age,salary = map(int,input('Enter the values').split(','))
print(age)
print(salary)

#Single input ---->int(input())
#two inputs --->a,b = map(int,input().split(','))
#any number result as list --->a = list(map(int,input().split(',')))

#float of integers
age,salary = map(float,input('Enter the values').split(','))
print(age)

#Accepting input from user --->int,float --->input fromatting

#Operators
#Arithmetic Operators ---->arithmetic operations
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3) #Float value
#Floor Division(Integer division) ----->returns quotient
print(5//3)
#Modulus --->divisible rules -->returns remainder
print(5%3)
#Power(exponential)
print(5**3)
'''
#Accept integer input as length ,breadth-->find the area of rectangle
#area = length *breadth
length , breadth = map(int,input('Enter the values:').split(','))
area = length*breadth
print(area)
'''
#Assignment operators--->assign the values
# = , +=, -=
a = 45
print(a)
#update the value of a
a = a+5 #a+=5
print(a)
b = 35
b += a #b =b+a
print(b)
b -= 5 #b = b-5
print(b)

#Task : *=, /=, //=, %=, **= workout

#Comparision Operators---->we compare the values --->boolean
# == , != , < , > , <= , >=
age = 25
print(age == 25)# returns Boolean output
print(age != 35)
print(age < 25)
print(age > 25)
print(age <= 25)
print(age >= 25)

print(-5 < -1)

#Membership Operators --->in , not in --->boolean
#it checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)

print(25 not in marks)

#Logical Operators------>and,or,not
#and---->all conditions to be satsified
#or------>any one condition to be satsified

a = (35 in[25,45,65]) and 45<56
print(a)
b = 45>56 or 25<=45
print(b)
c = not(True)
print(c)

#Identity operators---->check for identity of an object---->id()
a= 35
b=35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)

a = [1,3,5,7]
print(id(a))
c = a
print(id(c))
print(c is a)

b = [1,3,5,2,7]
print(id(b))
'''























































