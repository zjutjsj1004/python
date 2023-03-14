import os
import re

dir = '/data/gocpplua/python/test'
first_level_files = os.listdir(dir)
print(first_level_files)
filterSubpath = ''
update_kinect = True
count = 0
for idx in range(len(first_level_files)):
    first_level_file = first_level_files[idx]
    first_level_files_fullpath = os.path.join(dir, first_level_file)
    if not os.path.isdir(first_level_files_fullpath):
        print("first_level_files_fullpath {0} is not dir".format(first_level_files_fullpath))
        continue

    if not update_kinect:
        if count != 0:
            filterSubpath += ','
        filterSubpath += first_level_files_fullpath
        count = count + 1
        continue

    find_second = False
    second_level_files = os.listdir(first_level_files_fullpath)
    for idx2 in range(len(second_level_files)):
        second_level_file = second_level_files[idx2]
        second_level_files_fullpath = os.path.join(first_level_files_fullpath, second_level_file)
        if not os.path.isdir(second_level_files_fullpath):
            print("second_level_files_fullpath {0} is not dir".format(second_level_files_fullpath))
            continue
        match_path = re.findall('.*VID_[0-9]{8}_[0-9]{6}', second_level_files_fullpath)
        if len(match_path) == 0:
            print("second_level_files_fullpath {0} is not match".format(second_level_files_fullpath))
            continue
        else:
            if count != 0:
                filterSubpath += ','
            find_second = True
            filterSubpath += second_level_files_fullpath
            count = count + 1
    if not find_second:
        if count != 0:
            filterSubpath += ','
        filterSubpath += first_level_files_fullpath
        count = count + 1

print (filterSubpath)
