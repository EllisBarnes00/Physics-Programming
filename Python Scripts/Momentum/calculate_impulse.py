# Impulse is the amount of force applied over a time
# The longer the time, the less force will be applied at 
# a given moment. So a ball hitting a wall at an angle 
# would do less damage than one straight on.

# Impulse = Ft

force = float(input("Force Applied:"))
time = float(input("Time: "))
impulse = force * time

print("Impulse: ", impulse)