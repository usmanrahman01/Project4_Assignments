def main():
    # Ask the user to enter a number
    # User se ek number input lena
    try:
        curr_value = int(input("Enter a number: "))  
    except ValueError:
        print("Please enter a valid integer.")
        return

    print("\nDoubling the number until it reaches or exceeds 100:")
    # Jab tak value 100 se choti hai, loop chalega
    while curr_value < 100:
        curr_value *= 2  # Value ka double karna
        print(curr_value, end=" ")  # Ek hi line mein output dikhana

# Call the main function
if __name__ == '__main__':
    main()
