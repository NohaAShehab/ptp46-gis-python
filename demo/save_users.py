from inputs_module import ask_for_email, ask_for_name
from filehandler import generate_id, save_data, read_data
"id:name:email"
def add_new_user():
    # ask for , name, email
    name = ask_for_name()
    email = ask_for_email()
    id = generate_id()
    user_info = f"{id}:{name}:{email}\n"
    saved  = save_data("users.txt", user_info)

    if saved:
        print("--- user saved successfully ---")
    else:
        print("---- please try again ---")

def list_all_users():
    users = read_data("users.txt")
    for user in users:
        user = user.strip()
        user_info = user.split(":")
        print(f"id={user_info[0]}, name={user_info[1]}, email={user_info[2]}")


def main_menu():
    while True:
        choice = input("N. Add new user\nL. List all users\nE. Exit\n")
        if choice.lower() == "n":
            add_new_user()
        elif choice.lower() == "l":
            print("-- list all users --")
            list_all_users()
        else:
            exit()

if __name__ == "__main__":
    main_menu()





