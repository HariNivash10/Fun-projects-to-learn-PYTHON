a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
z=input("Enter the operation you want to perform (+, -, *, /): ")
match z:
    case "+" | "plus":
        c=a+b
        print("The sum of the two numbers is:",c)
    case "-" | "minus":
        d=a-b
        print("The difference of the two numbers is:",d)
    case "*" | "multiply":
        e=a*b
        print("The product of the two numbers is:",e)
    case "/" | "division" if b==0:
        print("Error: can't divide with 0")
    case "/" | "division" :
        f=a/b
        print("The division of the two numbers is:",f)
    case _:
        print("Invalid operation")
