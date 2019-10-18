username = input("enter your user name: ")
password = input("enter your password: ")
hidden_password = len(password)*"*"
print(f"hi {username}, your password ({hidden_password}) is of leangth {len(password)}")