# How quickly something is going in a direction
# acceleration = change in velocity / time
# ex. (60 km/hr) / 10 sec. = 6 (km/h)/s or 6 km/h/s 

iv = float(input("Initial Velocity: "))
fv = float(input("Final Velocity: "))
t = float(input("Time: "))

a = (fv - iv)/t
print("Acceleration: ", a)