
password = input("What is the master password?")


def view():
    pass


def add():
    pass


while True:
    mode = input(
        "Would you like to add a new password or view your existing ones? \nPress q to quit")
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Please choose a valid mode!")
        continue
