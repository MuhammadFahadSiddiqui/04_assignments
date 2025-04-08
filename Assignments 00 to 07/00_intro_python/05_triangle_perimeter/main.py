def main():
    # Get the lengths of the three sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print out the perimeter (sum of the sides) of the triangle
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))
    
    # Print the result using f-string
    print(f'The perimeter of the triangle is {perimeter} "using f-string5"')


if __name__ == '__main__':
    main()
