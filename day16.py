'''
Mapping-->Dictionary-->Collection of key-value pairs used to store
related data-->JSON,APIs,database records
dict()-->data = {}-->data={key,value}
dictionary is Mutable,Indexed through keys,Ordered,Heterogeous,
keys must be Unique (int,strings,float values....)
'''
#dictionary
'''
details = {}
print(type(details))

details = {'Id':'CDH476','Name': 'gfhwe',
           'Gender':'F','Age':23,
           'Batch' :'DA23','Place': 'HYD'}
print(details)
print(len(details))

'''
#Access the data from dictionary
#details[0] #KeyError
'''
print(details.keys()) #it returns keys from dictionary
print(details['Id']) ,details['Name']
#if key name is not matching / invalid-->then it raises a keyError
#print(details['marks']) #KeyError as marks is not present

details['marks'] = []
print(details)
print(type(details['marks']))

details['marks'].append(20)
print(details)

details['marks'].extend([15,20,25,20,20])
print(details)
'''

#-->create a key-value pair of Practice Session
'''
details['PS']= ('Tuesday','Thursday','Saturday')
print(details.keys())

#-->Accessing 3rd day marks of student
print(details['marks'][2])

#-->Accessing 2nd day of practice session
print(details['PS'][1])

#-->create a key-value pair of practice session
details['MI'] = ['Monday','Wednesday','Friday']
print(details)
'''

#operations-->mutable,indexing through keys,membership
'''
print('Wednesday' in details)
print('MI' in details)  #returns True as we have MI as key
for i in details:
    print(i) #returns keys one by one

for i in details.keys():
    print(f'Key = {i}')
    print(f'Value = {details[i]}')

#keys()-->returns keys from the dictionary
for i in details.values():#returns value from dictionary
    print(i)

for i in details.items(): #returns a key-value pair in tuple
    print(i)
   
for key,value in details.items():
    print(f'key is {key}')
    print(f'Value is {value}')
'''

#update()---> updating the dictionary with key-value pairs
'''
details.update({'marks':[],
                'PS':('Tuesday','Thursday','Saturday')})
print(details)
details['marks'].extend([25,30,25])
print(details)

#another way
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

print(details.key())
print(details.get('Name'))
print(details.get('Branch')) #it returns None as we dont have branch as key
    
details.setdefault('Branch') #if key is not present it inserts into dict
print(details)
details['Branch'] = 'CSE'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch'))#we need to mention key
print(details.keys())

print(details.popitem()) #removes and return a key,value pair as a 2-tuple
print(details.popitem())

del details['Id']
print(details.keys())

details.clear() #remove all elements from D
print(details)
'''

#fromkeys()--->creates a dictionary from iterable(lists,tuples,sets,string
'''
data=['ducati','zonda','data']
a=dict.fromkeys(data) #creates a dictionary but values set to None
print(a)
a['ducati']=21
print(a)
c=dict.fromkeys(['CDH476','CDH890'],['Ana','lytics'])
print(c)
'''

#Task: create a dictionary with your personal details, similar to your codegnan profile analytics



    
