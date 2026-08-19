'''
Functions-->Variable length arguments(*args)
         -->Keyword Variable length arguments(**kwargs)
#Variable length arguments-->The number of positional arguments are not limit
#we can pass any number of positional arguments,but we need to use the *representation,
#data is stored in tuple.
'''
'''
def sample(*args):
    """Simple demo for args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,5,6) #any arguments
sample('Engineer','Varsha',23)
details = [24,45,35,65]
sample(details) #passing a collection
sample(*details) #unpacking values from collection

a,b,c = 13,4,'da'
print(a,b,c)
#a,*b,c = 'python','Engineer',23,45,9.7,'data'
#a,b,*c = 'python','Engineer',23,45,9.7,'data'
a,b,*c = 34,'analytics'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)
'''


#Task-->We wanted to calculate the sum of given objects using Function

def add(*a):
    """Sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result  = 0
    for i in a:
        print(i)
        #if type(i) == int or type(i)== float :
        if type(i) in (int,float,complex):
           # print(i)
         result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(3,4,5,'poll','dear',45,4.5))

#if user want in dynamic then
#b= list(map(int,input("Enter the values").split(',')))
#print(add(*b)) # * is used to unpack the values from collection 
#print(b)
#print(*b) #it returns each value side by side
#for i in b:
#    print(i,end=' ') #same as here
'''

'''
#Keyword variable length arguments--> we can pass any number of keyword
#arguments we use ** representation ,data is stored in dictionary
'''   
def detaiils(**kwargs):
    """Usage of**kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details() #returns empty dictionary
#details(2,3,4,6) #raises TypeError
details(name='Engineer',place='hyd',batch='da')
batch = {'number':'da23','place':'hyd'}
details(**batch)
'''
 
#--->Now let us include both of them into a function
'''
def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result = result + i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
sample(2,4,5,'police','engineer',3.5,
       name = 'engineer',
       place = 'hyd',
       batch='da26')
'''
        














