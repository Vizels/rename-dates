import os
from name import FileName

path = "/mnt/f/test/"

file_list = os.listdir(path)

base = FileName()

for file_name in file_list:
    print(base.read_file_name(file_name))
    print(base.rename_file())
    os.rename(path + file_name, path + base.rename_file())