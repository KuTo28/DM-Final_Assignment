import sys

if len(sys.argv) != 2:
    print("This cli takes only one positional argument <file_path>")
    exit(1)

file_path = sys.argv[1]

with open(file_path, "r") as file:
    lines = file.readlines()

with open(f"{file_path}.bak", "w") as file:
    file.write(lines)

c_lines = [lines[0][:-1]]
for line in lines[1:]:
    cleaned_line = line[1:] if line[0] == '"' else line
    cleaned_line = cleaned_line[:-2] if line[-2] == '"' else cleaned_line[:-1]
    cleaned_line = cleaned_line.replace('""', '"')
    c_lines.append(cleaned_line)

with open(file_path, "w") as file:
    file.write("\n".join(c_lines))
