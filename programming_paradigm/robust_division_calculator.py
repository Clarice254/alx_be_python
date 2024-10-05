#robust_division_calculator.py
def safe_divide(numerator, denominator):
    """Perform division and handle errors."""
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter numeric values only.")

    else:
        print(f"The result of the division is {result}")
    