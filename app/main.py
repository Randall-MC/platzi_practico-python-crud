import sys

clients = ['Pablo', 'Ricardo']

def welcome():
    print('¡ Welcome to Platzi Ventas !',
          '*' * 30,
          'What would you like to do today?',
          '[C] Create client',
          '[U] Update client',
          '[D] Delete client',
          '[L] List clients',
          '[S] Search client',
          '>>>', sep='\n', end=' ')

def create_client(client_name):
    # Take global variable clients to use it
    global clients

    if client_name not in clients:
        # Add element client_name to the list
        clients.append(client_name)
    else:
        print(f"The client with the name {client_name} already exists in the database.")
     

def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print(f'The client with the name {client_name} is not exists in our database.')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print(f'The client with the name {client_name} is not exists in our database.')


def search_client(client_name):
    global clients

    return client_name in clients


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client}')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return input('What is the client name? ')


if __name__ == '__main__':
    welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the new client name? ')
        update_client(client_name, updated_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print(f'The client {client_name} is in the client\'s list')
        else:
            print(f'The client {client_name} is not in our client\'s list')
    else:
        print('Invalid command')

