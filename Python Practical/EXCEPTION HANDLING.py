def divide_number():
    try:
        num1=float("Enter the Numerator:")
        num2=float("Enter the Denominator:")

        result=num1/num2
    except ValueError:
            print("Error: Please enter numeric value only")

    except ZeroDivisionError:
            print("Error: Division by 0 is not allowed")

    else:
            print(f"The result is:{result}")

    finally:
            print("Execution completed")

divide_number()
            
