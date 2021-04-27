import argparse
import sys, time, math
import os.path as path
import cv2
import numpy as np

import time
import serial
#import pandas as pd
import struct
import csv

cur_dir = path.dirname(path.abspath(__file__))

def get_portname():
    import platform
    if platform.system() == 'Linux':
        import glob
        # Note: if you get a permission error, you might need to add yourself to the dialout group:
        # sudo adduser name dialout
        # reboot for it to take effect
        # TODO: switch to more robust list_ports
        port_l = glob.glob('/dev/ttyUSB*')
        if len(port_l) == 0:
            port_l = glob.glob('/dev/ttyACM*')
            if len(port_l) == 0:
                print("No serial port found for Arduino")
                sys.exit(1)
        port = port_l[0]
    else:
        port = 'COM4'
    return port

def main(args):

    time_l = []
    voltage_l = []

    ser = serial.Serial(get_portname(), 115200)
    print("Connected!")
    time.sleep(1)

    ser.write(b'\x00\x00') # start process
    ser.write(b'\x01\x01') # start process
    print("Recording voltages")

    try:
        while True:
            bytes = ser.read(4 + 2) # 32-bit unsigned int + 16-bit int
            (t, v) = struct.unpack('Ih', bytes)
            #print(t, v)
            time_l.append(t)
            voltage_l.append(v)
    except:
        raise
    finally:
        print(f"Dumping to {args.out}")

        ser.write(b'\x00\x00') # stop process
        with open(args.out, 'w') as csv_f:
            writer = csv.writer(csv_f, delimiter=',')
            for i, t in enumerate(time_l):
                #print(i, t)
                writer.writerow((t, voltage_l[i]))

        #df = pd.DataFrame(data=d)
        #df.to_csv(args.out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='./output.csv', help='Output file')
    args = parser.parse_args()

    main(args)
