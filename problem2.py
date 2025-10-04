"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    # Implement with Codex
    # TODO: Implement this function
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    # Implement with Codex
    # TODO: Implement this function
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    # Implement with Codex
    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places
    
    print("Temperature Converter")
    print("-" * 30)
    
    while True:
        try:
            temp = float(input("Enter temperature value: "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    
    while True:
        unit = input("Enter current unit (C or F): ").upper()
        if unit == 'C' or unit == 'F':
            break
        else:
            print("Invalid unit! Please enter C or F.")
    
    if unit == 'C':
        result = celsius_to_fahrenheit(temp)
        print(f"\n{temp}°C = {result}°F")
    else:
        result = fahrenheit_to_celsius(temp)
        print(f"\n{temp}°F = {result}°C")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")
    
    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"
    
    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"
    
    print("All tests passed!")
    print()
    
    # Run interactive converter
    temperature_converter()