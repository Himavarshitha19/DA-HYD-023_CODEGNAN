
#1.Strings----->Group of characters,we use single or double or triple quotes
#for representation of strings.....
#Strings are Immutable,Ordered,Indexed Collection
#In python space is also character

name = 'Varshitha'
print(name)
print(type(name))
print(len(name)) #len--->returns the number of items in container
#--->index()-->fetch the object (position)starts at 0 and ends at len(obj)
#where we use [] representation
print(name[0])
print(name[5])
#print(name[25]) # IndexError --->as its out of range
#--->Negative Indexing --> -1 to len(obj)
print(name[-1]) #it returns last character
print(name[-3])

#2.Slicing-->We can access group of characters(objects)
#we use [start:end]
#start default-->0, start is included,end is excluded

name = 'codegnan'
print(name[:]) #returns entire string
print(name[0:]) #returns entire string
print(name[:4])  #stsrts at 0th index before 4th index
print(name[1:5])
print(name[:3])
print(name[2:4])
print(name[5:])
name = 'Python'
print(name[3:7])
print(name[7:3]) #returns empty as strings are immutable
#slicing is applicable for lower index to higher index
print(name[:45])
print(name[45:])

#---->Negative indexing
name = 'Analytics'
print(name[-1:-5])
print(name[-5:-1])#starts at -5 and ends at -2
#print cs in both postive and negative
print(name[7:])
print(name[-2:])

name = 'Tokens'
print(name[1:-2])
print(name[2:-6]) #returns empty string

#3.striding----> [start:end:step]

course = 'DataAnalysis'
print(len(course))
#Data ---->result
print(course[:4])
print(course[4:])
print(course[-3])
print(course[::1] #returns all characters
print(course[::2]) #includes start to end skipping1 character
print(course[1:6:3]) #[1:6]--->ataAn--->[1:6:3]---->aA
print(course[2::3])
print(course[::-1]) #it returns the reverse of a string
print(course[::-2]) #it skips the character

#Task: Workout with all possibilites of slicing and striding on a example

name = 'Report'
#name[3] = 'w' #Strings are immutable
      

#4.Operations on strings---->Indexing,Concatenation,Repetition
print(name * 3)
print('*' * 25) #repetition
#----->Concatenation --> combining strings
data = 'Hima' + 'python' + ' ' + 'database'
print(data)
print('123' * 4) #Numeric String
print('code' in 'codegnan')
#in the below case we get every character line by line
for i in 'codegnan':
    print(i,':')
#in above case we get every character line by line
for i in 'codegnan':
    print(i,end=' ')


#5.Built-in functions --->len(),max(),sorted()
name = 'dataCodegnan'
print(len(name))
print(min(name)) #alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(chr(90))
print(max(name))
print(sorted(name)) #returns a list by sorting all elements


#6.Methods on Strings --> Case-Conversions, Finding/Searching.....
name = 'Power BI'
#Case-conversions-->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)
#---->Capitalize()--> converts first letter to uppercase
c = name.capitalize()
print(c)
d = name.title() #converts every work first letter to uppercase
print(d)
      

#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#use loops and strings to return A - Z




















