# Grav. Potential Energy = mass (kg) * g * height (m)
# PE_g = mgh
# Measured in Joules

m = float(input("Mass: "))
g = float(input("Gravity: "))
h = float(input("Height: "))

potential_energy = m*g*h
print("Potential Grav. Energy: ", potential_energy, "\bJ")