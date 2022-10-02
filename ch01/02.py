string1 = "パトカー"
string2 = "タクシー"

print("".join([i + j for i, j in zip(string1, string2)]))
