def main():
    # Prompt user for a number and convert to float
    num = float(input("Type a number to see its square: "))

    square = num * num

    print(f"{num} squared is {num ** 2}")
    
    print(f'{num} squared is {square} "using squre verible"')

if __name__ == '__main__':
    main()