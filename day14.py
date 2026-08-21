'''
List ,Tuples...
'''
#List--->Mutable,Ordered,Hetergenous
#index(),count(),copy(),sort(),reverse()

#--->index()
'''
details = ['codegnan',7,2018,'Hyderabad']
print(len(details))
print(details.index(7))
print(details.index('Codegnan'))
details.extend[7,21,445,21]
print(details.index(21))
print(details.index(21,6))
#print(details.index('python')) #ValueError
'''
#--->count()
'''
print(details.count(21))
print(details.count('python'))

#--->yesterday task
data = ['codegnan','saketh','python','java']

for obj in data:
    print(data.index(obj),':',obj)
    
#another way-->           
for obj in range(len(data)):
    print(obj,':',data[obj])
'''
   
#--->copy()-->it creates shallow copy of the given collection

'''
new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'Agentic AI'
print(new)
print(data)

data.append('Porsche')
print(data)
print(new)
'''
#nestedlist
#copy in nested list doesnot work
#whenever we make changes in nested list original will
#also be effected
'''
data = [1,4,5,[21,34,45],65]
print(data)
new = data.copy()
print(new)

new[3][2]='Agents'
print(new)
print(data)

new[1] = 'Python'
print(new)
print(data)
'''

#Sorting
'''
marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort()) #returns None
print(marks) #returns in ascending order
marks.sort(reverse=True)#returns in descending order....
print(marks)
marks.insert(2,'code')

#we cannot compare string and integer--sort is not possible
marks=['codegnan','varsha','python','java',21]
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
'''

#-->reverse()--->returns in reverse order
'''
marks.reverse()
print(marks)
print(marks[::-1])
'''
'''
#type(),len(),max(),min(),print()

#Built-in function--->sorted
#sorted can be appilcable on anything like(list,string,tuple...)
print(sorted('Hennesy'))#returns list in asending order
#print(sorted(['code',23,34,45])) #raise error
      
'''
#Tuples--->Tuples are Indexed,Ordered,Heterogenous,Immutable collection
#dimensions,coordinates,database records,we prefer() for tuple notation
#we cannot combine tuple and list it raises an error
'''
a = ()
print(type(a))
print(len(a))

dim = 1.5,2.5
print(dim)
print(type(dim))
print(len(dim))
'''
#Operations--->Indexing,Slicing,Striding,Membeship,Merging,Repetition
'''
courses = ('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses)
print(len(courses))

print(courses[-2][-2:])
print(courses[-2][:-2]) 

courses[-1].append('') #we can make any modifications inside list
print(courses)


print('PFS' in courses) #Membership
d = courses *2 #repetition
print(d)
e = courses + (2,3,4,5)#merging
print(e)
'''
#Tuples are immutable so they are only 2 things to do
#-->count(),index()
#count--no of occurances,-->index---position
'''
courses=('PFS','JFS',('DA','DS'),'AgenticAI',[100,6,6])
print(courses.index('AgenticAI'))#returns first occurance
print(courses.count('Agents'))

print(courses.sort()) #AttributeError--->sort() is in Lists not in tuples

print(sorted(courses[-1]))
print(sorted(courses))#it raises an error as we have mixed type

#Typecasting
d = tuple(sorted((23,12,3,4,5)))
print(d)
'''

#--->accept group of integers space separated
'''
a,b = map(int,input("Enter the values").split())
print(a,b)

a = tuple(map(int,input("Enter the values").split(',')))
print(a)
'''
#--->eval()

'''
print(9+4)#it returns 9+4 bcoz it is in the string format
#eval() function can take any kind of input
print(eval('9+4'))

a = eval(input('Enter list:'))#in this case u can exactly enter the data as
print(a)
print(type(a))
'''


#Task 1-->create a nested tuple as above and work on slicing,striding,and list functions


#Task 2--> take a user input as string, do this is two ways:
'''
1) give the count of each of each repeating character
test case 1: programming
r is repeating 2 times
g is repeating 2 times
m is repeating 2 times

2) r is repeating 2 times
index=[1,4]
g is repeating 2 times
index=[3,10]
m is repeating 2 times
index=[6,7]
'''
