passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('Enter Your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
if typedPassword == '123456':
    print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')

print('Working with git is good')