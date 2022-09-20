import os
import sys
sys.path.append(os.getcwd())

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import obspy
import glob

class PrecisionDateFormatter(ticker.Formatter):
  

    def __init__(self, fmt, precision=3, tz=None):
        """
        Parameters
        ----------
        fmt : str
            `~datetime.datetime.strftime` format string.
        """
        from matplotlib.dates import num2date
        if tz is None:
            from matplotlib.dates import _get_rc_timezone
            tz = _get_rc_timezone()
        self.num2date = num2date
        self.fmt = fmt
        self.tz = tz
        self.precision = precision

    def __call__(self, x, pos=0):
        if x == 0:
            raise ValueError("illegal date;"
                             "you have not informed the axis that it is "
                             "plotting dates, e.g., with ax.xaxis_date()")

        dt = self.num2date(x, self.tz)
        ms = dt.strftime("%f")[:self.precision]

        return dt.strftime(self.fmt).format(ms=ms)

    def set_tzinfo(self, tz):
        self.tz = tz

def plot_wave(obspydata, **kwargs):

    data_len = len(obspydata)
    
    #fig, ax = plt.subplots(data_len, figsize=(15, 5*data_len), sharex=True, sharey=True)
    
    
    
    #fig, ax = plt.subplots(data_len, figsize=(35, 15), sharex=True, sharey=True)
    fig, ax = plt.subplots(data_len, figsize=(15, 5*data_len), sharex=True, sharey=True)
    
    
    
    
    
    #fig, ax = plt.subplots(data_len, figsize=(35, 8), sharex=True, sharey=True)
        
  
    #fig, ax = plt.subplots(data_len, 1 , sharex=True, sharey=True)
    
    #print(data_len)
    
    
    if type(obspydata) == obspy.core.trace.Trace:
        obspydata = [obspydata]

    for n, tr in enumerate(obspydata):
        ax[n].plot(tr.times('matplotlib'), np.array(tr.data) - np.mean(np.array(tr.data)), **kwargs)
        ax[n].text(1, 1000,str("LALA"), fontsize = 12)
        #ax[n].set_ylabel('Pressure (Pa)', fontsize=15)
        
    ax[n].xaxis.set_major_formatter(PrecisionDateFormatter("%H:%M:%S.{ms}"))
    
    fig.tight_layout(pad=0)
    return fig, ax
    
    
def plot_wave_autoscale(obspydata, **kwargs):

    data_len = len(obspydata)
    
    #fig, ax = plt.subplots(data_len, figsize=(15, 5*data_len), sharex=True, sharey=True)
    
    fig, ax = plt.subplots(data_len, figsize=(35, 15), sharex=True, sharey=False)
    
    #fig, ax = plt.subplots(data_len, 1 , sharex=True, sharey=True)
    
    #print(data_len)
    
    
    if type(obspydata) == obspy.core.trace.Trace:
        obspydata = [obspydata]

    for n, tr in enumerate(obspydata):
        ax[n].plot(tr.times('matplotlib'), np.array(tr.data) - np.mean(np.array(tr.data)), **kwargs)
        #ax[n].set_ylabel('Pressure (Pa)', fontsize=15)
        
    ax[n].xaxis.set_major_formatter(PrecisionDateFormatter("%H:%M:%S.{ms}"))
    
    fig.tight_layout(pad=0)
    return fig, ax

    

if __name__=='__main__':
    print('WOOHOO!')
