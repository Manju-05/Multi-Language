a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))

x=int(input("""enter the number of operation to be performed\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponent\n"""))
match x:
    case 1:
        c=a+b
        print("addition :",c)
    case 2:
        c=a-b
        print("Subtraction :",c)
    case 3:
        c=a*b
        print("Multiplication :",c)
    case 4:
        c=a/b
        print("division :",c)
    case 5:
        c=a%b
        print("modululs :",c)
    case 6:
        c=a**b
        print("Exponent :",c)
    case _:
        print("Enter the Valid number to perform operaration")      