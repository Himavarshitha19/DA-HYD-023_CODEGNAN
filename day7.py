
#Usage of else with for --> the else keyword will only be executed when the loop is completely done without any break

work_log = [0,1,1,1,0,1,0]
#result variable ---->longest_streak
longest_streak = 0  #target variable
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0 #streak breaks
else:
    print(f'longest_streak is {longest_streak}')

#In this case when the entire looop execution is done we get result of
#else block    

#same program with break usage

work_log = [0,1,1,1,0,1,0]
#result variable ---->longest_streak
longest_streak = 0  #target variable
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(f'Longest Streak is {longest_streak}')
            break
    else:
        current_streak = 0 #streak breaks
else:
    print(f'longest_streak is {longest_streak}')
print("Execution done")

#for-else with Notifications scenario
notifications = [0,0,0,0]
for notification in notifications:
    if notification == 1:
        print("Unread notification")
        break
else:
    print("All Caught Up!")
    

#try to take notifications fromm user---->list of integers
notification = [0,0,0,0]
notifications = list(map(int,input("Enter the values-->0 or 1:").split(',')))
for notification in notifications:
    if notification == 1:
        print("Unread notification")
        break
else:
    print('All Caught Up')

    
'''
#while--->it relies on Conditio,it will be completely executed until the 
#condition is stasified...

Syntax:
while<condition>:
       statement(s)....
       .....
       ....
while True:
   print("Yes") 
#It runs an infinite loop we need to press Ctrl+C(keyboard interrput)
'''

i = 0 #initalised
while i<=10:
    print(i)
    i=i+1 #counter
     
#Get the counter from 10 to 1
i =10
while i>=1:
    print(i)
    i = i-1 #decrment i-=1

#banking scenario----> PIN authentication if more than 3 attempts
#Account locked.....

pin = '2612'
max_attempts = 3
current_attempts = 0
while current_attempts < max_attempts:
    entered_pin = input('Enter the ATM PIN:')
    if entered_pin ==pin:
        print('Login Successful')
        break
        #continue#it holds for this condition and skips to the next part of 
    else:
        print('Entered PIN is wrong...Try agin carefully')
        current_attempts += 1
else:
    print("Account Locked, try after 24hours....")



