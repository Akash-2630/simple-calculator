print("1 is +")
print("2 is -")
print("3 is *")
print("4 is /")
option = int(input("choose an operator: "))
result = 0

if option in [1, 2, 3, 4]:
    num1 = int(input("enter first num: "))  
    num2 = int(input("enter second num: "))  

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        result = num1 // num2

    print("result is: {}".format(result))
else:
    print("invalid operator")