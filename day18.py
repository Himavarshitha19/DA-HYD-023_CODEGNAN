'''
functions-->variable length arguments(*args)
        -->keyword variable length arguments(**kwargs)
'''
#1.variable length arguments-->the number of positional arguments are not limit
#we can pass any number of arguments,but we need to use the * representation,
#data is stored in tuple
'''
def sample(*args): #by * we can pass any positional arguments
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,5,6) #any number
sample('Engineer','varsha',21)
details=[24,45,35,65] 
sample(details) #passing a collection
sample(*details) #unpacking values from collection
'''
#--->another example for variable length arguments by using variables
#'*' is used for unpacking the values into a collection
'''
a,b,c=13,4,'da'
print(a,b,c)

#in this i gave * to the variable b so codegnan and the numeric values stored in b in the form of list
a,*b,c='python','engineer',23,45,6.7,'data'
print(a)
print(b)
print(c)

#in this i gave * to the variable c , so the numberic values and data is stored in c in the form of list
a,b,*c='python','engineer',23,45,6.7,'data'
print(a)
print(b)
print(c)

#in this we given * to c
#first in c there is no value so it passed empty list
#next i had given extend to c and passed some values and printed, so the values will be printed in c
a,b,*c=34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)
'''

#Task-->we wanted to calculate the sum of given objects using function
'''
ef add(*a):
    """"Sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result = 0
    for i in a:
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float,complex):
            #print(i)
            result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4,5.6))
#add(3,4,5,'poll','dear',4.5)hence its the breaks the sum since it contines strings
#print(add(3,4,5,5.5,2+4j,56.'code',23))
print(add(3,4,5,'poll','dear',4.5))
b = list(map(int,input("Enter the values:").split(',')))
#print(add(*b))#here  '*' is used to unpack the values from collection
print(b)
print(*b)#it returns each value sde by side
for i in b:
    print(i,end='') #it does the same process here as the "*" do
'''

#2.Keyword variable length arguments-->we can pass any number of keyword arguments
#as we use ** representation
#kwargs-->keyword variable length arguments
#the data is stored in dictionary
'''
def details(**kwargs):
    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details() #return empty dictionary
#details(2,3,4,5)-->wrong representation
details(name='engineer',place='hyd',batch='da')

batch={'number':'da23','place':'hyd'}
details(**batch)
'''

#--->now let us include both of them into a function(above example)
'''
def sample(*a,**b):
    """usage of both varibale length and keyword variable length args"""
    result=0
    for i in a:
        if type(i) in (int,float,complex):
            result=result+i
    print(result)
    for key,value in b.items():
        print(f'key is : {key}')
        print(f'Value is : {value}')
sample(2,4,5,'police','engineer',3.5,
              name='engineer',
              place='hyd',
              batch='da23')
'''
