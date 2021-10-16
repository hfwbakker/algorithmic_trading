# the formula background

# Price to sales ratio (PSR) = total market value / total sales past 12 months (dus Kindig methode kan niet worden toegepast op bedrijven die minder dan 1 jaar oud zijn?)
# Growth rate = total sales + total earnings December 31st 2021 / total sales + earnings January 1st 2021

# IF Growth rate > 30% & stock price < PSR * 10

# Ik kijk naar de kwartaal groei op jaarbasis, dus vergelijking 2021q3 met 2020q3. Ik weet niet zeker wat Beth doet.

# the formula

price_to_sales_ratio = 0
total_market_value = 0
total_sales_past_12_months = 0

total_year_sales = 0
total_year_earnings = 0
growth_rate = 0

price_to_sales_ratio = total_market_value / total_sales_past_12_months
growth_rate = total_year_sales + total_year_earnings
stock_price = 0

if growth_rate > 0.3 & stock_price < (price_to_sales_ratio * 10):
    print("BUY BUY BUY!")
