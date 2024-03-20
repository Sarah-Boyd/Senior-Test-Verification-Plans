# Welcome to the IMU gyroscope test script! Note that integration methods were taken from https://makersportal.com/blog/calibration-of-an-inertial-measurement-unit-imu-with-raspberry-pi-part-ii
# To proceed, please replace the following variables: 
#   delta_t: the time difference between measurements, in seconds
#   vel_hex_x: hexadecimal values of the x-axis angular velocity readings
#   vel_hex_y: hexadecimal values of the y-axis angular velocity readings
#   vel_hex_z: hexadecimal values of the z-axis angular velocity readings
#   lsb_value: sensitivity in LSB/dps, where LSB = Least Significant Bit and dps = degrees per second

import numpy as np
from functools import reduce
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt

# initializing values
delta_t = 0.087 # measurements taken every 87 ms
vel_hex_x = ['8201', 'F700', 'DA00', '2001', '6E01', '9801', 'FF01', '0102', 'EC01', 'C001', 'D301', '1902', 'C002', 'FFFF', 'B302', '0D02', '6B01', '4901', '5101', '7501', '8D01', 'E101', 'D601', 'FFFF', 'C401', 'A301', 'FFFF', '1B01', '0801', '0001', 'EB00', 'E900', '0F01', '0201', 'D700', 'D900', 'E600', '4700', '6400', '7B00', '3A00', '0600', 'EFFF', 'FBFF', '0A00', '0400', '0000']
vel_hex_y = ['9900', 'D100', '6B00', '2000', '2700', '6F00', 'E400', '5A00', '4A00', '6400', 'D200', 'B800', '5400', 'FFFF', '8B00', '7E00', '7C00', '8400', '0B00', 'F2FF', 'FDFF', '7200', 'C400', 'FFFF', '2800', 'F4FF', 'FFFF', 'BA00', 'B400', '2D00', 'A800', 'D500', '9F00', '1900', 'CFFF', 'B8FF', '84FF', '9000', '4000', 'F8FF', 'D1FF', 'E0FF', '4200', '1F00', 'E6FF', 'EAFF', '0900']
vel_hex_z = ['F402', '4F02', 'D001', '1702', 'A802', '1703', '2304', 'DF03', '9B03', '4D03', '9B03', '2D04', '1705', 'FFFF', '4F05', 'FE03', 'D002', '8802', '7502', 'AF02', 'EB02', '8403', 'A203', 'FFFF', '4303', '0D03', 'FFFF', '5E02', '3902', '1202', '0D02', '1402', '1C02', 'D201', '9301', '9501', '9001', 'FC00', 'D500', 'AE00', '5A00', '0600', 'FFFF', '0300', '0400', '0500', '0200']
lsb_value = 262.144 # LSB/dps

# making arrays of zero
vel_dec_x = np.zeros(len(vel_hex_x))
vel_dec_y = np.zeros(len(vel_hex_x))
vel_dec_z = np.zeros(len(vel_hex_x))

time_array = np.zeros(len(vel_hex_x))
lsb_matrix = np.zeros(len(vel_hex_x))

vel_values_x = np.zeros(len(vel_hex_x))
vel_values_y = np.zeros(len(vel_hex_x))
vel_values_z = np.zeros(len(vel_hex_x))

dist_values_x = np.zeros(len(vel_hex_x))
dist_values_y = np.zeros(len(vel_hex_x))
dist_values_z = np.zeros(len(vel_hex_x))

# filling in time and LSB/g arrays
for i in range(len(time_array)):
    if i > 0:
        time_array[i] = time_array[i - 1] + delta_t

for i in range(len(vel_hex_x)):
    lsb_matrix[i] = lsb_value

# converting angular velocity measurements to dps
for i in range(len(vel_hex_x)): # converting from hexadecimal to decimal
    vel_dec_x[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in vel_hex_x[i]])
    vel_dec_y[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in vel_hex_y[i]])
    vel_dec_z[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in vel_hex_z[i]])

vel_values_x = np.divide(vel_dec_x,lsb_matrix) # in dps (degrees per second)
vel_values_y = np.divide(vel_dec_y,lsb_matrix)
vel_values_z = np.divide(vel_dec_z,lsb_matrix)

# integrating to angular distance travelled (rotation)
for i in range(len(vel_values_x) - 1):
    dist_values_x[i + 1] = delta_t*(vel_values_x[i] + vel_values_x[i + 1])/2
    dist_values_y[i + 1] = delta_t*(vel_values_y[i] + vel_values_y[i + 1])/2
    dist_values_z[i + 1] = delta_t*(vel_values_z[i] + vel_values_z[i + 1])/2

# printing total displacement
total_distance_x = sum(dist_values_x)
total_distance_y = sum(dist_values_y)
total_distance_z = sum(dist_values_z)

print("Total rotation in the x-axis: " + str(total_distance_x) + " degrees")
print("Total rotation in the y-axis: " + str(total_distance_y) + " degrees")
print("Total rotation in the z-axis: " + str(total_distance_z) + " degrees")

# plotting results
plot1 = plt.subplot2grid((2, 2), (0, 0), colspan=2) 
plot2 = plt.subplot2grid((2, 2), (1, 0), colspan=2) 

plot1.plot(time_array, vel_values_x, label = 'X')
plot1.plot(time_array, vel_values_y, label = 'Y')
plot1.plot(time_array, vel_values_z, label = 'Z')
plot1.set_title("Angular Velocity")
plot1.set_ylabel("Angular Velocity (dps)")
plot1.legend()

plot2.plot(time_array, dist_values_x, label = 'X')
plot2.plot(time_array, dist_values_y, label = 'Y')
plot2.plot(time_array, dist_values_z, label = 'Z')
plot2.set_title("Rotation")
plot2.set_xlabel("Time (s)")
plot2.set_ylabel("Rotation (deg)")
plot2.legend()

plt.tight_layout() 
plt.show()