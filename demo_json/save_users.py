import tabulate

from inputs_module import ask_for_email, ask_for_name
from filehandler import generate_id, save_users_to_json, read_users_from_json
"id:name:email"
def add_new_user():
    # ask for , name, email
    name = ask_for_name()
    email = ask_for_email()
    id = generate_id()
    user_info = {
        "id": id,
        "name": name,
        "email": email
    }
    saved  = save_users_to_json("users.json", user_info)

    if saved:
        print("--- user saved successfully ---")
    else:
        print("---- please try again ---")

def list_all_users():
    users = read_users_from_json("users.json")
    print(tabulate.tabulate(users, headers="keys", tablefmt="psql"))


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





