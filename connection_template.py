##DEPENDENCIES

from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException
import time
import socket
import exceptions
import math
import argparse

##FUNCTIONS

def connectMyCopter():

	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()

	connection_string = args.connect

	##For dronekt-sitl
	##We don't need to put 127.0.. to launch
	if not connection_string:
		import dronekit_sitl
		sitl = dronekit_sitl.start_default()
		connection_string = sitl.connection_string()

	vehicle = connect(connection_string,wait_ready=True)

	return vehicle

##>>python connection_template.py --connect 127.0.0.1:14550
##MAIN EXECUTABLE

vehicle = connectMyCopter()
