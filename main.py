import os

size = 0
info_dict = {}

check_path = r'C:\Users\vby\PycharmProjects\Traverse_directories\dummy'

for root, folders, files in os.walk(check_path):
    print("-----------")
    print(root)
    print(folders)
    print(files)
    for file in files:
        print(f"this is here {str(root+'\\'+file)}")
        print(f"{file} is of size {os.path.getsize(str(root+'\\'+file))}")
        size += os.path.getsize(str(root+'\\'+file))
    info_dict[root] = size
    size = 0
    print(info_dict)
