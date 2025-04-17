def celsius_to_fahrenheit(celsius):
     return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("CELSIUS TO FAHRENHEIT")
    temp = float(input("Enter the temperature value:"))
    unit = input("Is it Celsius or Fahrenheit(C or F):")
    if unit == 'C':
        converted = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {converted:.2f}°F")
    elif unit == 'F':
        converted = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {converted:.2f}°C")
    else:
        print("Wrong operation")
main()



