# Constants
PROMPT = "What would you like to hear? (Type 'Joke' to hear a joke): "
JOKE = (
    "Here’s a joke for you!\n"
    "Panaversity GPT - Sophia is heading out to the grocery store.\n"
    "A programmer tells her: 'Get a liter of milk, and if they have eggs, get 12.'\n"
    "Sophia returns with 13 liters of milk.\n"
    "The programmer asks why, and Sophia replies: 'Because they had eggs.'"
)
SORRY = "Sorry, I can only tell jokes. Try typing 'Joke'."

def main():
    # Prompt user for input
    user_input = input(PROMPT).strip().lower()

    # Respond based on user input
    if user_input == "joke":
        print("\n" + JOKE)
    else:
        print("\n" + SORRY)

# Run the program
if __name__ == '__main__':
    main()
