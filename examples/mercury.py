

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
    # commenta
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

            if (angle < limit) and (angle > (limit-45)):

                sector = np.append(sector, angle)
                print("sector")
                print(sector)
                print("limit")
                print(limit)

            else:
                sector_avg = np.average(sector)
                limit = limit + 45
                sector = []
                bounds[count] = sector_avg
                count = count+1
            if limit >= 360:
                limit = 45
                count = 0

            print(bounds)



            '''
            else:
                print(sector)
                sector_avg = np.average(sector)
                limit = limit + 45
                sector = np.zeros(1)
            
            if sector_avg < distance_warning:
                bounds[(limit - 90) / 45] = 1
                '''





    except KeyboardInterrupt:
        print('Stoping.')
        lidar.stop()
        lidar.stop()
        lidar.disconnect()


if __name__ == '__main__':
    run(sys.argv[1])
