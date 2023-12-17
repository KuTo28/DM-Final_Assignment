import os

# Get a list of files in the directory
files = [filename for filename in os.listdir(".") if filename[0].isdigit()]

# Sort the files based on their numeric prefix
sorted_files = sorted(files, key=lambda x: int(x.split("_")[0]))

# Merge the contents of the sorted files
merged_contents = ""
for filename in sorted_files:
    file_path = os.path.join(".", filename)
    with open(file_path, "r") as file:
        merged_contents += file.read()

# Write the merged contents to a new file
merged_file_path = os.path.join(".", "heart_data.csv")
with open(merged_file_path, "w") as merged_file:
    merged_file.write(merged_contents)
