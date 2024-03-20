import numpy as np
from functools import reduce
from math import sqrt

# initializing values
delta_t = 0.087 # measurements taken every 87 ms
accel_hex_x = ["E307", "2308", "F107", "F707", "EF07", "1208", "8607", "E307", "CD07", "EF07", "9107", "AE07", "1A08", "0D08", "F507", "E507", "0F08", "EB07", "0208", "FE07", "AC07", "F007", "3B08", "1C08", "D807"]
accel_hex_y = ['3800', '4E01', '9201', 'DC01', 'CB01', 'AA01', '6101', '3901', '2E01', 'BF01', '5C01', 'BA01', 'A501', '9510', 'C401', 'B701', 'F301', '3C02', '4E02', '9701', '7601', '5802', '3402', '1F02', 'DF01']
accel_hex_z = ['290E', 'E20D', '050E', 'CF0D', 'F20D', 'E30D', '4F0E', '0C0E', '2D0E', 'F60D', '2D0E', '3C0E', '0E0E', '190E', '1D0E', '000E', 'E70D', 'EF0D', 'F00D', '130E', '140E', 'E50D', 'DD0D', 'EF0D', 'F70D']

accel_dec_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
accel_dec_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
accel_dec_z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(accel_hex_x)):
    accel_dec_x[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in accel_hex_x[i]])
    accel_dec_y[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in accel_hex_y[i]])
    accel_dec_z[i] = reduce(lambda x, y: x*16 + y, [int(char, 16) for char in accel_hex_z[i]])

accel_decimal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(accel_hex_x)):
    accel_decimal[i] = sqrt((accel_dec_x[i])**2+ (accel_dec_y[i])**2 + (accel_dec_z[i])**2) # magnitude of each acceleration vector

# converting accelerations to m/s^2
lsb_matrix = [16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384, 16384] # LSB/g
accel_g = np.divide(accel_decimal,lsb_matrix) # in g
accel_values = 9.81*accel_g # in m/s^2

#print(accel_values)

# integrating into velocity
vel_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(accel_values) - 1):
    vel_values[i + 1] = delta_t*(accel_values[i] + accel_values[i + 1])/2

#print(vel_values)

# integrating into distance
dist_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(accel_values) - 1):
    dist_values[i + 1] = delta_t*(vel_values[i] + vel_values[i + 1])/2
'''
print(dist_values)

total_distance = sum(dist_values) #in m

print("Total distance travelled: " + str(total_distance) + " m")
'''

# different way
accel_g_x = np.divide(accel_dec_x,lsb_matrix) # in g
accel_g_y = np.divide(accel_dec_y,lsb_matrix)
accel_g_z = np.divide(accel_dec_z,lsb_matrix)

accel_values_x = 9.81*accel_g_x # in m/s^2
accel_values_y = 9.81*accel_g_y
accel_values_z = 9.81*accel_g_z

vel_values_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vel_values_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vel_values_z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(accel_values_x) - 1):
    vel_values_x[i + 1] = delta_t*(accel_values_x[i] + accel_values_x[i + 1])/2
    vel_values_y[i + 1] = delta_t*(accel_values_y[i] + accel_values_y[i + 1])/2
    vel_values_z[i + 1] = delta_t*(accel_values_z[i] + accel_values_z[i + 1])/2

dist_values_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dist_values_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
dist_values_z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(accel_values_x) - 1):
    dist_values_x[i + 1] = delta_t*(vel_values_x[i] + vel_values_x[i + 1])/2
    dist_values_y[i + 1] = delta_t*(vel_values_y[i] + vel_values_y[i + 1])/2
    dist_values_z[i + 1] = delta_t*(vel_values_z[i] + vel_values_z[i + 1])/2

total_distance = sqrt(sum(dist_values_x)**2 + sum(dist_values_y)**2 + sum(dist_values_z)**2)

print("Acceleration in x measured in g:")
print(accel_g_x)
print("Acceleration in x-axis:")
print(accel_values_x)
print("Velocity in x-axis:")
print(vel_values_x)
print("Distance in x-axis:")
print(dist_values_x)
print("Total distance: " + str(total_distance))