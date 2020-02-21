####Dependencies###################

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import socket
import exceptions
import argparse

###Function definitions for mission####

##Function to connect script to drone
def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect

    vehicle = connect(connection_string, wait_ready=True)

    return vehicle


vehicle=connectMyCopter()

time.sleep(2)

print("eph: %s"%vehicle.parameters['eph'])
print("epv: %s"%vehicle.parameters['epv'])
print("fix_type: %s"%vehicle.parameters['fix_type'])
print("satellites_visible: %s"%vehicle.parameters['satellites_visible'])

print("End of function")
print("Arducopter version: %s"%vehicle.version)

while True: 
    time.sleep(2)

vehicle.close()
### End of script
