import os
import time

info_dict = {}


check_path = r'C:\Users\vby\PycharmProjects\Traverse_directories\dummy'

def dive_deep_info(path):
    for entry in os.scandir(path):
        if path not in info_dict:   
            info_dict[path] = [0,None]
        if os.path.isfile(os.path.join(path,entry)):
            info_dict[path][0] += os.path.getsize(os.path.join(path,entry))
            last_modified = time.ctime(os.path.getmtime(os.path.join(path,entry)))
            info_dict[path][1] = last_modified
        elif os.path.isdir(os.path.join(path, entry)):
            dive_deep_info(os.path.join(path, entry))
            try:
                info_dict[path][0] += info_dict[os.path.join(path, entry)][0] 
            except KeyError:
                continue

    return info_dict
    
        
#os.walk

print(dive_deep_info(check_path))


