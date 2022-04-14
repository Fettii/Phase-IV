reader = open("testfiel.txt","r")
all_lines = reader.readlines()
for line in all_lines:
    print(all_lines.index(line))