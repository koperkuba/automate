def collatz(number):
    if (number % 2 == 0):
        value = number // 2
    else:
        value = 3 * number + 1
    return value

userInput = int(input('Write a number please: '))
print('The Collatz sequence is: \n' + str(userInput))

newInput = collatz(userInput)
print(newInput)

while newInput != 1:
    newInput = collatz(newInput)
    print(newInput)