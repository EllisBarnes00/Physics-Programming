from math import pow

# For use in a function where the distances are known
def get_distance(initial_distance, final_distance):
	return float(final_distance) - float(initial_distance)

# Use when the user needs to input
def get_distance():
	initial_distance = float(input("Initial distance: "))
	final_distance = float(input("Final Distance: "))
	return float(final_distance) - float(initial_distance)

# For when acceleration and time appear
def get_distance(acceleration, time):
	return .5 * (acceleration * pow(time, 2))