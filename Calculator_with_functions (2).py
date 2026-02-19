#Pseudo code
#1 import cmath function so that it's possible to have a negative square root
#2 write functions of arithematic operations(remember rules of operations, especially that dividing by zero gives you an error)
#3 use while loop to create a running calculator, use break to escape from invalid choice
#4 get choice of of operations through an input
#5 use if else statement to create an exit , second elif on square root since it has only one input, the rest of the choices have two inputs with each choice using both the inputs
#6 print the outcome of the required operation

import cmath

def add(n1,n2):
    return(n1 + n2)
    
def diff(n1,n2):
    return(n1 - n2)
    
def prod(n1,n2):
    return(n1 * n2)
    
def div(n1,n2):
    if n2 == 0:
        return "Error! Division by zero"
    return(n1/n2)
    
def pow(n1,n2):
    return n1**n2
    
def sqrt(n1):
    return cmath.sqrt(n1)

def modulus(n1,n2):
    if n2 == 0:
        return "Error, Division by zero is not possible"
    return n1%n2
    
def fdiv(n1,n2):
    if n2 == 0:
        return "Error, Division by zero is not possible"
    return n1//n2
    




while True:
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. power")
    print("6. square root")
    print("7. modulus")
    print("8. floor division")
    print("9. exit")
    choice = int(input("Enter your choice of operation: "))
    
    if choice == 9:
        print("Exiting calculator...")
        break
    
    elif choice == 6:
        n1 = int(input("enter no.1: "))
        print(f'square root of {n1} is {sqrt(n1)}')
    
    else:
        if choice == 1:
            print(f'sum of {n1} and {n2} is {add(n1,n2)} ')
        elif choice == 2:    
            print(f'difference of {n1} and {n2} is {diff(n1,n2)} ')
        elif choice == 3:    
            print(f'product of {n1} and {n2} is {prod(n1,n2)} ')
        elif choice == 4:    
            print(f'quotient of {n1} and {n2} is {div(n1,n2)} ')
        elif choice == 5:
            print(f'power of {n1} and {n2} is {pow(n1,n2)} ')
        elif choice == 7:
            print(f'modulus of {n1} and {n2} is {modulus(n1,n2)} ')
        elif choice == 8:
            print(f'floor division of {n1} and {n2} is {fdiv(n1,n2)} ')
        else:
            print("invalid choice")
        