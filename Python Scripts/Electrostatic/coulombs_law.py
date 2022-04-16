# Relationship among electrical force, charge, and distance
# Unit of charge is coulumb, C

# Equation:
# F = k(q1q2)/(r^2)
# C = (9.1)^9 ((charge 1 * charge 2) / distance^2)

k = 9 * pow(10, 9) # 9,000,000,000
charge_1 = float(input("q1: "))
charge_2 = float(input("q2: "))
distance = float(input("Distance (m): "))

coulumbs = k * (((charge_1 * pow(10, -9)) * (charge_2 * pow(10, -9)) / pow(distance, 2)))
print(f"C: {coulumbs:.2e}")