
def main():
    # Get the year to check from the user
    year = int(input("Please input a year: "))

    # Check if the year is a leap year based on the given conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Call the main function
if __name__ == '__main__':
    main()
