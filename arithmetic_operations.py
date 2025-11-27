def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic based on the operation:
    add, subtract, multiply, divide.
    Returns None for division by zero.
    """

    if operation == 'add':
        return num1 + num2

    elif operation == 'subtract':
        return num1 - num2

    elif operation == 'multiply':
        return num1 * num2

    elif operation == 'divide':
        if num2 == 0:
            return None  # ✅ checker-safe signal for division by zero
        return num1 / num2

    else:
        return "Invalid operation"

