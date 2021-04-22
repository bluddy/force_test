import argparse
import sys, time, math
import os.path as path
import cv2
import numpy as np

import serial
import pandas as pd
import struct

cur_dir = path.dirname(path.abspath(__file__))

def main(args):
    
    d = {'time': [], 'voltage': []}

    ser = serial.Serial(port, 9600)
    print("sleeping for 2 seconds after serial port has opened")
    time.sleep(2)

    try:
        while True:
            bytes = ser.read(4 + 2) # 32-bit unsigned int + 16-bit int
            (time, voltage) = struct.unpack('Ih', bytes)
            d['time'].append(time)
            d['voltage'].append(voltage)
    except:
        raise
    finally:
        df = pd.DataFrame(data=d)
        df.to_csv('args.out')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='./output.csv', help='Output file')
    args = parser.parse_args()

    main(args)
