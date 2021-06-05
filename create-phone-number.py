def create_phone_number(n):
    #your code here
    # create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

    stringNumber = "".join(str(i) for i in n)

    print(stringNumber)

    return "("+stringNumber[0:3]+") "+stringNumber[3:6]+"-"+stringNumber[6:]

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))