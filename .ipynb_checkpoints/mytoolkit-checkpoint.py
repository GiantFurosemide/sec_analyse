

import pandas
import numpy


# choose df by 'time' which between 2.5/5.0
def pick_x_region(
    df:'pandas data frame',
    x_interval:'x axis interval'=(2.5,5.0),
    ):

    """
    input:
    pandas.core.frame.DataFrame df
    tuple x_interval.
    
    output: 
    pandas.core.frame.DataFrame a df section in x_interval
    """
    if isinstance(df,pandas.core.frame.DataFrame):
        df = df.copy()
        df = df[df.time<x_interval[1]]
        df = df[df.time>x_interval[0]]
        return df


#normalize to max
def normalize_peak2max(df:'pandas data frame'):
    if isinstance(df,pandas.core.frame.DataFrame):
        df.peak= df.copy().apply(lambda x: (x-x.min())/(x.max()-x.min())).peak*100
    return df

#normalize to zero
def normalize_peak2zero(df:'pandas data frame'):
    if isinstance(df,pandas.core.frame.DataFrame):
        df.peak= df.copy().apply(lambda x: (x-x.min())).peak
    return df


# pandas.read_csv.input string file_path output a pandas data frame
def pandas_read_sec_csv(file_path:'string file path'):
    '''
    only for read individual sec csv file
    columns given [['time','peak']]
    '''
    if isinstance(file_path,str):
        df = pandas.read_csv(file_path,encoding = "UTF-16-LE",sep='\t',names=['time','peak'])
        return df
    else:
        return None


