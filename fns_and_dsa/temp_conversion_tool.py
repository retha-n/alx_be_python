global FAHRENHEIT_TO_CELSIUS_FACTOR  
global CELSIUS_TO_FAHRENHEIT_FACTOR

FAHRENHEIT_TO_CELSIUS_FACTOR =  5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =  9/5

def convert_to_celsius(fahrenheit):
    conversion = (fahrenheit -32 * FAHRENHEIT_TO_CELSIUS_FACTOR)
    return conversion
def convert_to_fahrenheit(celsius):
    conversion = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32)
    return conversion

temperature = float(input("Enter the temperature to convert:"))
measure = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if measure == "F":
    conversion = convert_to_celsius(temperature)
    print(f"{temperature}°F is {conversion}°C")
elif measure == "C":
    conversion = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {conversion}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")
