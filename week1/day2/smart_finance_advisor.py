savings = float(input("Enter savings amount: "))

if savings >= 10000:
    print("Excellent Savings")
elif savings >= 5000:
    print("Good Progress")
elif savings >= 1000:
    print("Building Momentum")
else:
    print("Keep Saving")