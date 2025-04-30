import random

# Constants
N_NUMBERS: int = 10   # Kitne numbers generate karne hain
MIN_VALUE: int = 1    # Minimum value
MAX_VALUE: int = 100  # Maximum value

def main():
    print(f"🎲 Generating {N_NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE}...\n")
    
    # Random numbers generate karna
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Numbers ko ek line me print karna
    print("Generated Numbers:", *random_numbers)

    # Optional: Sorted version bhi dikhana
    print("Sorted Numbers   :", *sorted(random_numbers))

if __name__ == '__main__':
    main()
