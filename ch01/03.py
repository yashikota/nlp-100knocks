string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
splitted_string = string.replace(",", "").replace(".", "").split()

length_list = [len(i) for i in splitted_string]

print(length_list)
