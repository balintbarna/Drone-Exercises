from data_reader.data_reader import data_loader
import failure_detection
import data_reader.paths as paths
import matplotlib.pyplot as plt

def main():
    # load accel data
    acceleration = data_loader(paths.SENSOR_COMBINED,debug = True)
    acceleration.loadCSV_accel()
    
    # read trigger data
    trigger = data_loader(paths.MANUAL_CONTROLLED_SETPOINT,debug = True)
    trigger.loadCSV_para()

    # read velocity data
    vel = data_loader(paths.VELOCITY,debug=True)
    vel.loadVelocity_data()

    # detect failure
    failure_time = failure_detection.freefall_detect(acceleration.Accelerometer_total, acceleration.TimestampS, 10)
    # plot
    fig, ax = plt.subplots()
    # acceleration plot:
    ax.plot(acceleration.TimestampS, acceleration.Accelerometer_total, linewidth=0.5, label='accel_total')
    # parachute trigger plot:
    ax.plot(trigger.ParaTimestampS, trigger.ParaTriggerS, linewidth=1, label='para_trigger')
    # mark detected failure
    plt.axvline(x=failure_time, color='red')
    # plot settings
    # ax.set(xlabel='time (s)', ylabel='Velocity (m/s)', title='Data Plot of Test 9')
    legend = ax.legend(loc='best', shadow=True, fontsize='medium')
    ax.grid()
    plt.show()


if __name__ == "__main__":
    main()

