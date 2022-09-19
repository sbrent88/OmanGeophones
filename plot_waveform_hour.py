import matplotlib.pyplot as plt
import numpy as np
import obspy
#from hydrophone_data_processing import plotting
import plot
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

inv = obspy.read_inventory("7F.OmanDP.PIC.2020127.xml",format="STATIONXML")


chan = 'GHZ'
statlist = [ 'A19' ,'A04' , 'A07' , 'A17' , 'B11' , 'B15' , 'B04' ]
#statlist = [ 'A01' ,'A03' , 'A05' , 'A07' , 'A09' , 'A11' , 'A13' , 'A15' , 'A17' , 'A19' ]
day_list = ['10','11','12', '13', '14', '15', '16', '17', '18', '19', '20','21', '22', '23', '24', '25', '26', '27', '28', '29','30', '31','32']
day = 10	
hr = 13

#data = [tr.data for tr in stream]
start_time = obspy.UTCDateTime('2020-1-' + str(day) + 'T00:00:00')
#print(start_time)

stream = obspy.read("/media/sbrent/Oman3/PASSCAL/Main_deployment/DAYS/" +statlist[0]+ "/*.." + chan +".2020.0" +str(day))

for s in statlist[1:]:
    
    stream += obspy.read("/media/sbrent/Oman3/PASSCAL/Main_deployment/DAYS/" + s + "/*.." + chan + ".2020.0" + str(day))


stream_snapshot = stream.slice(starttime=start_time+hr*3600,endtime=start_time+(hr+1)*3600)

#plotting.plot_waveforms(stream_snapshot, color='dodgerblue')

plot.plot_wave(stream_snapshot, color='dodgerblue')

plt.show()
