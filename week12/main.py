import matplotlib.pyplot as plt
import data_reader.paths as paths
from data_reader.data_reader import data_loader
import failure_detection
import impact_energy

def main():
    # load accel data
    acceleration = data_loader(paths.SENSOR_COMBINED_9,debug = True)
    acceleration.loadCSV_accel()
    
    # read trigger data
    trigger = data_loader(paths.MANUAL_CONTROLLED_SETPOINT_9,debug = True)
    trigger.loadCSV_para()

    # read velocity data
    print_impact_energy(paths.VELOCITY_5)
    print_impact_energy(paths.VELOCITY_8)
    print_impact_energy(paths.VELOCITY_9)

    # plot_acceleration_error(acceleration, trigger)

def print_impact_energy(velocity_path):
    print("calculating impact energy for:")
    print(velocity_path)
    velocity = data_loader(velocity_path)
    velocity.loadVelocity_data()
    print(impact_energy.calculate_impact_energy(velocity))

def plot_down_velocity(velocity: data_loader):
    fig, ax = plt.subplots()
    ax.plot(velocity.velocity_timestamps, velocity.velocity_down, linewidth=0.5, label='down_vel')
    legend = ax.legend(loc='best', shadow=True, fontsize='medium')
    ax.grid()
    plt.show()

def plot_acceleration_error(acceleration: data_loader, trigger: data_loader):

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

