import obspy
import obspy.signal.trigger as trigger
import matplotlib.pyplot as plt
import numpy as np
from hydrophone_data_processing import plotting
import plot_working

#from hydrophone_data_processing import load, preprocessing, tempmatch, useful_variables, plotting
from matplotlib.dates import num2date
#import event_times as iet
import itertools

#class Event_Processing:

#def __init__(self)



def get_event_window_raw(data, event_time):
    """
    gets data around event with lead time and follow times 
    defined by the start_window_edge and end_window_edge
    
    The edges are in units of seconds
    """
    start_window_edge = -0.2
    end_window_edge = 0.3
    starttime = event_time + start_window_edge
    endtime = event_time + end_window_edge
    return data.slice(starttime=starttime, endtime=endtime)



def aic_pick_t1(events):

    #calculate the aic score
    aic_score = [trigger.aic_simple(tr.data) for tr in events]

    #find maxima and returns index of aic scores
    aic_t_idx = [aic.argmin() for aic in aic_score]

    #use maxima index to find timestamp
    aic_time = [events[n].times('matplotlib')[i] for n,i in enumerate(aic_t_idx)]

    return aic_time, aic_score



def get_waveforms_window(data, starttime):
    """
    Returns a 1 second long trimmed event for the starttime and endtime

    Applies hanning window to edges to smooth to zero.
    Parameters
    -----------------
    starttime : obspy.UTCDatetime
        starttime for the event
    Returns
    -----------------
    data : obspy.Stream
        trimmed waveforms for 1 second event window
    """
    starttime = starttime - 0.1
    print(starttime)
    endtime = starttime + 0.9
    print(endtime)
    trimmed = data.copy().trim(starttime=starttime, endtime=endtime)
    trimmed.taper(type='hann', max_percentage=0.5)
    return trimmed




def aic_pick(event):
        """
        Uses obspy aic_simple to pick the start time of an event
        Parameters
        --------------------
        event : obspy.Stream
            an obspy stream with traces inside. the expected data
            will be only for a single event, not the whole data set
        Returns
        --------------------
        aic_t : list
            the times per geophone for each aic picked event
        aics : list
            the raw aics calculated for each event
        """

        # calculates aic score
        aics = [trigger.aic_simple(tr.data) for tr in event]

        # finds minimum and returns index for aic scores
        # aic_t_idx = [aic.argmin() for aic in aics]
        # diffs = [np.diff(aic) for aic in aics]
        # diffs = [np.diff(aic, n=20) for aic in aics]
        diffs = [np.diff(aic, n=1) for aic in aics]
        maxes = [np.argmax(diff) for diff in diffs]
        
        # print(maxes)

        # uses minimum index to retrieve the timestamp
        aic_t = [event[n].times('matplotlib')[i] for n, i in enumerate(maxes)]

        return aic_t, aics



    
    
def plot_waveforms_with_aic(event,aics,aic_t):
    
    #axes_id = dict(np.array([['7F.A01..BHZ' ,'7F.A02..BHZ' , '7F.A03..BHZ' , '7F.A04..BHZ' , '7F.A05..BHZ' , '7F.A06..BHZ' , '7F.A07..BHZ' , '7F.A08..BHZ' , '7F.A09..BHZ'  , '7F.A10..BHZ' , '7F.A11..BHZ', '7F.A13..BHZ', '7F.A14..BHZ', '7F.A19..BHZ'],[0,1,2,3,4,5,6,7,8,9,10,11,12,13], ]).transpose())


    fig, axes = plot_working.plot_wave_autoscale(event, color='blue')
    for n, ax in enumerate(axes):
        ax2 = ax.twinx()
        t = event[n].times('matplotlib')
        aic = aics[n]
        ax2.plot(t, aic, color='green')
        ax.plot((aic_t[n], aic_t[n]), (-10000, 10000), color='red')
        #ax[n].text(1, 10000, list(axes_id.keys())[n])
    return fig, axes








if __name__=='__main__':
    print("WOOHOOO")
    