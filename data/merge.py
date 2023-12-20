import os
import sys

if len(sys.argv) != 3:
    print("This cli takes two positional arguments <path> <merged_filename>")
    exit(1)

path = sys.argv[1]
target_file = sys.argv[2]

files = (filename for filename in os.listdir(path) if filename[0].isdigit())

sorted_files = sorted(files, key=lambda x: int(x.split("_")[0]))

lines = []
for filename in sorted_files:
    file_path = os.path.join(path, filename)
    with open(file_path, "r") as file:
        lines.extend(file.readlines())

with open(os.path.join(path, target_file), "w") as merged_file:
    merged_file.writelines(lines)
