

#!/usr/bin/env python3
'''Records scans to a given file in the form of numpy array.
Usage example:

$ ./record_scans.py out.npy'''
import sys
import numpy as np
from rplidar import RPLidar



def run(usb):
    '''Main function'''
    PORT_NAME = '/dev/ttyUSB'
    PORT_NAME = PORT_NAME + str(usb)
    lidar = RPLidar(PORT_NAME)
    data = []
    limit = 45
    sector = np.zeros(1)
    # commenta
    try:
        print('Recording measurments... Press Crl+C to stop.')

        for measurment in lidar.iter_measurments():

            one_scan = np.asarray(measurment)
            print(one_scan)

            bounds = np.zeros(8)
            sector_avg = 6000
            distance_warning = .4

            dist = one_scan[3]
            angle = float(one_scan[2])
            print(dist, angle)

            if angle < limit:
                sector = np.append(sector,dist)

            else:
                print(sector)
                sector_avg = np.average(sector)
                limit = limit + 45
                sector = np.zeros(1)
            '''
            if sector_avg < distance_warning:
                bounds[(limit - 90) / 45] = 1
                '''





    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()


if __name__ == '__main__':
    run(sys.argv[1])
