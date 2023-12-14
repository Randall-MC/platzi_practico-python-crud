import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    }
]

def welcome():
    print('¡ Welcome to Platzi Ventas !',
          '*' * 30,
          'What would you like to do today?',
          '[C] Create client',
          '[U] Update client',
          '[D] Delete client',
          '[L] List clients',
          '>>>', sep='\n', end=' ')

def create_client(client):
    # Take global variable clients to use it
    global clients

    if client not in clients:
        # Add element client to the list
        clients.append(client)
    else:
        print(f"The client with the name {client} already exists in the database.")
     

def update_client(client_name):
    global clients

    for client in clients:
        if client['name'] == client_name:
            new_name = input('What is the updated client name? ')
            client['name'] = new_name
            break
    else:
        print(f'The client with the name {client_name} does not exist in our database.')


def delete_client(client_name):
    global clients

    for client in clients:
        if client['name'] == client_name:
            clients.remove(client)
            break
    else:
        print(f'The client with the name {client_name} is not exists in our database.')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client["name"]}, {client["company"]}, {client["email"]}, {client["position"]}')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')

    return field


if __name__ == '__main__':
    welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        # Create a dictionary with the client data
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

