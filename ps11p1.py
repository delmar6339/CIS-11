def calculate_discount(quantity, price, discount_rate):
    discount_amount = price * (discount_rate / 100) * quantity
    discounted_price = (price * quantity) - discount_amount
    return discount_amount, discounted_price
def main():
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    discount_rate = float(input("Enter the discount rate (%): "))
    discount_amount, discounted_price = calculate_discount(quantity, price, discount_rate)
    print(f"\nQuantity: {quantity}\nPrice: ${price}\nDiscount Amount: ${discount_amount:.2f}\nDiscounted Price: ${discounted_price:.2f}")
if __name__ == "__main__":
    main()