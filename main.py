import os
from name import FileName

path = "/mnt/f/test/"

file_list = os.listdir(path)

base = FileName()
try:
    for file_name in file_list:
        base.read_file_name(file_name)
        if os.path.isdir(path + file_name) and base.is_base_digital():
            print(base.base)
            base.rename_file()
            os.rename(path + file_name, path + base.rename_file())
            
    print("Files renamed successfully.")
except Exception as e:
    print(e)
    print("Error in renaming files.")
