# Rate at which electric charge energy is converted into
# another form.
# Measured in watts
# Equation: Power = current * voltage
# 			P = IV

current = float(input("Current/Amps: "))
voltage = float(input("Voltage: "))
power = current * voltage

print("Power: {0} W".format(power))