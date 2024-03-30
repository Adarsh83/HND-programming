# Program that will be executed the task to calculate the fibonacci number of iterations and factorial of the number.

# Defined the function for fibonacci here
def fibonacci(E_num):
    first = 0
    second = 1
    if E_num < 0:   # Condition for printing string when entered value less than 0.
        print("You entered incorrect value.")
    elif E_num == 0:    # Condition for when entered value is 0.
        return first
    elif E_num == 1:    # Condition for when entered value is 1.
        return second
    else:               # Condition for the value is greater than equal to 2.
        for i in range(2,E_num+1):
            r = first + second  # Here add the value and store in the r variable
            first = second      
            second = r          # Assigned the stored value of r in second variable
        return second

# Defined the function for factorial here
def factorial(E_num):
    fact =E_num                # Assigned the stored value of E_num in fact variable
    for i in range(1,E_num):    # For loop from 1 to E_num value  
       E_num=E_num-1            # Decrement E_num by 1 and store in the E_num variable
       fact = fact*(E_num)     # Multiply fact by E_num and store in the fact
    return fact

# Input value from user and store in E_num variable
E_num=int(input("Enter the Input number: "))
# Print the value for fibonacci returned from fibonacci function
print("Fibonacci value of the number is: ",fibonacci(E_num))
# Print the value for factorial returned from factorial function
print("Factorial value of the number is: ",factorial(E_num))


