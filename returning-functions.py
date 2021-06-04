def calculate_recursive_sequence(number):
    print(number)
    if number == 0:
        return number

    return calculate_recursive_sequence(number-1)

def calculate_iterative_sequence(number):
    for i in range(number, -1, -1):
        print(i)

number = int(input("Write a number to calculate its descending sequence to 0: "))

print("Recursive sequence")
calculate_recursive_sequence(number)

print("Iterative sequence")
calculate_iterative_sequence(number)