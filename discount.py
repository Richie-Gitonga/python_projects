def calculate_discount(price, discount_rate):
    result = 0
    if(discount_rate > 0.02):
        result = price * discount_rate
    else:
        result = price
    return result
price = float(input('Enter the price: '))
discount = float((input('Enter the discount percentage: ')))/100

print(calculate_discount(price, discount))

