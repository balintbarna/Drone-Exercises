from data_reader.data_reader import data_loader
from failure_detection import *
import data_reader.paths as paths

def main():
    # load accel data
    reader = data_loader(paths.SENSOR_COMBINED,debug = True)
    reader.loadCSV_accel()
    freefall_detect(reader.Accelerometer_total, reader.TimestampS)

    # read velocity data
    vel = data_loader(paths.VELOCITY,debug=True)
    vel.loadVelocity_data()


if __name__ == "__main__":
    main()

