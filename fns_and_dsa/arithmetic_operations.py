def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    if operation == "subtract":
        result = num1 - num2
    if operation == "multiply":
        result = num1 * num2
    if operation == "divide":
        if num1 == 0 or num2 == 0:
            return "Error; cannot perform division by zero" 
        else:
            if num1 != 0 and num2 != 0: 
                result = num1 / num2
    return result
