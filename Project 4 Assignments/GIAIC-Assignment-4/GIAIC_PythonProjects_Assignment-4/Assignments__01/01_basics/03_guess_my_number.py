import random  # Random number generate karne ke liye

def main():
    # 0 se 99 ke beech ek random number choose karna
    secret_number = random.randint(0, 99)
    
    print("🔢 I'm thinking of a number between 0 and 99... Can you guess it?")

    while True:
        try:
            # User se number input lena
            guess = int(input("👉 Enter your guess: "))

            # Conditions check karna
            if guess > secret_number:
                print("📈 Too high! Try again.")
            elif guess < secret_number:
                print("📉 Too low! Try again.")
            else:
                print(f"🎉 Congrats! You guessed it right. The number was: {secret_number}")
                break  # Correct answer milne par loop end kar dena
        except ValueError:
            print("🚫 Please enter a valid number!")

# Main function ko call karna
if __name__ == '__main__':
    main()
