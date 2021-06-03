print("You need to create an acccount in order to continue\n")
print("Write an username to your account")
username_db = input()

print("Write a password to your account")
password_db = input()

print("\n\n\n")

print("Now log in into your account")

print("Username ")
username = input()

print("Password")
password = input()

print("\n\n\n")

if username == username_db and password == password_db:
    print("Welcome", username_db)
else:
    print("Access denied")