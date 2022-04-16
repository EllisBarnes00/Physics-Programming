# relationship between voltage, current, and resistance
# States that the current in a circuit varies in direct 
# proportion to the potential difference, or voltage, and 
# inversely with the resistance

# Equation: V = IR
# Voltage = Amps * Ohms
# Voltage = Current * Resistance

current = float(input("Amps/Current: "))
resistance = float(input("Ohms/Resistance: "))

voltage = current * resistance
print("Voltage: {0} V".format(voltage))