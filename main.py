from decimal import Decimal, ROUND_HALF_UP

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
amount = total_bill*(1+tip_percentage/100)/num_of_people
rounded_amount = Decimal(amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"Each person should pay ${rounded_amount}")
