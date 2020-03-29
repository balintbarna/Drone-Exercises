#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
2019-03-27 VKT Version 1.0: Document created
2020-03-13 VKT Version 1.1: Converted to python3
"""
"""
Description:
    Simple example python class for loading data from csv files and plotting data.
License: BSD 3-Clause
"""

### Import start
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, pow
### Import end

### Class start
class data_loader():
    def __init__(self, inFileName, debug = False):
        self.fileName = inFileName

        # Prepare containers for the data
        self.TimestampS = []
        self.AccelerometerXS = []
        self.AccelerometerYS = []
        self.AccelerometerZS = []
        self.Accelerometer_total=[]

        self.ParaTimestampS = []
        self.ParaTriggerS = []

        self.velocity_timestamps=[]
        self.velocity_ground=[]
        self.velocity_down=[]

        self.attitude_time=[]
        self.attitude=[]

        # remember to add class definitions for variables

        # Print debug value
        self.debugText = debug

    def loadCSV_para(self):
        with open(self.fileName) as csvfile:
            if self.debugText:
                print ('Data file opened, attempting data load')
            readCSV = csv.DictReader(csvfile, delimiter=',')

            for row in readCSV:
                ParaTimestampS = float(row['timestamp'])/1000000
                self.ParaTimestampS.append(ParaTimestampS)
                ParaTrigger = float(row['aux1']) * 20
                self.ParaTriggerS.append(ParaTrigger)

            if self.debugText:
                print ('Data loaded')

    def loadCSV_accel(self):
        with open(self.fileName) as csvfile:
            if self.debugText:
                print ('Data file opened, attempting data load')
            readCSV = csv.DictReader(csvfile, delimiter=',')

            for row in readCSV:
                TimestampS = float(row['timestamp'])/1000000
                self.TimestampS.append(TimestampS)
                AccelerometerX = float(row['accelerometer_m_s2[0]'])
                self.AccelerometerXS.append(AccelerometerX)
                AccelerometerY = float(row['accelerometer_m_s2[1]'])
                self.AccelerometerYS.append(AccelerometerY)
                AccelerometerZ = float(row['accelerometer_m_s2[2]'])
                self.AccelerometerZS.append(AccelerometerZ)
                acc_total=sqrt(AccelerometerX*AccelerometerX + AccelerometerY*AccelerometerY 
                + AccelerometerZ*AccelerometerZ)
                self.Accelerometer_total.append(acc_total)

            if self.debugText:
                print ('Data loaded')

    # Extend class with more methods for loading different kind of csv files..
    # e.g loading 'TEST9_08-02-19_telemetry_status_0.csv':
    #
    def loadCSV_telemetry_status(self):
        with open(self.fileName) as csvfile:
            if self.debugText:
               print('Data file opened, attempting data load')
            readCSV = csv.DictReader(csvfile, delimiter=',')
            for row in readCSV:
                TelemTimestampS = float(row['timestamp'])/1000000
                self.TelemTimestampS.append(ParaTimestampS)
                RXerrors = float(row['rxerrors'])
                self.RXerrorsS.append(RXerrors)
            if self.debugText:
                print ('Data loaded')
    #
    # (...)
    def loadVelocity_data(self):
        with open(self.fileName) as csvfile:
            if self.debugText:
                print('Data file opened, attempting data load')
            readCSV = csv.DictReader(csvfile, delimiter=',')
            for row in readCSV:
                TimestampS=float(row['timestamp'])/1000000
                self.velocity_timestamps.append(TimestampS)
                vel_gnd=float(row['vel_m_s'])
                self.velocity_ground.append(vel_gnd)
                vel_down=float(row['vel_d_m_s'])
                self.velocity_down.append(vel_down)

            if self.debugText:
                print ('Data loaded')

    def loadCSV_attitude(self):
        with open(self.fileName) as csvfile:
            if self.debugText:
                print('Data file opened, attempting data load')
            readCSV = csv.DictReader(csvfile, delimiter=',')
            for row in readCSV:
                TimestampS=float(row['timestamp'])/1000000
                self.attitude_time.append(TimestampS)
                att=(float(row['q[0]']),float(row['q[1]']),float(row['q[2]']),float(row['q[3]']))
                self.attitude.append(att)

### Class end - Main start

if __name__ == '__main__':

    SENSOR_COMBINED = '../csv_files/TEST9_08-02-19/TEST9_08-02-19_sensor_combined_0.csv'
    #SENSOR_COMBINED = '../csv_files/TEST5_30-01-19/TEST5_30-01-19_sensor_combined_0.csv'
    MANUAL_CONTROLLED_SETPOINT = '../csv_files/TEST9_08-02-19/TEST9_08-02-19_manual_control_setpoint_0.csv'

    # Initialize and load data
    reader = data_loader(
        SENSOR_COMBINED,
        debug = True
    )
    reader.loadCSV_accel()

    trigger = data_loader(
        MANUAL_CONTROLLED_SETPOINT,
        debug = True
    )
    trigger.loadCSV_para()

    # Add readers for the additional files you want to load...
    vel=data_loader('../csv_files/TEST9_08-02-19/TEST9_08-02-19_vehicle_gps_position_0.csv'
    ,debug=True)
    vel.loadVelocity_data()

    #Attitude plotting
    att=data_loader('../csv_files/TEST9_08-02-19/TEST9_08-02-19_vehicle_attitude_0.csv'
    ,debug=True)
    att.loadCSV_attitude()
    # Here you can add the analysis of the different parameters and create boolean variables that triggers upon failure detection.
    # You can likewise plot these failure detection parameters (with the same timestamp as the investigated dataset) together with the logged data.

    fig, ax = plt.subplots()

    # acceleration plot:
    #ax.plot(reader.TimestampS, reader.AccelerometerXS, linewidth=0.5, label='accel_x')
    #ax.plot(reader.TimestampS, reader.AccelerometerYS, linewidth=0.5, label='accel_y')
    #ax.plot(reader.TimestampS, reader.AccelerometerZS, linewidth=0.5, label='accel_z')
    #ax.plot(reader.TimestampS, reader.Accelerometer_total, linewidth=0.5, label='accel_total')
    # parachute trigger plot:
    #ax.plot(trigger.ParaTimestampS, trigger.ParaTriggerS, linewidth=1, label='para_trigger')

    # Add more plots or create new plots for additional data loaded...
    ax.plot(vel.velocity_timestamps,vel.velocity_ground,linewidth=0.5, label='Ground_vel')
    ax.plot(vel.velocity_timestamps,vel.velocity_down,linewidth=0.5, label='Down_vel')
    #ax.plot(att.attitude_time,att.attitude,linewidth=0.5, label='Attitude')
    # plot settings
    ax.set(xlabel='time (s)', ylabel='Velocity (m/s)',
       title='Data Plot of Test 9')
    legend = ax.legend(loc='best', shadow=True, fontsize='medium')
    ax.grid()
    plt.show()

### Main end