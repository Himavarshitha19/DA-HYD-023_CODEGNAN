'''
#Test Case Converter
text = input('Enter the text:')
print('Lower:',text.lower())
print('Upper:',text.upper())
print('Swapcase:',text.swapcase())
print('Title:',text.title())
print('Capitalize:',text.capitalize())
case = 'isupper(), islower(), istitle()'
if text.isupper():
    print('Uppercse')
elif text.islower():
    print('lowercase')
elif text.istitle():
    print('Textcase')
else:
    print('Mixedcase')

#username validator
name = 'pagani'
if name != " ":
    if name.isalnum():
        print("Letters and numbers only")
    if name[0].isalpha():
        print("Starts with a letter")
    if name.isidentifier():
        print("Valid Python variable name")
    if name.isascii():
        print("ASCII characters only")
else:
    print("Username cannot be empty")    
'''
#Formatted student report

print("Student report")
for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"
    print(name.ljust(10), str(marks).rjust(5), grade.rjust(5))

#character and Text analyzer
















    
