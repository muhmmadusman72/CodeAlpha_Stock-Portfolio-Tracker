# Hardcoded dictionary defining stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "NVDA": 450,
    "MSFT": 400,
    "AMZN": 175
}

def main():
    print("--- Simple Stock Tracker ---")
    print(f"Available stocks in system: {', '.join(STOCK_PRICES.keys())}\n")
    
    # 1. Get user input for stock name
    stock_name = input("Enter the stock ticker symbol (e.g., TSLA): ").strip().upper()
    
    # Check if the stock exists in our hardcoded dictionary
    if stock_name not in STOCK_PRICES:
        print(f"Error: Stock '{stock_name}' is not in our database.")
        return

    # 2. Get user input for quantity
    try:
        quantity = int(input(f"Enter the quantity of {stock_name} shares purchased: "))
        if quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            return
    except ValueError:
        print("Error: Please enter a valid whole number for quantity.")
        return

    # 3. Basic Arithmetic: Calculate total investment value
    price_per_share = STOCK_PRICES[stock_name]
    total_investment = price_per_share * quantity

    # 4. Display the total investment value
    result_message = (
        f"\n--- Investment Summary ---\n"
        f"Stock: {stock_name}\n"
        f"Price per Share: ${price_per_share}\n"
        f"Quantity: {quantity}\n"
        f"Total Investment Value: ${total_investment}\n"
        f"--------------------------"
    )
    print(result_message)

    # 5. Optional: Save the result to a .txt file
    save_choice = input("\nWould you like to save this summary to a text file? (yes/no): ").strip().lower()
    
    if save_choice in ['yes', 'y']:
        filename = f"{stock_name}_investment.txt"
        try:
            with open(filename, "w") as file:
                file.write(result_message)
            print(f"Success! Summary successfully saved to '{filename}'.")
        except IOError:
            print("Error: Could not save the file.")
    else:
        print("Summary not saved. Thank you for using Stock Tracker!")


    main()