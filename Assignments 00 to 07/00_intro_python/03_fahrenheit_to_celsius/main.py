

def main():
    
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0


    print(f"Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.6f}C")

if __name__ == '__main__':
    main()
