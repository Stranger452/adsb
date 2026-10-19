import os

# os.system('python /home/irtaza/Downloads/ADSB-Out-master/ADSB_Encoder.py')
os.system('hackrf_transfer -t /home/irtaza/Downloads/ADSB-Out-master/Samples_256K.iq8s -f 1090000000 -s 2000000 -x 10')