from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plot_working
import event_processing
import loading_stream_function

import matplotlib.ticker as ticker
from datetime import datetime
from datetime import timedelta


def filter_waveforms(data, events, event_id):
    
    data_cp1 = data.copy()

    time = events.time[event_id]

    data_window = event_processing.get_event_window_raw(data_cp1, time)
    data_window = data_window.detrend('demean')

    data_window_cp1 = data_window.copy()
    data_window_cp2 = data_window.copy()
    #data_window_cp3 = data_window.copy()

    data_hp = data_window_cp1.filter(type='highpass', corners = 4, zerophase=True, freq = 350)

    data_bp = data_window_cp2.filter(type='bandpass', freqmin = 100, freqmax = 250)

    return data_window, data_hp, data_bp






def bandpass_50_inc_filter_waveforms(data, events, event_id):
    
    data_cp1 = data.copy()

    time = events.time[event_id]

    data_window = event_processing.get_event_window_raw(data_cp1, time)
    data_window = data_window.detrend('demean')

    data_window_cp1 = data_window.copy()
    data_window_cp2 = data_window.copy()
    data_window_cp3 = data_window.copy()
    data_window_cp4 = data_window.copy()
    data_window_cp5 = data_window.copy()
    data_window_cp6 = data_window.copy()
    #data_window_cp7 = data_window.copy()

    #data_hp = data_window_cp1.filter(type='highpass', corners = 4, zerophase=True, freq = 350)

    data_bp_50_100 = data_window_cp1.filter(type='bandpass', freqmin = 50, freqmax = 100)

    data_bp_100_150 = data_window_cp2.filter(type='bandpass', freqmin = 100, freqmax = 150)

    data_bp_150_200 = data_window_cp3.filter(type='bandpass', freqmin = 150, freqmax = 200)

    data_bp_200_250 = data_window_cp4.filter(type='bandpass', freqmin = 200, freqmax = 250)

    data_bp_250_300 = data_window_cp5.filter(type='bandpass', freqmin = 250, freqmax = 300)

    data_bp_300_350 = data_window_cp6.filter(type='bandpass', freqmin = 300, freqmax = 350)

    data_bp_350_400 = data_window_cp1.filter(type='bandpass', freqmin = 350, freqmax = 400)


    return data_window, data_bp_50_100, data_bp_100_150, data_bp_150_200, data_bp_200_250, data_bp_250_300, data_bp_300_350, data_bp_350_400








def plot_filtered_waveforms(data_window, data_hp, data_bp, events, event_id):

    axes_id = dict(np.array([['7F.A01..BHZ' ,'7F.A02..BHZ' , '7F.A03..BHZ' , '7F.A04..BHZ' , '7F.A05..BHZ' , '7F.A06..BHZ' , '7F.A07..BHZ' , '7F.A08..BHZ' , '7F.A09..BHZ'  , '7F.A10..BHZ' , '7F.A11..BHZ', '7F.A13..BHZ', '7F.A14..BHZ', '7F.A19..BHZ'],[0,1,2,3,4,5,6,7,8,9,10,11,12,13], ]).transpose())

    fig, ax = plt.subplots(14, figsize=(30, 75), sharex=True, sharey=False)

    for id in events.trace_ids.iloc[event_id]:
    
        i = int(axes_id[id])
        #print(id)
        ax[i].plot(data_window[i].times('matplotlib'), data_window[i].data, color='limegreen', label="event_unfiltered")
        ax[i].plot(data_hp[i].times('matplotlib'), data_hp[i].data, 'blue', label = "hp350")
        ax[i].plot(data_bp[i].times('matplotlib'), data_bp[i].data, 'purple', label = "bp100-250")
        ax[i].set_title(id)
        ax[i].legend(loc="upper right")
    return fig, ax 



def plot_unit_var_filtered_waveforms(data_window, data_hp, data_bp, events, event_id):

    axes_id = dict(np.array([['7F.A01..BHZ' ,'7F.A02..BHZ' , '7F.A03..BHZ' , '7F.A04..BHZ' , '7F.A05..BHZ' , '7F.A06..BHZ' , '7F.A07..BHZ' , '7F.A08..BHZ' , '7F.A09..BHZ'  , '7F.A10..BHZ' , '7F.A11..BHZ', '7F.A13..BHZ', '7F.A14..BHZ', '7F.A19..BHZ'],[0,1,2,3,4,5,6,7,8,9,10,11,12,13], ]).transpose())

    fig, ax = plt.subplots(14, figsize=(30, 75), sharex=True, sharey=False)

    for id in events.trace_ids.iloc[event_id]:
    
        i = int(axes_id[id])
        


        ax[i].plot(data_window[i].times('matplotlib'), data_window[i].data/(data_window[i].data).std(), color='limegreen', label="event_unfiltered")
        ax[i].plot(data_hp[i].times('matplotlib'), data_hp[i].data/(data_hp[i].data).std(), 'blue', label = "hp350")
        ax[i].plot(data_bp[i].times('matplotlib'), data_bp[i].data/(data_bp[i].data).std(), 'purple', label = "bp100-250")
        ax[i].set_title(id)
        ax[i].legend(loc="upper right")
    return fig, ax 















def bandpass_plot_filtered_waveforms(data_window, data_bp_50_100, data_bp_100_150, data_bp_150_200, data_bp_200_250, data_bp_250_300, data_bp_300_350, data_bp_350_400, events, event_id):

    axes_id = dict(np.array([['7F.A01..BHZ' ,'7F.A02..BHZ' , '7F.A03..BHZ' , '7F.A04..BHZ' , '7F.A05..BHZ' , '7F.A06..BHZ' , '7F.A07..BHZ' , '7F.A08..BHZ' , '7F.A09..BHZ'  , '7F.A10..BHZ' , '7F.A11..BHZ', '7F.A13..BHZ', '7F.A14..BHZ', '7F.A19..BHZ'],[0,1,2,3,4,5,6,7,8,9,10,11,12,13], ]).transpose())

    fig, ax = plt.subplots(14, figsize=(25, 65), sharex=True, sharey=False)

    for id in events.trace_ids.iloc[event_id]:
    
        i = int(axes_id[id])
        #print(id)
        ax[i].plot(data_window[i].times('matplotlib'), data_window[i].data, color='limegreen', label="event_unfiltered")
        ax[i].plot(data_bp_50_100[i].times('matplotlib'), data_bp_50_100[i].data, 'blue', label = "bp500-100")
        ax[i].plot(data_bp_100_150[i].times('matplotlib'), data_bp_100_150[i].data, 'purple', label = "bp100-150")
        ax[i].plot(data_bp_150_200[i].times('matplotlib'), data_bp_150_200[i].data, 'orange', label = "bp150-200")
        ax[i].plot(data_bp_200_250[i].times('matplotlib'), data_bp_200_250[i].data, 'green', label = "bp200-250")
        ax[i].plot(data_bp_250_300[i].times('matplotlib'), data_bp_250_300[i].data, 'pink', label = "bp250-300")
        ax[i].plot(data_bp_300_350[i].times('matplotlib'), data_bp_300_350[i].data, 'royalblue', label = "bp300-350")
        ax[i].plot(data_bp_350_400[i].times('matplotlib'), data_bp_350_400[i].data, 'red', label = "bp350-400")



        ax[i].set_title(id)
        ax[i].legend(loc="upper right")
    return fig, ax 
    

   
#if __name__=='__main__':
#    d_w, d_h, d_b = filter_waveforms()