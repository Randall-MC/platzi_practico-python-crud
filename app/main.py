import os
import csv

CLIENT_TABLE = './app/data/.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def create_client(client):
    # Take global variable clients to use it
    global clients

    if client not in clients:
        # Add element client to the list
        clients.append(client)
    else:
        print(f"The client with the name {client} already exists in the database.")
     

def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client["name"]}, {client["company"]}, {client["email"]}, {client["position"]}')


def update_client(client_list, client_id, low, high):
    global clients

    if low > high:
        return print(f'The client with the id: {client_id} does not exist in our database.')
    else:
        mid = (low + high) // 2
        if mid == client_id:
            updated_client = _get_client_from_user()

            if updated_client['name']:
                client_list[mid]['name'] = updated_client['name']
            else:
                updated_client['name'] = client_list[mid]['name']
            if updated_client['company']:
                client_list[mid]['company'] = updated_client['company']
            else:
                updated_client['company'] = client_list[mid]['company']
            if updated_client['email']:
                client_list[mid]['email'] = updated_client['email']
            else:
                updated_client['email'] = client_list[mid]['email']
            if updated_client['position']:
                client_list[mid]['position'] = updated_client['position']
            else:
                updated_client['position'] = client_list[mid]['position']
        elif client_id < mid:
            return update_client(client_list, client_id, low, mid-1)
        else:
            return update_client(client_list, client_id, mid+1, high)
        

def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break
    else:
        print(f'The client with the id {client_id} is not exists in our database.')

def search_client(client_name):
    global clients

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True
        

def _get_client_field(field_name):
    field = input(f'What is the client {field_name}? ')
    if field == '':
        return None
    else:
        return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client

def _create_data_folder():
    directory = './app/data'
    file_path = os.path.join(directory, '.clients.csv')

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass

    return True


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        
    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def welcome():
    print('What would you like to do today?',
          '[C] Create client',
          '[L] List clients',
          '[U] Update client',
          '[D] Delete client',
          '[S] Search client',
          '[E] Exit]',
          '>>>', sep='\n', end=' ')


if __name__ == '__main__':

    _create_data_folder()

    _initialize_clients_from_storage()

    print('*' * 32,
        '* ¡ Welcome to Platzi Ventas ! *',
          '*' * 32, sep='\n')

    command = ''

    while command != 'E':

        welcome()

        command = input()
        command = command.upper()

        if command == 'C':
            client = _get_client_from_user()
            create_client(client)
        elif command == 'L':
            list_clients()
        elif command == 'U':
            client_id = int(_get_client_field('id'))
            update_client(clients, client_id, 0, len(clients) - 1)
        elif command == 'D':
            client_id = int(_get_client_field('id'))
            delete_client(client_id)
        elif command == 'S':
            client_name = _get_client_field('name')
            found = search_client(client_name)

            if found:
                print(f'The client {client_name} is in our client\'s list')
            else:
                print(f'The client {client_name} is not in our client\'s list')
        elif command == 'E':
            break
        else:
            print('Invalid command')

    _save_clients_to_storage()
