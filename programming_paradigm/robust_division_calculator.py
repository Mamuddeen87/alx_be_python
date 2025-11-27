# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float (handle non-numeric)
        num = float(numerator)
        den = float(denominator)

        # Perform division (handle division by zero)
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

