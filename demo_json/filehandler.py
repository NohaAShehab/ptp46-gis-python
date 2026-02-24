"""

    .json file ===> 1- [{}, {}]
    2- {
        users: [{}]
    }


"""

"""
    to generate id --> create user ??
    read value from id.txt
    +1
    then save id.txt
    use the +1

"""


def generate_id():
    try:
        with open('id.txt','r') as f:
            id = f.read()
            id = int(id)
            id = id + 1

        with open('id.txt','w') as f:
            f.write(str(id))

    except Exception as e:
        return False

    return id


import json

def read_users_from_json(file_name):
    try:
        with open(file_name,'r') as f:
            data = json.load(f) # json load --> accept file object -->
            # then read its content to python
            return data

    except Exception as e:
        return []


# to save new object in the json
# first read old data ==> list of dicts
# then append the dict --> to the list
# then write the updated list to the file

def save_users_to_json(file_name,data):
    existing_users = read_users_from_json(file_name)
    existing_users.append(data)
    try:
        with open(file_name,'w') as f:
            json.dump(existing_users,f, indent=4)
            return True
    except Exception as e:
        return False

if __name__ == '__main__':
    result = read_users_from_json('users.json')
    print(result)






