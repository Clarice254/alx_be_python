#robust_division_calculator.py
def safe_divide(numerator, denominator):
    """Perform division and handle errors."""
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        result = num1 / num2

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

    return f"The result of the division is {result}"
    