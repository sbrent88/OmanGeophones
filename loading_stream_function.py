import os
import sys
sys.path.append(os.getcwd())

import glob
import obspy



def import_data_one_day(station_list, day_id):
    day = []

    for s in station_list:

        dir = '/media/sbrent/Oman3/PASSCAL/Main_deployment/DAYS/{s}/{s}.7F..GHZ.2020.*'.format(s=s)

        d = glob.glob(dir)
        
        day.append(d)


    path = day[0][day_id]
    stream = obspy.read(path)
    for index in range(1,len(day)):
        path = day[index][day_id]
        stream = stream + obspy.read(path)
    #print(len(stream))
    print(stream)
    return stream




if __name__=='__main__':
    stat_list = [ 'A19' ,'A04' , 'A07' , 'A17' , 'B11' , 'B15' , 'B04' ]
    
    st = import_data_one_day(stat_list,10)
    
    hr = 20
    start_time = obspy.UTCDateTime('2020-1-' + str(10) + 'T00:00:00')
    stream_snapshot = st.slice(starttime=start_time+hr*3600,endtime=start_time+(hr+1)*3600)
    print(stream_snapshot)
    #print('Nothing to see here. You may go about your business.')
