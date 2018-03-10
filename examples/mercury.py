

#!/usr/bin/env python3
'''Records scans to a given file in the form of numpy array.
Usage example:

$ mercury.py 0 '
$ mercury.py 1 '
where 0 is the dev/ttyUSB0'''

import sys
import numpy as np
from rplidar import RPLidar



def run(usb):
    '''Main function'''
    PORT_NAME = '/dev/ttyUSB'
    PORT_NAME = PORT_NAME + str(usb)
    lidar = RPLidar(PORT_NAME)
    limit = 45.0
    sector = []
    bounds = np.zeros(8)
    count = 0
    start = 0

    try:
        print('Recording measurments... Press Crl+C to stop.')

        for measurment in lidar.iter_measurments():

            one_scan = np.asarray(measurment)



            sector_avg = 6000
            distance_warning = .4

            dist = one_scan[3]
            angle = float(one_scan[2])
            print("angle")
            print(angle)

            if (angle < limit):

                sector = np.append(sector, angle)
                print("sector")
                print(sector)
                print("limit")
                print(limit)
                start = 1

            else:
                if start ==1:
                    sector_avg = np.average(sector)
                    limit = limit + 45
                    sector = []
                    bounds[count] = sector_avg
                    count = count+1

            if limit >= 360:
                limit = 45
                count = 0

            #print(bounds)









    except KeyboardInterrupt:
        print('Stoping.')
        lidar.stop()
        lidar.stop()
        lidar.disconnect()


if __name__ == '__main__':
    run(sys.argv[1])
