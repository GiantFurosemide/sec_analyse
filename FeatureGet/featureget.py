import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import nltk
import pandas as pd
import TraverseDir.TraverseDir as td
import pandas_toolkit.mytoolkit as tk
from scipy.signal import find_peaks
import scipy.signal

def df2feature_vector(df:'pandas.dataframe',maxn:int=1):
    
    '''
    input pandas.df\maxn(optional)
    output:([index_list],array[max_peak_list]:peak height,array[prominences],array[results_half[0]],array[results_full[0]])
    
    need: 
    import matplotlib.pyplot as plt
    import matplotlib
    import numpy as np
    import nltk
    import pandas as pd
    import TraverseDir.TraverseDir as td
    import pandas_toolkit.mytoolkit as tk
    from scipy.signal import find_peaks
    import scipy.signal
    
    maxn:number of max values you want.usually we just pick main peak between time[2.0,5.0]
    
    about width:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.peak_widths.html#scipy.signal.peak_widths
    '''
    try:
        # find peaks,return peaks's index array
        peaks_found,_ = scipy.signal.find_peaks(df.peak)
        # pick peaks' <.peak> from df by peaks_found
        sele_peak=df.peak[peaks_found]
        # pick max value from pd.Series sele_peak,max顺序为数值降序
        max_array=sele_peak.values[np.argsort(sele_peak)[-maxn:][::-1]]
        # make index list
        index_list=[]
        for i in max_array:
            index_list.append(sele_peak.index[sele_peak==i][0])
        # get prominences:array
        prominences = scipy.signal.peak_prominences(df.peak,index_list)[0] # prominences has 3 arraies,use first 
        # calculation about width.
        # x axis is value .time. But results_half returns indexs of .time,with which we calculate width.
        # width_coefficient*results_half[0] returns what we see in the plot.
        index_x_max=df.time.index[df.time==df.time.max()][0]
        index_x_min=df.time.index[df.time==df.time.min()][0]
        index_length = index_x_max-index_x_min
        width_coefficient=(df.time.max()-df.time.min())/index_length
        
        # get width:array
        results_half = scipy.signal.peak_widths(df.peak, index_list, rel_height=0.5)[0]*width_coefficient
        results_full = scipy.signal.peak_widths(df.peak, index_list, rel_height=1)[0]*width_coefficient
        # get retention time list
        retention_time_list = []
        for i in index_list:
            retention_time_list.append(df.time[i])
        
        return (index_list,max_array,retention_time_list,prominences,results_half,results_full)
    except TypeError:
        return ([])
    
    
def make_name_feature_list(ss:'df'):
    '''
     make feature list :
     input: ss:[(name:str,df:pandas.datafram),...]
     output:[(name,[max_peak,retention_time,half_width)]
    '''
    name_feature_list = []
    for sample in ss:
        name = sample[0]
        df_zero = sample[1]
        
        try:
            features = df2feature_vector(df_zero,1)
            max_peak= features[3][0] #use prominences
            retention_time = features[2][0]
            half_width = features[4][0]
            
            name_feature_list.append((name,[max_peak,retention_time,half_width]))
        except IndexError:
            pass
    return name_feature_list
