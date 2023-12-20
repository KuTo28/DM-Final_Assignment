import sys

if len(sys.argv) != 3:
    print("This cli takes two positional arguments <file_path> <cleaned_path>")
    exit(1)

file_path = sys.argv[1]
cleaned_path = sys.argv[2]

with open(file_path, "r") as file:
    lines = file.readlines()

c_lines = []
for line in lines:
    cleaned_line = line[1:] if line[0] == '"' else line
    cleaned_line = cleaned_line[:-2] if line[-2] == '"' else cleaned_line[:-1]
    cleaned_line = cleaned_line.replace('""', '"')
    c_lines.append(cleaned_line)

with open(cleaned_path, "w") as file:
    file.write("\n".join(c_lines))
