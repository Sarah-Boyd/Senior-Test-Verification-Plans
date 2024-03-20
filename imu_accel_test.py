# Welcome to the IMU accelerometer test script! To proceed, please replace the following variables: 
#   delta_t: the time difference between measurements, in seconds
#   accel_hex_x: hexadecimal values of the x-axis accelerometer readings
#   accel_hex_y: hexadecimal values of the y-axis accelerometer readings
#   accel_hex_z: hexadecimal values of the z-axis accelerometer readings
#   lsb_value: sensitivity in LSB/g, where LSB = Least Significant Bit and g = 9.81 m/s^2

import numpy as np
from functools import reduce
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt

# initializing values - values to be replaced by user
delta_t = 0.087 # measurements taken every 87 ms
accel_hex_x = ["E307", "2308", "F107", "F707", "EF07", "1208", "8607", "E307", "CD07", "EF07", "9107", "AE07", "1A08", "0D08", "F507", "E507", "0F08", "EB07", "0208", "FE07", "AC07", "F007", "3B08", "1C08", "D807"]
accel_hex_y = ['3800', '4E01', '9201', 'DC01', 'CB01', 'AA01', '6101', '3901', '2E01', 'BF01', '5C01', 'BA01', 'A501', '9510', 'C401', 'B701', 'F301', '3C02', '4E02', '9701', '7601', '5802', '3402', '1F02', 'DF01']
accel_hex_z = ['290E', 'E20D', '050E', 'CF0D', 'F20D', 'E30D', '4F0E', '0C0E', '2D0E', 'F60D', '2D0E', '3C0E', '0E0E', '190E', '1D0E', '000E', 'E70D', 'EF0D', 'F00D', '130E', '140E', 'E50D', 'DD0D', 'EF0D', 'F70D']
lsb_value = 16384 # LSB/g

# making arrays of zero
accel_dec_x = np.zeros(len(accel_hex_x))
accel_dec_y = np.zeros(len(accel_hex_x))
accel_dec_z = np.zeros(len(accel_hex_x))

time_array = np.zeros(len(accel_hex_x))
lsb_matrix = np.zeros(len(accel_hex_x))

accel_decimal_x = np.zeros(len(accel_hex_x))
accel_decimal_y = np.zeros(len(accel_hex_x))
accel_decimal_z = np.zeros(len(accel_hex_x))

vel_values_x = np.zeros(len(accel_hex_x))
vel_values_y = np.zeros(len(accel_hex_x))
vel_values_z = np.zeros(len(accel_hex_x))

dist_values_x = np.zeros(len(accel_hex_x))
dist_values_y = np.zeros(len(accel_hex_x))
dist_values_z = np.zeros(len(accel_hex_x))

# filling in time and LSB/g arrays
for i in range(len(time_array)):
    if i > 0:
        time_array[i] = time_array[i - 1] + delta_t

for i in range(len(accel_hex_x)):
    lsb_matrix[i] = lsb_value

# converting acceleration measurements
for i in range(len(accel_hex_x)): # converting from hexadecimal to decimal
    accel_dec_x[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in accel_hex_x[i]])
    accel_dec_y[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in accel_hex_y[i]])
    accel_dec_z[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in accel_hex_z[i]])

accel_g_x = np.divide(accel_dec_x,lsb_matrix) # converting to g
accel_g_y = np.divide(accel_dec_y,lsb_matrix)
accel_g_z = np.divide(accel_dec_z,lsb_matrix)

accel_values_x = 9.81*accel_g_x # converting to m/s^2
accel_values_y = 9.81*accel_g_y
accel_values_z = 9.81*accel_g_z

# integrating to velocity
for i in range(len(accel_values_x) - 1):
    vel_values_x[i + 1] = delta_t*(accel_values_x[i] + accel_values_x[i + 1])/2
    vel_values_y[i + 1] = delta_t*(accel_values_y[i] + accel_values_y[i + 1])/2
    vel_values_z[i + 1] = delta_t*(accel_values_z[i] + accel_values_z[i + 1])/2

# integrating to distance
for i in range(len(accel_values_x) - 1):
    dist_values_x[i + 1] = delta_t*(vel_values_x[i] + vel_values_x[i + 1])/2
    dist_values_y[i + 1] = delta_t*(vel_values_y[i] + vel_values_y[i + 1])/2
    dist_values_z[i + 1] = delta_t*(vel_values_z[i] + vel_values_z[i + 1])/2

# printing total displacement
total_distance_x = sum(dist_values_x)
total_distance_y = sum(dist_values_y)
total_distance_z = sum(dist_values_z)
total_distance = sqrt(total_distance_x**2 + total_distance_y**2 + total_distance_z**2)

print("Total displacement in the x-axis: " + str(total_distance_x) + " m")
print("Total displacement in the y-axis: " + str(total_distance_y) + " m")
print("Total displacement in the z-axis: " + str(total_distance_z) + " m")
print("Total displacement magnitude: " + str(total_distance) + " m")

# plotting results
plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=3) 
plot2 = plt.subplot2grid((3, 3), (1, 0), colspan=3) 
plot3 = plt.subplot2grid((3, 3), (2, 0), colspan=3)

plot1.plot(time_array, accel_values_x, label = 'X')
plot1.plot(time_array, accel_values_y, label = 'Y')
plot1.plot(time_array, accel_values_z, label = 'Z')
plot1.set_title("Acceleration")
plot1.set_ylabel("Acceleration (m/s^2)")
plot1.legend()

plot2.plot(time_array, vel_values_x, label = 'X')
plot2.plot(time_array, vel_values_y, label = 'Y')
plot2.plot(time_array, vel_values_z, label = 'Z')
plot2.set_title("Velocity")
plot2.set_ylabel("Velocity (m/s)")
plot2.legend()

plot3.plot(time_array, dist_values_x, label = 'X')
plot3.plot(time_array, dist_values_y, label = 'Y')
plot3.plot(time_array, dist_values_z, label = 'Z')
plot3.set_title("Displacement")
plot3.set_xlabel("Time (s)")
plot3.set_ylabel("Displacement (m)")
plot3.legend()

plt.tight_layout() 
plt.show()