### Tony Gaddis. Chapter 5: Functions;  Page 273

# Получить месячные продажи продавца.    done 
# Получить сумму авансовой выплаты.     done 
# Применить сумму месячных продаж для определения ставки комиссионных.   done
# Рассчитать выплату продавцу с использованием ранее показанной формулы.
# Если сумма отрицательная, то указат ь, что продавец должен возместить компании разницу.


# Main function
def main():
    sales = get_sales()                     # Get sales over the month
    prepay = get_prepay()                   # Get an anvanced pay
    comm_rate = determine_comm_rate(sales)  # Determine commision rate
    
    payment = sales * comm_rate - prepay    # Getting the payment for a month

    print(f"The payment will be ${payment:,.2f}!")

    if payment < 0:
        print('U have to pay the discrepancy in price to the company!')


def get_sales():                           # First function in MAIN for getting input.
    monthly_sales = float(input('Enter the monthly sales: '))
    return monthly_sales                   # We return the value to MAIN func.


def get_prepay():                          # Second function in MAIN func
    print("Enter the adv pay if there was or type 0 if there weren't.")
    print()
    adv_pay = float(input('Enter the adv pay: '))
    return adv_pay

def determine_comm_rate(sales):             # Third function in MAIN func
    if sales < 10000.00:
        rate = 0.10
    elif sales >= 10000 and sales <= 14999.00:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999.00:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999.00:
        rate = 0.16
    else:
        rate = 0.18

    return rate

main()

# Feedback by ChatGPT
## 1 use dictionary instead of redundant if elif
# commission_rates = {
    #     (0, 9999.99): 0.10,
    #     (10000.00, 14999.99): 0.12,
    #     (15000.00, 17999.99): 0.14,
    #     (18000.00, 21999.99): 0.16,
    # }
    
    # for (min_sales, max_sales), rate in commission_rates.items():
    #     if min_sales <= sales <= max_sales:
    #         return rate
## 2 Use Validation    using  while True:  try except