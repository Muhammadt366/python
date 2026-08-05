
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


try:
    user_key = int(input("Enter a key to look up: "))

    if user_key in d:
        print(f"The value for key {user_key} is: {d[user_key]}")
    else:
        print("Key not found in the dictionary.")
        
except ValueError:
    print("Please enter a valid integer.")
