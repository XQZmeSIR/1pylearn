# Main function

def main():
    sales = get_sales()                     # Get sales over the month
    prepay = get_prepay()                   # Get an anvanced pay
    comm_rate = determine_comm_rate(sales)  # Determine commision rate
    
    payment = sales * comm_rate - prepay    # Getting the payment for a month

    print(f"The payment will be {payment:,.2f}!")

    if pay < 0:
        print('U have to pay the discrepancy in price to the company!')


def get_sales():  # First function in MAIN for getting input.
    monthly_sales = float(input('Enter the monthly sales: '))
    return monthly_sales  # We return the value to MAIN func.