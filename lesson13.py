

#name = input ("What's your name? ")
#print("Hello, " + name)
#num1 = input("Enter X: ")
#num2 = input("Enter Y: ")
#sum = int(num1) + int(num2)
#print(sum)


login_attempts = []
password_attempts = []
correct_username = 'egorzolotko'
correct_password = '2001'

while True:
    user_name = input("Please enter Your name: ")

    if user_name.lower() == 'egor':
        print(f"Hello, {user_name}!")
        break
    else:
        print("Incorrect name. Try again.")

while True:
    user_login = input("Please enter Your login: ")
    login_attempts.append(user_login)
    if user_login == correct_username:
        break
    else:
        print("Incorrect login. Try again.")

while True:
    message = input("Please enter Your password: ")
    password_attempts.append(message)
    if message == correct_password:
        break
    print(message + " Your password is not correct.")

print("Password is correct! You needed", len(password_attempts), "attempts.")

if len(password_attempts) > 1:
    print("Incorrect password attempts:")
    for attempt in password_attempts[:-1]:
        print(attempt)

print("\nFinal Result:")
print("Name:", user_name)
print("Your Login:", user_login)
print("Your Password:", message)
print("Login Attempts:", ", ".join(login_attempts))
print("Password Attempts:", ", ".join(password_attempts))
print("Welcome!")
