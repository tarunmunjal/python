import os,re

def get_filenames_reursively(file_pattern,path_to_search):
    fullfilepath = []
    for root, d, filenames in os.walk(path_to_search):
        for filename in filenames: 
            fullfilepath.append(os.path.join(root,filename)) 
    if file_pattern:
        ffp = []
        pattern = re.compile(file_pattern)
        for ffpath in fullfilepath:
            if pattern.findall(ffpath):
                ffp.append(ffpath)
        return ffp
    else:
        return fullfilepath
allfilepaths = get_filenames_reursively(".yaml","/home/tmunjal/Desktop/somefolder")
