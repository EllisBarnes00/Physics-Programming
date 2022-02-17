# Ken. Potential Energy is when something is in motion
# Depends on mass and squared speed
# KE = .5 * mass * (velocity^2)
# KE = .5 * kg * (10 * 10)
from math import pow

m = float(input("Mass: "))
v = float(input("Speed: "))
kenetic_energy = .5 * m * pow(v, 2)

# If speed is doubled, then the kenetic energy is quadrupled

print("Kenetic Energy: ", kenetic_energy, "\bJ") 