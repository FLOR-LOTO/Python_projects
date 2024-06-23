import getpass

database = {'florencia': '1234', 'gisele': '5678'}

username = input('Enter your Username: ')
password = getpass.getpass('Enter your Password: ')

if username in database: #verifica si el valor de username está presente en las claves del diccionario database
    while password != database[username]:
        print("Incorrect password. Try again.")
        password = getpass.getpass('Enter your password again: ')
    print('Verified')
else:
    print("Username not found")