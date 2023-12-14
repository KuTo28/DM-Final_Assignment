
with(open("./dataset/heart_data.csv", "r")) as file:
    lines = file.readlines()

c_lines = [lines[0][:-1]]    
for line in lines[1:]:
    cleaned_line = (line[1:-2]).replace('""', '"')
    c_lines.append(cleaned_line)
    
with(open("./dataset/cleaned_data.csv", "w")) as file:
    file.write("\n".join(c_lines))