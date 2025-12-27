invst = float(input("Enter Initial Investment Amount: "))
prd = int(input("Enter Project Period (in years): "))
operating_cost = float(input("Enter Annual Operating Cost: "))
expected_sales = float(input("Enter Expected Annual Sales Revenue: "))

annual_profit = expected_sales - operating_cost
total_profit = annual_profit * prd
total_roi = ((total_profit - invst) / invst) * 100
annualized_roi = ((((total_profit) / invst) ** (1/prd)) - 1) * 100

print("-" * 30)
print(f"Annual Profit: {annual_profit:,.2f}")
print(f"Total Profit over {prd} years: {total_profit:,.2f}")
print(f"Total Cumulative ROI: {total_roi:.2f}%")
print(f"Annualized ROI: {annualized_roi:.2f}%")
