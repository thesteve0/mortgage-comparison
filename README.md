# mortgage-comparison

This is a little program I wrote get my head around the interaction between mortgage interest rate versus housing prices. The idea I am exploring is:

`Is it better to buy at a low interest rate in a hot market or wait until prices go down a bit but interest rates will go up`
                               
Used the following formula

M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

M = monthly payment amount                                               

P = principal loan amount

i = monthly interest rate

n = number of months required to repay the loan
                                                          
Got this formula from this [page](https://www.businessinsider.com/personal-finance/how-to-calculate-mortgage-payment)

Inputs:
1. House Price - range from lower estimate to upper estimate - integers
1. How much you put down - just one integer value
1. Interest rate - range from lower estimate to upper estimate - decimal
1. Length of the loan (in years) - integer

This program does not include any other monthly costs, such as taxes, insurance, or mortgage insurance (even though mortgage insure in invoked for various reasons that may depend on the variables above).

Output
A CSV file for a down payment + loan length that looks something like

id (int),House Price (int), Interest Rate (decimal),Total Payment (int),Monthly Payment (int)
1,100000,3.2,500000,2000
2,100000,3.3,501000,2050
3,110000,3.2,506000,2070
....
