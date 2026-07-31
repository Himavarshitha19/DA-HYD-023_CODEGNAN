
Identity Operators ---->Checks the identity of an object ---->id()
#is, is not

a = 5
b = a
print(id(a))


print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)

a = [1,3,5.7]
b = a
print(id(a))
print(id(b))
c = [1,3,5,7]
print(id(c))
#As we have Lists (Mutable collection) both c and a lists will be differernt
#ids whereas values are same
print(c is a) #output False
print(c == a) #output True
print(a is not c)
 
#Bitwise Operators --->we perform bitwise operations over operands
#&(and) , | (or), ^(XOR) , shifting operators(<<,>>)
#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5/3) #bitwise OR

print(5^3) #bitwise XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns 5 in above case

print(5 or 3) #returns 3 in this case

#Leftshift Operator << , Rightshift Operator >>

print(5<1) #Flase Comparision
print(5<<1)
print(5>>1)

print(15<<2) #convert 15 to binary and perform 2 times left shifting

print(15>>2) #same 2 times right shifting

#Input Formmatting --->input(), int(input()), float(input())
#you know -->single input
#2 or 3 inputs --->map()
#group of integers --->list(map(int,input().split(','))

names = input('Enter the names:').split(',')
print(names)

name1,name2 = map(str,input('Enter the Friends Names:').split(','))
print(name1,name2)

                 
#Conditional Statements---->if usage

syntax:
if<condition>:
    statement(s)......
    .....

#age = 15
age = int(input('Enter the age:'))
if age >=18:
    print('Your age is:',age)

age = int(input('Enter the age: '))
if age>=18 and age in [19,20,25]:
    print('Your Age is',age)
print(age)


#else keyword--->if else

else:
    statement(s)...

if-else usage as below:

if <condition>:
    statement(s)...
    .....
else:
    statemment(s)....
    ...
      

#Vote Eligibility--->To check his/her voter eligibility and give access

age = int(input('Enter the age:'))

if age>=18:
    print('You have Voter eligibility and age is ',age)
    print('Access Granted')
else:
    age = 18-age
    #print('You dont have eligibility as your age is',age,'years')
    print('You need to wait for more',age, 'years' )

#Same case let's use only nested---->if,else     

if age>0:
   if age>=18:
       print('You have Voter eligibility and age is ',age)
       print('Access Granted')
   else:
      age = 18-age
      #print('You dont have eligibility as your age is',age,'years')
      print('You need to wait for more',age, 'years' )
else:
    print('You  have entered -ve values/zero enter only +ve')





