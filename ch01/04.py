string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_letter = [1, 5, 6, 7, 8, 9, 15, 16, 19]
periodic_table = dict()

splitted_string = string.replace(".", "").split()

for i, word in enumerate(splitted_string):
    if i + 1 in one_letter:
        periodic_table[word[:1]] = i + 1
    else:
        periodic_table[word[:2]] = i + 1

print(periodic_table)
