i = 1
while True:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == 'admin' and password == '123':
        print('Login successful!')
        break
    else:
        print('Invalid username or password!')
        print(f'You have left {3-i} chances!')
        i += 1
    if i > 3:
        print('You have been banned!')
        break
