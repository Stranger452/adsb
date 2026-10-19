#!/usr/bin/env python3
import time
import threading
from ADSB_Encoder import *
files = [{'csv':'generated/allLat-0.csv', 'out':'allLat-0.iq8s'},{'csv':'generated/allLat-1.csv', 'out':'allLat-1.iq8s'},{'csv':'generated/allLat-2.csv', 'out':'allLat-2.iq8s'},{'csv':'generated/allLat-3.csv', 'out':'allLat-3.iq8s'}]
for file in files:
    t = threading.Thread(target=threadingCSV, args=(file,))
    t.start()
    print(file)
    time.sleep(1)
