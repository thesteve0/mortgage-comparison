import numpy as np
from decimal import *

house_price_range = [1100000, 1600000]
house_increment = 50000
down_payment = 300000
interest_rate_range = [Decimal(2.6), Decimal(4.0)]
interest_increment = Decimal(0.2)
term_years = 30

if __name__ == '__main__':
    for h in range(house_price_range[0], house_price_range[1]+house_increment, house_increment):
        for i in np.arange(interest_rate_range[0], interest_rate_range[1] + interest_increment, interest_increment):

            print("house price: " + str(h) + " interest rate: " + str(i))
