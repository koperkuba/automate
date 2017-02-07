# This program says hello and asks for my name.

print('What is your name? ') # aks for their name
myName = input()
print('Its is good to meet You, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print(f'You will be {str(int(myAge) + 1)} in a year.')