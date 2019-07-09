import os 


def traverse_dir(rootDir,pathlist:list): 
    '''
    input: string rootDir, list for filepath storage
    output: NA
    '''

    for fi in os.listdir(rootDir): 
        path = os.path.join(rootDir, fi) 
        if os.path.isdir(path): 
            traverse_dir(path,pathlist)
        elif not os.path.isdir(path):
            if ".csv" in fi or ".CSV" in fi:
                pathlist.append(path)


# use this to ruturn a sorted filepaths of all csv files in rootdir(which as input filepafth)
def show_all_path(filepath:str):
    filepath_list = []
    filepath = filepath.strip()
    traverse_dir(filepath,filepath_list)
    return sorted(filepath_list)


def get_filename(filepath_list:list):
    namelist=[]
    for fi in filepath_list:
        fi = os.path.basename(fi)
        namelist.append(fi.split('.')[0])# fi.split('.')[0] for delete '.csv'
    return namelist

name= show_all_path('/Users/wangmu/Documents/Science/mG1/数据/sec ')