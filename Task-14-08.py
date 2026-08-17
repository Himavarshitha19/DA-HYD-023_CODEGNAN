
#task 1---->
marks = [int(input(f"Mark {i+1}: ")) for i in range(3)]
marks = [90] + marks + [75, 85]

if 75 in marks: marks.remove(75)

print(f" Original marks:  |Final list: {marks[:-1]} | Popped: {marks[-1]} | Total: {len(marks)-1}")

'''
#task 2--->
nums = [20, 10, 30, 20, 40, 20]

print("Ascending:", sorted(nums), "| Descending:", sorted(nums, reverse=True))

n = int(input("Search number: "))
print(f"Count: {nums.count(n)}, First index: {nums.index(n)}" if n in nums else "Not found")

print(f"Min: {min(nums)}, Max: {max(nums)}, Sum: {sum(nums)}")

#task3---->
numbers = [10, 15, 20, 25, 30, 35]

print("Even numbers:", [n for n in numbers if n % 2 == 0])
print("Odd numbers:", [n for n in numbers if n % 2 != 0])
print("First three:", numbers[:3], "| Last three:", numbers[-3:])

backup, _ = numbers.copy(), numbers.clear()
print("Original:", numbers, "| Backup:", backup)

#task---->4

names=['Asha','Rahul','Asha','John','Rahul']
x=set(names)
print(x)
x.add('Meera')
print(x)
x.update(("Arun","Priya"))
print(x)
if 'John' in x:
    x.remove("John")
print(x)
x.discard('John')
for i in x:
    print(i)

#task---->5
python = {"Asha", "Rahul", "John", "Meera"}
da = {"Rahul", "Meera", "Arun"}

# Set operations using standard operators
print("All students:", python | da)             # Union
print("Both courses:", python & da)             # Intersection
print("Only Python:", python - da)              # Difference
print("Only one course:", python ^ da)          # Symmetric Difference

# Simple boolean checks
print("Is DA inside Python?:", da <= python)    # Subset check
print("No common students?:", python.isdisjoint(da))

# Summary
if common := python & da:
    print(f"Overlap: {common} enrolled in both.")

#task 1
marks=[]
for i in range(3):
    mark=int(input('Enter the mark:'))
    marks.append(mark)
print('Original marks:',marks)
marks.insert(0,90)
print(marks)
marks.extend([75,85])
print(marks)
if 75 in marks:
    marks.remove(75)
remove=marks.pop()
print("Removed value:", remove)
print("Final list:", marks)
print("Length:", len(marks))

'''


















