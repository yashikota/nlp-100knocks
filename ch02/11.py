with open("./popular-names.txt") as f:
    file = f.read()

file.replace("\t", " ")

with open("./popular-names.txt") as f:
    file = f.readlines()

print(file)
