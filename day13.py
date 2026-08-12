'''
sequences-->Strings,lists,tuples,sets
mapping-->Dictionary
'''

#1.Lists--> collection of heterogenous elements(items)
#list-->is indexed,ordered,mutable,heterogeneous,we use [] to store the data

marks=[35,25,21,45]
print(marks)
print(type(marks))
print(len(marks))


#2.operations: indexing,striding,slicing,membership,merging,repetition

#3.Nested Lists--> a list inside another list

names=['Engineer',21,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4]) #it returns code
print(names[0][4:]) #it returns gnan
#get the output as neer
print(names[0][::2])
names[0]=names[0][::-1]
print(names[0])
'''
#---------->
'''
names=['Engineer',21,4.6,[45,35,25,65],'DA23',34]
print(names[3])
print(len(names[3]))
print(names[3][2])
#--->indexing,slicing--->mutable
names[2]='varsha'
print(names)
#by indexing if we change the element, length of collection will remain same
names[3]=['Engineer','PFS','JFS','DA','AAA']
print(names)
print(len(names))
names=['Engineer',21,4.6,[45,35,25,65],'DA23',34]
print(names[4][0][4:])
'''
#--------->
'''
names=['Engineer',21,4.6,[45,35,25,65],'DA23',34]
print(names)
names[2:4]='varsha','hima','buggati','pagani'
print(names)
#in slicing whatever elements u passed as per the logic length keeps on increasing
'''
#----------->
'''
names=['Engineer',21,4.6,[45,35,25,65],'DA23',34]
print(names)
names[2:4]='varsha','hima','buggati','pagani'
print(names)
names[3:6:2]='python','java'
print(names)
'''
#Task-->create a nested list with strings,lists and work on indexing,slicing,striding
#added advantage if u could add string functions also it

#4.List functions-->append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()
'''
names=['Engineer','varsha']
#--->append()-->inserts single element to the end of the list
names.append('data')
print(names)
#names.append('analysis','agents')-->we cannot pass 2 elements in append()
#print(names)
names.append(['analysis','agents'])
print(names)
print(len(names))
#append() will always increment the length of the list by 1
names[3].append('chatgpt')
print(names)
#print(names[3].append('chatgpt'))-->it returns None as append is applicable on list not print
'''

#--->extend()-->it inserts multiple elements to the end of list
#inserts single element to the end of the list
'''
names.extend('data') #string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,56,67,78])
print(names)
'''

#--->insert()-->[index,object]-->inserts given object before index
'''
names=['Engineer', 'varsha', 'data', ['analysis', 'agents']]
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])-->syntax error
names.insert(-1,'AAA')
print(names)
'''

#--->pop(),remove(),clear()-->
#pop() by default last,else given index
'''
names=['Engineer', 'varsha', 'data', ['analysis', 'agents']]
names.pop()
print(names)
names.pop(2)
print(names)

#--->remove()-->we can remove a specific value
names.extend([23,34,67])
print(names)
names.remove(34)
print(names)
#names.remove(34)-->it raised ValueError

#--->del-->del keyword will apply permanent changes
del names[1:3]
print(names)

#--->clear()-->will remove all elements and it returns an empty list
names.clear()
print(names)
'''
'''
'''
Task-->
data=['codegnan','saketh','python','java']
output should be as follows
0 : codegan
1 : saketh
2 : python
3 : java
'''











            
