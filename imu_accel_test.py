import numpy as np

# initializing values
delta_t = 0.0017 # measurements taken every 17 ms
accel_decimal = [12940, 12570, 12000] # matrix of decimal values of acceleration
lsb_matrix = [16384, 16384, 16384] # LSB/g

# converting accelerations to m/s^2
accel_g = np.divide(accel_decimal,lsb_matrix) # in g
accel_values = 9.81*accel_g # in m/s^2

print(accel_values)

# integrating into velocity
vel_values = [0, 0, 0]

for i in range(len(accel_values) - 1):
    vel_values[i + 1] = delta_t*(accel_values[i] + accel_values[i + 1])/2

print(vel_values)

# integrating into distance
dist_values = [0, 0, 0]
for i in range(len(accel_values) - 1):
    dist_values[i + 1] = delta_t*(vel_values[i] + vel_values[i + 1])/2

print(dist_values)
