from math import pow

acceleration = float(input("Acceleration: "))
time = float(input("Time: "))
distance = .5 * (acceleration * pow(time, 2))

print("Distance Traveled: ", distance)