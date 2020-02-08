#!/usr/bin/python
# -*- coding: utf-8 -*-

# IMU exercise
# Copyright (c) 2015-2020 Kjeld Jensen kjen@mmmi.sdu.dk kj@kjen.dk

##### Insert initialize code below ###################

## Uncomment the file to read ##
fileName = 'imu_razor_data_static.txt'
# fileName = 'imu_razor_data_pitch_55deg.txt'
# fileName = 'imu_razor_data_roll_65deg.txt'
# fileName = 'imu_razor_data_yaw_90deg.txt'

## IMU type
#imuType = 'vectornav_vn100'
imuType = 'sparkfun_razor'

## Variables for plotting ##
showPlot = True
plotData = []
unfilteredData = []
filteredData =[]
angxData=[]
angyData=[]
angzData=[]

## Initialize your variables here ##
myValue = 0.0






######################################################

# import libraries
from math import pi, sqrt, atan2
import matplotlib.pyplot as plt

# open the imu data file
f = open (fileName, "r")

# initialize variables
count = 0

# looping through file
filtered = 0.0
angz = 0.0
angx=0.0
angy=0.0

vxacc = 0.0
vyacc = 0.0
vzacc = 0.0
mycount = 0

for line in f:
	count += 1

	# split the line into CSV formatted data
	line = line.replace ('*',',') # make the checkum another csv value
	csv = line.split(',')

	# keep track of the timestamps 
	ts_recv = float(csv[0])
	if count == 1: 
		ts_now = ts_recv # only the first time
	ts_prev = ts_now
	ts_now = ts_recv

	if imuType == 'sparkfun_razor':
		# import data from a SparkFun Razor IMU (SDU firmware)
		acc_x = int(csv[2]) / 1000.0 * 4 * 9.82;
		acc_y = int(csv[3]) / 1000.0 * 4 * 9.82;
		acc_z = int(csv[4]) / 1000.0 * 4 * 9.82;
		gyro_x = int(csv[5]) * 1/14.375 * pi/180.0;
		gyro_y = int(csv[6]) * 1/14.375 * pi/180.0;
		gyro_z = int(csv[7]) * 1/14.375 * pi/180.0;

	elif imuType == 'vectornav_vn100':
		# import data from a VectorNav VN-100 configured to output $VNQMR
		acc_x = float(csv[9])
		acc_y = float(csv[10])
		acc_z = float(csv[11])
		gyro_x = float(csv[12])
		gyro_y = float(csv[13])
		gyro_z = float(csv[14])
	 		
	##### Insert loop code below #########################

	# Variables available
	# ----------------------------------------------------
	# count		Current number of updates		
	# ts_prev	Time stamp at the previous update
	# ts_now	Time stamp at this update
	# acc_x		Acceleration measured along the x axis
	# acc_y		Acceleration measured along the y axis
	# acc_z		Acceleration measured along the z axis
	# gyro_x	Angular velocity measured about the x axis
	# gyro_y	Angular velocity measured about the y axis
	# gyro_z	Angular velocity measured about the z axis

	## Insert your code here ##
	
	# 3.2.1
	# myValue = atan2(acc_y,sqrt(acc_x*acc_x + acc_z*acc_z)) # relevant for the first exercise, then change this.

	# 3.2.2
	# myValue = atan2(-acc_x, acc_z)

	# 3.2.3
	# myPitch = atan2(acc_y,sqrt(acc_x*acc_x + acc_z*acc_z))
	# myRoll = atan2(-acc_x, acc_z)
	
	# plotData.append(myPitch*180.0/pi)
	# plotData.append(myRoll*180.0/pi)

	# 3.2.4
	# myPitch = atan2(acc_y,sqrt(acc_x*acc_x + acc_z*acc_z)) # relevant for the first exercise, then change this.
	# # plotData.append(myPitch*180.0/pi)
	# gain = 0.1
	# filtered = (1-gain)*filtered + gain*myPitch

	# unfilteredData.append(myPitch*180.0/pi)
	# filteredData.append(filtered*180.0/pi)

	# 3.3.1
	dt = ts_now - ts_prev
	angz = angz + dt*gyro_z
	angzData.append(angz*180.0/pi)
	angx = angx + dt*gyro_x
	angxData.append(angx*180.0/pi)
	angy = angy + dt*gyro_y
	angyData.append(angy*180.0/pi)

	# get drifts
	vxacc += gyro_x
	vyacc += gyro_y
	vzacc += gyro_z
	mycount += 1

	# in order to show a plot use this function to append your value to a list:
	# plotData.append (myValue*180.0/pi)

	######################################################

# closing the file	
f.close()

velxdrift=vxacc/mycount
velydrift=vyacc/mycount
velzdrift=vzacc/mycount
print("velxdrift: " + str(velxdrift))
print("velydrift: " + str(velydrift))
print("velzdrift: " + str(velzdrift))

# show the plot
if showPlot == True:
	# plt.plot(unfilteredData)
	# plt.plot(filteredData)
	# plt.plot(plotData)
	# plt.plot(rollData)
	# plt.plot(pitchData)
	# plt.plot(yawData)
	plt.savefig('imu_exercise_plot.png')
	plt.show()


