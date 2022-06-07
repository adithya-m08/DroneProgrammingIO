#import libraries
from dronekit import *
import time
import cv2
cap = cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()

#connect to vehicle
vehicle = connect('127.0.0.1:14551',baud=921600,wait_ready=True)

#takeoff function
def arm_takeoff(height):
    #check if drone is ready
    while not vehicle.is_armable:
        print("waiting for drone")
        time.sleep(1)

    #change mode and arm
    print("arming")
    vehicle.mode=VehicleMode('GUIDED')
    vehicle.armed=True
    
    #check if drone is armed
    while not vehicle.armed:
        print("Waiting for arm")
        time.sleep(1)

    #takeoff
    print("takeoff")
    vehicle.simple_takeoff(height)

    #report values back every 1s and finally break out
    while True:
        print('Reached ',vehicle.location.global_relative_frame.alt)
        if(vehicle.location.global_relative_frame.alt>=height*0.95):
            print("Reached Target Altitude")
            break
        time.sleep(1)

while True:
    _,image=cap.read()
    cv2.imshow('Video',image)
    res,_,_=detector.detectAndDecode(image)
    if res:
        print(res)
        if res=='1':
            arm_takeoff(10)
        elif res=='2':
            vehicle.mode=VehicleMode('RTL')
            time.sleep(10)
            vehicle.close()
            cv2.destroyAllWindows()
    cv2.waitKey(1)
