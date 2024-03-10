import os
base_directory="/home/ashwin/Desktop/"
for i in range(1,101):
    directory_name=f"friend{i}"
    directory_path=os.path.join(base_directory,directory_name)
    os.makedirs(directory_path)
print("Hundred directories named friend created successfully !!!")
