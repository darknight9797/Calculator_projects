word = float(input("Enter the no. of words: "))
cost_in_dollars = word * 0.015
cost_in_rupees = word * 1.40
print(f"Cost in dollars: ${cost_in_dollars:.2f}")
print(f"Cost in rupees: ₹{cost_in_rupees:.2f}")