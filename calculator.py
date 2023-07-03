while True:
    print("Please select operation")
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exit")
    o = int(input("Select operations from 1, 2, 3, 4, 5 : "))
    if o == 5:
        break
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    if o == 1:
        print("Addition of", a, "and", b, "is", a+b)
    elif o == 2:
        print("Substraction of", a, "and", b, "is", a-b)
    elif o == 3:
        print("Multiplication of", a, "and", b, "is", a*b)
    elif o == 4:
        if b == 0:
            print("Division by zero is undefined")
        else:
            print("Division of", a, "and", b, "is", a/b)    
    else:
        print("Invalid input")
        continue
              