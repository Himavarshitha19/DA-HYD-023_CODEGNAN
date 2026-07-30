
Tokens -->Variables,Punctuators
Variables --->Name memory location, its a placeholder for data
#Rules are to be followed

#MultiAssignment of Variables

name,age,place = 'Codegnan','7','Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b = 2,4,5 #ValueError as too many values to unpack
#reassigning variables

name = "Codegnan"
a,b = 45,1.5 
print(a,b)
a,b = b,a #swapping
print(a,b,sep=',')

a,b = c,b #NameError as c is not defined
print(a,b)

#Deleting the variables --->del
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators --->[],{},()
name="Codegnan";age = 7;course = 'Data_Analysis'
print(name,age,course)

#Datatypes --->Numeric ,Sequences

#Numeric type--->int,float,complex
#int dattype--> quantity,age...

age = 7
print(age)
print(type(age)) #type ---> returns the datatype of object

print(type(234))

#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --->temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex --->combination of real and imag

i2 = 4
data = 5+i2
print(data)

data = 5+2j #j is representation
print(data)
print(type(data))

#Boolean --->True / Flase

valid = True
print(type(valid))

error = False
print(type(error))

#TypeCasting --->Converting one type to another type
#Python by default follows Implicit Type(we need not mention the datatype)

#we will go for Explict Conversion

#Every built-in datatype is a built-in function
#int,float,bool,commplex

#TypeCating --->int--->float,complex,bool

age = 45
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) # returns True for existing data
print(d)
e = bool(age)
print(e)

#Float --> typecasting --->int ,complex,bool
price = 70.56
print(type(price))
d = int(price)
print(d)
print(type(price))
e = complex(price)
print(e)
print(type(e))
f = bool(price)
print(f)

#complex --->TypeCasting ---->int,float,bool
data = 2+5j
print(type(data))
#b = int(data) #TypeError
#print(data)
#c= float(data)
#print(c)
d=bool(data)
print(d)
print(type(d))

e = int(float(bool(45)))
print(e)

f = 45 + 2.5 + 2 + 3j +False
print(f)




























































































