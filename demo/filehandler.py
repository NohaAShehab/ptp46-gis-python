

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



def save_data(fileName, data):
    try:
        with open(fileName,'a') as f:
            f.write(str(data))
            return True
    except Exception as e:
        return False




def read_data(file_name):
    try:
        with open(file_name,'r') as f:
            data = f.readlines()
            return data

    except Exception as e:
        return []







