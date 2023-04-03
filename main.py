import os

folder_name = 'files/'
files = ['1.txt', '2.txt', '3.txt']

sorted_file_list = []

for file in files:
    with open(folder_name+file, 'r') as f:
        count = len(f.readlines())
    sorted_file_list.append([file, count])
sorted_file_list = sorted(sorted_file_list, key=lambda x:x[1])

with open('output/out.txt', 'w') as new:
    for list in sorted_file_list:
        new.write(f'{list[0]}\n')
        new.write(f'{list[1]}\n')
        with open(folder_name+list[0], 'r') as r:
            new.write(f'{r.read()}\n')
