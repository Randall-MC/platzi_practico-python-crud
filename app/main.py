clients = ['Pablo', 'Ricardo']

def welcome():
    print('¡ Welcome to Platzi Ventas !',
          '*' * 30,
          'What would you like to do today?',
          '[C] Create client',
          '[U] Update client',
          '[D] Delete client',
          '>>>', sep='\n', end=' ')

def create_client(client_name):
    # Take global variable clients to use it
    global clients

    if client_name not in clients:
        # Add element client_name to the list
        clients.append(client_name)
    else:
        print(f"The client with the name {client_name} already exists in the database.")
     

def update_client(client_name, new_client_name):
    global clients

    if client_name in clients:
        clients[clients.index(client_name)] = new_client_name
    else:
        print(f'The client with the name {client_name} is not exists in our database.')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print(f'The client with the name {client_name} is not exists in our database.')


def list_clients():
    print(clients)


def _get_client_name():
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
        new_client_name = input('What is the new client name? ')
        update_client(client_name, new_client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

