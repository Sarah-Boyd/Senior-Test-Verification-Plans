import numpy as np

# initializing values
delta_t = 0.0017 # measurements taken every 17 ms
gyro_decimal = [12940, 12570, 12000] # matrix of decimal values of angular velocity
lsb_matrix = [16384, 16384, 16384] # LSB/g

# converting accelerations to m/s^2
gyro_values = np.divide(gyro_decimal,lsb_matrix) # in dps (degrees per second)

print(gyro_values)

# integrating into velocity
dist_values = [0, 0, 0]

for i in range(len(gyro_values) - 1):
    dist_values[i + 1] = delta_t*(gyro_values[i] + gyro_values[i + 1])/2

print(dist_values)
