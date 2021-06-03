def add_two_numbers():
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
    print("Addition of ", number1, "and", number2, "is", number1 + number2)

def multiply_two_numbers(): 
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
    print("Multiplication of ", number1, "and", number2, "is", number1 * number2)


print("Please select a option right here")
print("1. Add two numbers")
print("2. Multiply 2 numbers")
print("3. Exit\n")

option = int(input("Your option: "))


if option == 1:
    add_two_numbers()
elif option == 2:
    multiply_two_numbers()
else:
    print("Adiós")
    exit()