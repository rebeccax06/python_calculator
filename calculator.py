print('Welcome to the Calculator!')
def add(x,y):
  return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return round(x/y,2)
def exponent(x,y):
    return x**y

operations = {'1':add,'2':minus,'3':multiply,'4':divide,'5':exponent}
#continues doing operations until the user tells it to stop

while True:
    userOperation = input("""\nWhat operation do you want to do?
    Enter '1' for +
    Enter '2' for -
    Enter '3' for *
    Enter '4' for /
    Enter '5' for ^
    Input: """)

    if int(userOperation) in range(1,6):
        firstNumber = input('\nEnter the first number: ')
        secondNumber = input('\nEnter the second number: ')
        while not firstNumber.isnumeric() or not secondNumber.isnumeric():
            if not firstNumber.isnumeric():
                 firstNumber = input('\nEnter the first number: ')
            if not secondNumber.isnumeric():
                 secondNumber = input('\nEnter the second number: ')
    
        print('\nThe answer is %.2f' % operations[userOperation](int(firstNumber),int(secondNumber)))   
        

    else:
      print('Enter a valid number')
    again = input('\nDo you want to go again?\nEnter "no" or "n" to stop: ').lower()
    
   
    if again == 'n' or again == 'no':
        break
