import os

os.chdir(r'C:\Users\student\cham\appliance')

for filename in os.listdir("."):
    filename_without_ext = os.path.splitext(filename)[0]
    extention = os.path.splitext(filename)[1]
    new_file_name = "ssafy_" + filename_without_ext
    new_file_name_with_ext = new_file_name + extention
    print(new_file_name_with_ext)