# a product will cot $100, how much tax do we pay?
product = 100
tax_rate = 0.0625
tax = product * tax_rate
print(f'The tax for the product that costs ${product} is ${tax}.')
# add f-string to tell python to format the string to contain variables


computer_price = 900
iphone_price = 1100
def calc_tax(price, tax_rate):
    """Calculate product tax based on given price and return the tax amount"""
    #tax_rate = 0.0625
    tax = price * tax_rate
    #print(f'The tax for the product that costs ${price} is ${tax}.')    
    #calc_tax(computer_price)
    #calc_tax(iphone_price)
    #print(tax)
    # if the function does not explicitly return any value, it will return None
    return tax

mass_rate = 0.0625
ny_rate = 8.875 / 100
tax_computer = calc_tax(computer_price, mass_rate)
tax_iphone = calc_tax(iphone_price, ny_rate)

total_tax = calc_tax(computer_price, mass_rate) + calc_tax(iphone_price, ny_rate)
print(total_tax)



