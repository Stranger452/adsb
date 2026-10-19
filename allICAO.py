#!/usr/bin/env python3
import time
import threading
from ADSB_Encoder import *
files = [{'csv':'generated/allICAO-0.csv', 'out':'allICAO-0.iq8s'},{'csv':'generated/allICAO-1.csv', 'out':'allICAO-1.iq8s'}]
for file in files:
    t = threading.Thread(target=threadingCSV, args=(file,))
    t.start()
    print(file)
    time.sleep(1)
