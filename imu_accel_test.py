import numpy as np
from functools import reduce

# initializing values
delta_t = 0.08677 # measurements taken every 17 ms
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


print(accel_dec_x)

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
