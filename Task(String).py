#Task 1-->observe +ve +ve,-ve -ve, +ve -ve,-ve +ve all possibilities

name='Engineer'
#1.(+ve +ve) 
print(len(name))
print(name[0:6]) 
print(name[2:5]) 
print(name[1:6]) 
print(name[4:8]) 
print(name[0:9]) 

#2.(-ve -ve) 
print(name[-5:-1]) 
print(name[-8:-3]) 
print(name[-4:-2]) 
print(name[-5:-1]) 
print(name[-9:-3]) 

#3.(+ve -ve) 
print(name[1:-3]) 
print(name[1:-2]) 
print(name[2:-5]) 
print(name[4:-1]) 
print(name[0:-4]) 

#(-ve +ve) 
print(name[-4:7]) 
print(name[-5:8]) 
print(name[-9:5]) 
print(name[-4:6]) 
print(name[-3:8])


#Task: A B C D E F G H I J K L M O P Q R S T U V W X Y Z
#use loops and strings to return A to Z

for i in range(65,91): #65 is starting number, 91 is ending number
    print(chr(i),end=' ')
