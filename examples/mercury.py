

#!/usr/bin/env python3
'''Records scans to a given file in the form of numpy array.
Usage example:

$ mercury.py 0 '
$ mercury.py 1 '
where 0 is the dev/ttyUSB0
where 1 is the dev/ttyUSB1
etc
'''

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
            distance_warning = 10 # mm

            dist = one_scan[3]
            angle = float(one_scan[2])


            if (angle < limit+ 10) and (angle > limit - 55):

                sector = np.append(sector, dist)
                start = 1

            else:
                if start ==1:
                    sector_avg = np.average(sector)
                    bounds[(limit / 45) - 1] = sector_avg
                    limit = limit + 45
                    sector = []


                    mask = bounds < distance_warning



                    file = open("testfile.txt", "w")
                    mask_to_write = np.array2string(bounds)
                    file.write(mask_to_write)
                    print(mask_to_write)
                    for i in range(1,10):
                        print('\r', end='')



                    #sys.stdout.write(mask_to_write)

                if limit > 360:
                    limit = 45


    except KeyboardInterrupt:
        print('Stoping.')
        lidar.stop()
        lidar.stop()
        lidar.disconnect()


if __name__ == '__main__':
    run(sys.argv[1])
