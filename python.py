#Get user input
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
operation=input("Enter an operator (+,-,*/)")
        
        #Perform the operation
        if operation=="+":
        result=num1+num2
        print(f"{num1}+{num2}={result}")

        elif operation=="-";
        result=num1-num2
        print(f"{num1}-{num2}={result}")

        elif operation=="*";
        result=num1*num2
        print(f"{num1}*{num2}={result}")

        elif operation=="/";
        result=num1/num2
        print(f"{num1}/{num2}={result}")
elif num2 !=0; and num1 !=0;
 result=num1/num2

 else:
print("Error!Division by Zero is not allowed.")

        else:
        print("Invalid operation! please enter +,-,* or /.")