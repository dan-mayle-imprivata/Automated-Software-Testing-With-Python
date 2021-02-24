users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longpassword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)

# prints
# {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'bob123'), 'Jose': (2, 'Jose', 'longpassword'), 'username': (3, 'username', '1234')}

print(username_mapping["Bob"])  # (0, 'Bob', 'password')

# For login
username_input: input("Enter your username:")
password_input: input("Enter your password:")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("your details are correct!")
else:
    print("Your details are incorrect.")
