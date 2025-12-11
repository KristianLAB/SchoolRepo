import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def load_users():
    
    users = []
    if not os.path.exists(CREDENTIALS_FILE):
        return users

    with open(CREDENTIALS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            user_id, username, pwd_hash = line.split(DELIMITER)
            users.append((int(user_id), username, pwd_hash))
    return users


def save_user(username, password):    
    users = load_users()
    next_id = 0 if not users else users[-1][0] + 1

    pwd_hash = hashlib.md5(password.encode()).hexdigest()

    with open(CREDENTIALS_FILE, "a") as f:
        f.write(f"{next_id}{DELIMITER}{username}{DELIMITER}{pwd_hash}\n")


def find_user(username, password):
    users = load_users()
    pwd_hash = hashlib.md5(password.encode()).hexdigest()

    for uid, uname, stored_hash in users:
        if uname == username and stored_hash == pwd_hash:
            return (uid, uname)
    return None


def user_menu(user):
    while True:
        print("\nUser Options:")
        print("1 - View profile")
        print("2 - Change password (not implemented)")
        print("0 - Logout")

        choice = input("Your choice: ")

        if choice == "1":
            print(f"\nUser ID: {user[0]}")
            print(f"Username: {user[1]}")
        elif choice == "2":
            print("Change password feature not implemented.")
        elif choice == "0":
            print("Logging out...")
            return
        else:
            print("Invalid choice!")


def main():
    print("Program starting.")

    while True:
        print("\nOptions:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            username = input("Insert username: ")
            password = input("Insert password: ")
            user = find_user(username, password)

            if user:
                print("Login successful!")
                user_menu(user)
            else:
                print("Login failed: invalid username or password.")

        elif choice == "2":
            username = input("Insert username: ")
            password = input("Insert password: ")
            save_user(username, password)
            print("User registration completed!")

        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid choice!")

    print("Program ending.")


if __name__ == "__main__":
    main()