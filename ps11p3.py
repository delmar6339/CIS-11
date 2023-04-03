def compute_commission_and_target(sales):
    commission_rate = 0.1 if sales > 100000 else 0.05
    commission = sales * commission_rate
    next_year_target = sales * 0.05
    return commission, next_year_target
def sales_report():
    last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter sales: "))
    commission, next_year_target = compute_commission_and_target(sales)
    print(f"Salesperson: {last_name}")
    print(f"Commission: ${commission:.2f}")
    print(f"Next Year's Target: ${next_year_target:.2f}")
if __name__ == "__main__":
    sales_report()