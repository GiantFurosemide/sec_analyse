import os 


def traverse_dir(rootDir,namelist:list,pathlist:list): 
    '''
    input: string rootDir, list for filename storage, list for file
    output: NA
    '''

    for fi in os.listdir(rootDir): 
        path = os.path.join(rootDir, fi) 
        if os.path.isdir(path): 
            traverse_dir(path,namelist,pathlist)
        elif not os.path.isdir(path):
            if ".csv" in fi or ".CSV" in fi:
                namelist.append(fi.split('.')[0])# fi.split('.')[0] for delete '.csv'
                pathlist.append(path)


# use this
def show_all_path(filepath:str):

    filename_list =[]
    filepath_list = []
    filepath = filepath.strip()
    traverse_dir(filepath,filename_list,filepath_list)
    return filename_list,filepath_list