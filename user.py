user_data = {}

def logon():
    identity = 'admin'
    password = 'abcdefg'
    name = input('Username: ')
    input_password = input('Password: ')
    if name == identity and password == input_password:
        main()
    else:
        print('Wrong username/password.')

def build_dict():
    user_data.clear()
    with open('user.txt', 'r') as build_user_data:
        for line in build_user_data:
            a = line.strip()
            if a == '':
                continue
            else:
                user_password = a.split()
                if not len(user_password) == 2:
                    print('Username/password format different from standard. Ignoring...')
                    continue
                else:
                    user_data[user_password[0]] = user_data.get(user_password[0], '') + user_password[1]
    
def main():
    print('Building database...')
    build_dict()
    print('Finish building database.')
    
    while True:
        print('''
Welcome to Database.
        
[1] - Add user
[2] - Change password
[3] - Remove user
[4] - Exit
              ''')
        user_option = input('What would you like to do? ')
        if user_option == '1':
            add_user()
        elif user_option == '2':
            change_pw()
        elif user_option == '3':
            delete_user()
        elif user_option == '4':
            print('Exiting...')
            break
        else:
            print('Invalid option. Exiting now...')
            break

def add_user():
    username = input('Enter the id you want to use: ')

    while username in user_data:
        print('Sorry, the id you have entered has been used. Please enter another id.')
        username = input('Enter the id you want to use: ')
            
    password = input('Enter the password you want to use (space is not allowed): ')
    while ' ' in password:
        print("Your password cannot have a space. Replace the space with another character e.g '_'")
        password = input('Enter the password you want to use: ')
    
    confirm_password = input('Confirm your password: ')
    
    while not (password == confirm_password):
        print('Your passwords are different! Please enter your password again.')
        password = input('Enter the password you want to use: ')
        confirm_password = input('Confirm your password: ')

    id_pw = '\n' + username + ' ' + password
    print('Adding user...')
    with open('user.txt', 'a') as user_add:
        user_add.write(id_pw)
    print('User added.')
    build_dict()
    print(user_data)
    
def change_pw():
    username = input('Enter the username you like to change: ')
    
    if username in user_data:
        password = input('Enter the new password you want to use: ')
        confirm_password = input('Confirm your new password: ')
        
        while not (password == confirm_password):
            print('Your passwords are different! Please enter your password again.')
            password = input('Enter the new password you want to use: ')
            confirm_password = input('Confirm your new password: ')

        print('Changing password...')
        user_data[username] = password
        with open('user.txt', 'w') as pw_change:
            for identity, password in user_data.items():
                id_pw = identity +  ' ' + password + '\n'
                pw_change.write(id_pw)
        print('Password changed...')
        build_dict()
        print(user_data)
    else:
        print('The username you have entered is not in the database!')

def delete_user():
    username = input('Enter the username you like to delete: ')

    if username in user_data:
        print('Deleting user record...')
        del user_data[username]
        with open('user.txt', 'w') as user_change:
            for identity, password in user_data.items():
                id_pw = identity +  ' ' + password + '\n'
                user_change.write(id_pw)
        print('User record deleted...')
        build_dict()
        print(user_data)
    else:
        print('The username you have entered is not in the database!')
    
logon()
