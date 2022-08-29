# part 1
print("Electricity bill estimator")
cents = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = (cents * daily_use * billing_days)/100
print(f"Estimated bill ${estimated_bill}")


# part 2
print("Electricity bill estimator 2.0")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
while True:
    tariff = int(input("Which tariff? 11 or 31: "))
    if tariff == 11:
        cents = TARIFF_11
        break
    elif tariff == 31:
        cents= TARIFF_31
        break
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
estimated_bill = (cents * daily_use * billing_days)
print(f"Estimated bill ${round(estimated_bill,2)}")
