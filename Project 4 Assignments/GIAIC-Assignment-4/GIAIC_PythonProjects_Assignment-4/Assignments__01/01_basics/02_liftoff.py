def main():
    # Countdown from 10 to 1
    # Loop 10 se 1 tak count karne ke liye
    print("Countdown begins...\n")
    
    for i in range(10, 0, -1):  # 10 se 1 tak reverse countdown
        print(i, end=" ", flush=True)  # Ek hi line me print karna

    # Countdown complete message
    print("\n\n🚀 Liftoff!")  # Thoda dramatic touch!

# Call the main function
if __name__ == '__main__':
    main()
