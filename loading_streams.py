import os
import sys
sys.path.append(os.getcwd())

import obspy
import io
import pandas as pd
import glob
import numpy as np



def import_data_for_single_day(paths):

    borehole = paths[0].split('/')[-1].split('.')[0]
 
    julian_day = paths[0].split('/')[-1].split('.')[-1]


    print(borehole)
    print(julian_day)
    
    #file_locs = []
    #for s in [1, 2, 3, 4, 5, 6]:
        
    #dir = '/media/sbrent/Oman3/Hydrophones/DAYS/{b}/{b}.7F..GHZ.2020.{d}'.format(b=borehole, d=julian_day)
    #file_locs.append(dir)

    #stream = get_raw_stream(file_locs)

    return borehole,julian_day



def get_raw_stream(paths):

    stream = obspy.read(paths[0])
    for p in paths[1:]:
        stream = stream + obspy.read(p)
    stream.merge(fill_value='latest')
    return stream













