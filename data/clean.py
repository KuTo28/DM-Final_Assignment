with open("./heart_data.csv", "r") as file:
    lines = file.readlines()

c_lines = [lines[0][:-1]]
for line in lines[1:]:
    cleaned_line = line[1:] if line[0] == '"' else line
    cleaned_line = cleaned_line[:-2] if line[-2] == '"' else cleaned_line[:-1]
    cleaned_line = cleaned_line.replace('""', '"')
    c_lines.append(cleaned_line)

with open("./clean_heart_data.csv", "w") as file:
    file.write("\n".join(c_lines))
