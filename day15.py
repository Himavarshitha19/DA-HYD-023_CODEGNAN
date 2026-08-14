'''
Sequences--->Strings,Lists,Tuples,Set,Frozenset
Mapping-->Dictionary
'''

#1.Sets--->A Set is a unique Collectionof objects,Unordered,Mutable,
#Hashing,Unindexed(),Unique,Heterogenous
#set(),{}
#a = {} its an empty dictionary
'''
a = set()
print(type(a))
stud_ids = {123,345,234,564,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])) #TypeError
print(234 in stud_ids)
#print(stud_ids *2)#Set  cannot be repeated
print(stud_ids +sud_ids) #Two sets cannot be Merged
'''

#2.Methods/functions of a set
#and also we cannot give set inside a set
'''
data = {12,3,4,5,[12,3,4],'Ford'}
print(data) #No list inside a Set(hashing technique) Lists are Mutable
print(len(data))
for i in data:
    print(i)
'''

#-->Methods on sets -->add(),update(),remove(),discard(),pop()
#add will insert an element into the set,it can be anywhere
'''
names = {'bmw','hyundai','ferrari','audi'}
print(len(names))
names.add('python')
print(names)

#names.add('varsha','poll')-->pass a error bcoz we should add only single element to the set
#print(names)

names.add(('mustang','italy')) #passing a tuple
print(names)
'''

#-->update()
'''
names = {'bmw','hyundai','ferrari','audi'}
da_names = {'abc','cde','fgh','ijk'}
names.update(da_names)
print(names)
print(da_names)
print(len(names))
print(len(da_names))

da_names.update(names)
print(names)
print(da_names)
print(len(names))
print(len(da_names))
'''

#remove(),discard(),pop(),clear()
#remove() removes an element from the set(it must be a member)
'''
da_names = {abc','cde','fgh','ijk'}
da_names.remove('fgh')
print(da_names)
#da_names.remove('fgh') #KeyError-bcoz we already removed that element
'''
#-->discard()
#will remove an element if its present else it ignores
'''
da_names.discard('fgh')
print(da_names)
'''

#-->pop()
da_names = {'joshna','hima','varsha','latha'}
da_names.pop()
print(da_names)
print(da_names.pop())#removes and returns an arbritrary element
#-->clear()
da_names = {'joshna','hima','varsha','latha'}
da_names.clear()
print(da_names)

da_names.add('varsha')#we should pass only single element in this we cannot pass[]
print(da_names)
print(len(da_names))

#-->copy() #creates a shallow copy of set(independent of each other)
da_names = {'joshna','hima','varsha','latha'}
d = da_names.copy()
print(d)
d.update({'python','analytics'})
print(da_names)
'''
#mathematical operations-->union(),intersection(),difference(),symmetric
#issubset(),issuperset(),isadjoint()

da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
#event = da_23.union(da_24) 
event =da_23 | da_24  # | union()
print(event)
print(len(event))
#common = da_23.intersection(da_24)
common = da_23 & (da_24)  # & intersection()
print(common)
print(len(common))
common = da_23.intersection_update(da_24)
print(common) #it retuns None
print(da_23) #common elements are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and prints rmmng elements from first set
diff = da_23.difference(da_24)
print(diff)
f = da_23 - da_24
print(f)
#symmetric_difference()-->removes common elements and prints all rmng
#elements from two sets

symm = da_23.symmetric_difference(da_24)
print(symm)
h = da_23^da_24
print(h)

#issubset()-->checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))

#Length of Unique student ids in a class, where user can enter first input
#he should be giving number
'''
