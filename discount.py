# Points to note:
# Price is in dollars
# price is formatted to 2 decimal places.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying the discount
if final_price != original_price:
    print("You have a discount of " + str(discount_percent) + "%")
    # format the price to 2 decimal places
    print("Final price after applying discount: ${:.2f}".format(final_price))
else:
    print("No discount applied. Final price remains: ${:.2f}".format(final_price))
