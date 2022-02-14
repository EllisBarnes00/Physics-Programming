from mimetypes import init
from distance import *

# For when distance is known
def find_velocity(distance, time):
	return float(distance)/float(time)

# For when distance isn't known
def find_velocity(initial_velocity, acceleration, time):
	return initial_velocity + (acceleration * time)



# (final velocity - initial velocity) / time(seconds)
def find_acceleration():
	fv = float(input("Final Velocity: "))
	iv = float(input("Initial Velocity: "))
	time_interval = float(input("Time (seconds): "))

	return (fv - iv)/time_interval


