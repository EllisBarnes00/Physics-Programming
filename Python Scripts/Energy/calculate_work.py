# Work is measured in Joules
# Work = Force * distance
# W = Fd
# 1000J = (50kg * g) * 2m

def get_force(weight, acceleration):
	return weight * acceleration

w = float(input("Weight: "))
a = float(input("Acceleration: "))
d = float(input("Distance: "))

work_done = (get_force(w, a)) * d
print("Work Done: ", work_done, "\bJ")