
#passing the number using while loop
secret = 123
guess=int(input("Enter the number:"))
while guess != secret:
    if guess<secret:
        print("too low")
    else:
        print("too high")
    guess = int(input("Enter the number:"))
print("correct guess")

#OTP Verification
OTP = "4321"
max_attempts=7
current_attempt=0
while current_attempt<max_attempts:
    entered_OTP=input('Enter the OTP:')
    if entered_OTP==OTP:
        print('OTP is Successful')
    else:
        print('Entered Otp is invaild')
        current_attempt+=1
else:
    print('Account locked, try after 24 hours..')

#Food order system
food = input("Enter the order:")
count = 0
while food != "EXIT":
    count += 1
    food = input()
    order = input("Enter the order:")

print("Total no of items ordered",count)

secret = "python"
current = 0
max_attempts = 3
while current<max_attempts:
    a = input("Enter the secret:")
    if (a==secret):
        print("access again")
        break
    else:
        remaining = max_attempts-current
        print(f"wrong guess")
        current += 1
else:
    print("chances over")
























    
                     
        

