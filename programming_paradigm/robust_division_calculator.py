# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Perform the division
        result = num / den
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is {result}"

