import itertools
from datetime import datetime
import numpy as np

start = datetime.now()


def elapsed_time():
    return datetime.now() - start



def make_geophone_data_paths(stat_list, julian_day):

    path_id = []
   
    for s in stat_list:
        #print(s)
        paths = ['/media/sbrent/Oman3/PASSCAL/Main_deployment/DAYS/{s}/{s}.7F..GHZ.2020.0{julian_day}']
        paths_form = [p.format(s=s, julian_day=julian_day) for p in paths]
        path_id.append(paths_form)
    
    p_id = list(itertools.chain(*path_id))
    return p_id

if __name__=='__main__':
    print('Nothing to see here. You may go about our business.')
    g_id = ['A01','A04']
    mgdp = make_geophone_data_paths(g_id,15)
    print(mgdp)


