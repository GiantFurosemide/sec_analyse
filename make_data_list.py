import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import nltk
import pandas as pd
import TraverseDir.TraverseDir as td
import pandas_toolkit.mytoolkit as tk
from scipy.signal import find_peaks
import pickle


def make_data_list(rootdir:str,x_interval:tuple=(2.0,5.5)):
    # this is data make module
    rootDir = rootdir
    file_path_list = td.show_all_path(rootDir)
    file_name_list = td.get_filename(file_path_list)
    #overview alldata in rootDir
    print('length is: '+f'{len(file_name_list)}')
    print('type is: '+f"{type(file_name_list)}")
    # make data list[('name',pandas.df),...]
    data_list = []
    for finame,fipath in zip(file_name_list,file_path_list):
        data_pair= (finame,tk.onestep_norm_peak2zero(fipath,x_interval),tk.onestep_norm_peak2max(fipath,x_interval))
        data_list.append(data_pair)
    ss=data_list
    return ss
    #SS :[(filename:str,peak2zero:pandas.df,peak2max:pandas.df)]
    #overview alldata in ss
    print('length is: '+f'{len(ss)}')
    print('type is: '+f"{type(ss)}")

# save
#with open(f'laballdata_datalist_ss_{x_interval[0]}_{x_interval[1]}','wb') as fi:
#    pickle.dump(ss,fi)
## load
#with open('laballdata_datalist_ss','rb') as fi:
#    ss_load = pickle.load(fi)
    

if __name__ == '__main__':
    rootDir_input = input('>>>Please input rootdir.\n')
    x_interval_input = input('>>>Please input x_interval.\n')
    ss = make_data_list(rootDir_input,x_interval_input)

    with open(f'laballdata_datalist_ss_{x_interval_input[0]}_{x_interval_input[1]}','wb') as fi:
        pickle.dump(ss,fi)

    print(f'laballdata_datalist_ss_{x_interval_input[0]}_{x_interval_input[1]}'+' has already been saved to current file')


    
    