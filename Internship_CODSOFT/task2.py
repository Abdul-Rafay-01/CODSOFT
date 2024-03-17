#TASK 2
# CALCULATOR
# Design a simple calculator with basic arithmetic operations. 
# Prompt the user to input two numbers and an operation choice. 
# Perform the calculation and display the result.

print("Welcome To Python Calculator")
print("Kindly Select An Opreation To Countinue")

while True:
    print(f"1) Addition  ")
    print(f"2) Subtraction  ")
    print(f"3) Multiplication ")
    print(f"4) Division  ")
    print(f"5) Exit  ")
    
    user_input= input("Kindly Enter Your Choice (1,2,3,4,5): ")
    if user_input == '5':
        print ("Exiting The Calculator. Thank You For Using. ")
        break
    if user_input == '1':
        first= int(input("Kindly Enter The First Number: "))
        second= int(input("Kindly Enter The Second Number: "))
        Result = first+second
        print(f"Result: {first} + {second} = {Result}")
    
    elif user_input=="2":
        first=int(input("Kindly Enter The First Number: "))
        second=int(input("Kindly Enter The Second Number: "))
        Result=first-second
        print(f"Result: {first} - {second} = {Result}")  


    elif user_input=="3":
        first=int(input("Kindly Enter The First Number: "))
        second=int(input("Kindly Enter The Second Number: "))
        Result=first*second
        print(f"Result: {first} * {second} = {Result}")    

    elif user_input=="4":
        first=int(input("Kindly Enter The First Number: "))
        second=int(input("Kindly Enter The Second Number: "))
        Result=first/second
        print(f"Result: {first} / {second} = {Result:.2f}")

    else: print("Kindly Enter A Valid Choice")



