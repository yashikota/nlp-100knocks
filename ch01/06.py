def character_n_gram(enter: str, n: int) -> list:
    return [enter[i : i + n] for i in range(len(enter) - n + 1)]


def main():
    str1: str = "paraparaparadise"
    str2: str = "paragraph"
    n: int = 2

    x = set(character_n_gram(str1, n))
    y = set(character_n_gram(str2, n))

    print("和集合", x.union(y))
    print("積集合", x.intersection(y))
    print("差集合", x.difference(y))
    print('xに"se"が含まれるか', {"se"}.issubset(x))
    print('yに"se"が含まれるか', {"se"}.issubset(y))


if __name__ == "__main__":
    main()
