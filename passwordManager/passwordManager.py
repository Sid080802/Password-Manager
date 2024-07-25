# These function is written for view saved username or password entered by end user
def view_passwords():
    with open("passwords.txt", "r") as f:  # This function read a file created by user
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

# These function is written for Add username or password to stored in passwords.txt file
def add_password():
    name = input("Type username ")
    password = input("Type password ")

    with open("passwords.txt", "a") as f:   # This function create .txt file to store the password
        f.write(name + "|" + password + "\n")



while True:
    # Taking user input
    mode = input("Would you like to add new password or view existing ones (view/add), press Q to Quit: ").lower().strip()
    if mode == "q":
        break

    if mode == "view":
        view_passwords()              # Call the function
    elif mode == "add":
        add_password()               # Call the function
    else:
        print("Invalid mode")