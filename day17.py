'''
#Functions-->a function is a block of code which performs a specific task
#Its a reusable group of statements where we define using
#def keyword
#Advantages--->Code reusability ,code maintainabiility ,ease of debugging,
#avodining code duplication,modularity

syntax-->
def fname(parameters):   #function definition
    """Doc String"""     #description function
    statement(s)....     #function body
    ...........
    return value(s)....
fname(args)     #function call
'''
#To perform sum of given objects
'''
def add(a,b):
    """Sum of objects"""
    c=a+b
    return c
print(add(12,16)) #Addition
print(add('Rolls','Royce')) #Concatenation
print(add([12,5],[13,6]))  #Merging

c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

#without return
def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('rolls','royce')
print(add(12,-34)) #it returns result along with None


name,age,salary = 'cbvdhc',20,700000
#usage of return
def details():
    return name,age,salary
print(details())


#There are 5 types of arguments:
-->Positional Arguments
-->Default Arguments
-->Keyword Arguments
-->Variable length arguments(*args)
-->keyword variable length arguments(**kwargs)
'''

#Positional Arguments--> Nuber of arguments in function defn should
#match with function call (order has to be maintained)
#print(len(123,234)) this is as per built-in len(obj) will accept one argument
'''
def details(name,place):
    """To store the details"""
    name = "Ananlytics"
    place = "Hyderabad"
    return name,place
print(details('lexus','India'))
print(details('ferrari','italy'))


def details(name,place):
    """To store the details"""
    #name = "Ananlytics"
    #place = "Hyderabad"
    #return name,place
    print(f'Name is {name}')
    print(f'place is {place}')
#print(details('lexus','India'))
#print(details('ferrari','italy'))
#print(details('vizag',34,'shyam'))-->it raises TypeError as only 2 arguments to be given
c,d=map(str,input('Enter the values:').split(','))
details(c,d)
'''
#Default arguments-->we can make arguments as default but not first argumnet
#as default
'''
#-->1st case--second parameter is default
def grocery(item,price):
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)

#-->2nd case-- two parameters default
def grocery(item,price=35):
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
grocery('bread') #by default we had given price as 35

 
#-->3rd caluse--first parameter is default
def grocery(item='Cheese',price=100):
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
grocery('bread')
grocery()


#-->fourth case
def grocery(item='Burger',price): #non default is always follows default
    """Usage of default arguments"""
    print(f'The Item is : {item} and Price is : {price}')
grocery('Milk',32)
grocery('bread')
'''
            
#Keyword arguments --->whenever we want to specify the name of argument
'''
def employee(name,salary,role,place = 'Hyderabad'):
    """Keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary},\
           works in [place})
employee("sai",20000,"Admin")
employee(salary=800000,role='Frontdesk',name='varsha')
employee("hima",800000,'IT','Cognizant')

