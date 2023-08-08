def calculate_compound_interest(principal, rate, time, pmt):
    amount = principal
    for _ in range(time):
        amount = (amount + pmt) * (1 + rate / 100)
    interest = amount - (principal + (pmt * time))
    return amount, interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = int(input("Enter the time period (in years): "))
pmt = float(input("Enter the periodic payment amount: "))

result, interest = calculate_compound_interest(principal, rate, time, pmt)

print("Compound Interest Calculation Results:")
print("Principal amount:", principal)
print("Annual interest rate:", rate)
print("Time period (in years):", time)
print("Periodic payment amount:", pmt)
print("Amount after compound interest:", round(result, 2))
print("Interest earned:", round(interest, 2))
