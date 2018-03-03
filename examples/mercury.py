

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
    # commenta
    try:
        print('Recording measurments... Press Crl+C to stop.')
        iterator = lidar.iter_scans()

        print (iterator)
        '''
        iterator = np.asarray(iterator)
        print(iterator)

        n, m = np.size(iterator)
        sector = np.zeros(1)
        bounds = np.zeros(8)
        sector_avg = 6
        distance_warning = .4
        for lecture in range(0, n-1):

            one_scan = iterator[lecture,:]
            dist = one_scan[2]
            angle = one_scan[1]
            if angle < limit:
                sector = np.append(dist)
            else:
                sector_avg = np.avg(sector)
                limit = limit + 45

            if sector_avg < distance_warning:
                bounds[(limit-90)/45] = 1
        '''
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    np.save(path, np.array(data))

if __name__ == '__main__':
    run(sys.argv[1])
