total = 0
tax = 0
def compute_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07
def main():
    quantity = int(input("Enter the quantity of the item: "))
    unit_price = float(input("Enter the unit price: "))
    compute_total_and_tax(quantity, unit_price)
    print(f"\nTotal: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")

if __name__ == "__main__":
    main()