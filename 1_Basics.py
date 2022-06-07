#import libraries
from dronekit import *

#connect to vehicle
vehicle = connect('127.0.0.1:14551',baud=921600,wait_ready=True)

#get vehicle mode
print(vehicle.mode)

#check if vehicle is armable
print(vehicle.is_armable)

#check if vehicle is armed
print(vehicle.armed)


if(vehicle.is_armable):
    vehicle.armed=True

print('armed')

#close the vehicle
vehicle.close()
