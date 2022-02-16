# Distance traveled by falling is the 
# same as distance traveled but 
# gravity is the acceleration

from math import pow

g = 10 # on earth it is 9.8 but rounded to 10 for calculations
t = float(input("Time: "))
d = .5 * g * pow(t, 2)

print("Distance fallen: ", d)