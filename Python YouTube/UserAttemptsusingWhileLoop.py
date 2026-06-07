# This program is about to user authentication for password

max_attempts = 3
correct_password = "password123"
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter your password: ")
    if user_input == correct_password:
        print("Login Successful")
    else:
        attempts +=1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. {remaining} attempts remaining")
else:
    print("Too many failed attempts. Account locked")