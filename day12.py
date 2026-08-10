'''
Strings--->CaseConversions,Searching & Finding,String testing methods,
replace,Space removal
'''
#1.Searching, Finding,Replacing,Joining...
'''
a = "Engineer"
print(len(a))
print(min(a))
print(max(a))
'''
#-->Searching-->
'''
b = a.index('i')#it returns the index position
print(b)
c = a.index('n') #it returns only the first occurance
print(c)
d = a.index('n',2) #it returns the next occurance
print(d)
#e = a.index('n',5) #ValueError
#print(e)
#f= a.index('t') #ValueError
#print(f)
g = a.index('n',2,6)
print(g)
'''

#--->rindex--> returns last occurance
'''
b=a.rindex('g')
print(b)
c=a.rindex('n')#here n is occuring at 4th index
print(c)
#d=a.rindex('n',5)#it returns ValueError
#print(d)
'''

#--->count()-->returns the number of items object is repeating
'''
print('Codegnan'.count('n'))
print('code'.count('w')) #it returns 0 as we dont have 'w' in ' code'
print('Cnsijdcfwocnw'.count('c'))
'''


#--->find()-->first occurance but it avoid error returns -1 if substring is
#not found
'''
print('Harley'.find('n')) #it returns -1
print('Ducatii'.find('i'))
'''

#--->example-->
'''
a='Data'
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))
'''

#--->Replacing,Splitting,Joining
#Strings are Immutable
'''
a ='Porsche'
#a[3] = 'b'
a = a.replace('s','b')
print(a)
print('sbjd#woe#ind#nbhd'.replace('#',''))
print(a.replace('x','varsha'))
'''

#--->splitting-->
'''
a = 'code varsha python'
print(len(a))
b= a.split() #by default if we have space it splits(returns list)
print(b)
print(len(b))
c= 'code,varsha,python'
d=c.split()
print(d)
e = c.split(',')
print(e)
'''

#--->join(iterable)--->concatenate any number of strings
'''
a ='hima'
b ='varsha'
print(a.join(b))
print(b.join(a))
print('$'.join('bmw'))
print(' '.join('bmw'))
'''

#2.String testing methods(boolean)
#isalpha(),isalnum(),isdigit(),issupper(),islower().....
'''
a='Pagani123'
print(a.isalnum())#returns True for alphanumeric strings else False
b = 'Pagani'
print(b.isalnum())
print(a.isalnum())#returns True only for aplhabets
print(a.isdigit())#returns True on;y for digit string
print('7617287917'.isdigit())
print('9879'.isnumeric())#this has upper edge(numbers,fractions,romans)
'''

#--->startswith()-->how its start
'''
print('analytics'.startswith('a'))
print('analytics'.startswith('y',4))
print('analytics'.endswith('c'))
print('analytics'.startswith('t',5))     
'''

'''
print('audi'.islower()) #returns True for all lower case
print('AUdi'.islower()) #returns True fro all upper case
print('Audi python'.istitle())
'''

#--->Space removal-->strip()(removes leading and trailing spaces)
'''
a =' numeric '
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''

#--->zfill() filling with zeros as per the given numeric string
'''
print('456'.zfill(4))
print('456'.zfill(7))
'''

#--->center(),ljust(),rjust()-->Alignment of strings(cehck length and then
#modify the width accordingly
'''
print('hello'.center(8))
print('hello'.center(8,'#'))

print('hello'.ljust(8,'#'))
print('hello'.rjust(8,'#'))

'''
