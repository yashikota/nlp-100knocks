def character_n_gram(enter: str, n: int) -> list:
    return [enter[i : i + n] for i in range(len(enter) - n + 1)]


def word_n_gram(enter: str, n: int) -> list:
    return [
        " ".join(enter.split()[i : i + n]) for i in range(len(enter.split()) - n + 1)
    ]


def main():
    enter: str = "I am an NLPer"
    n: int = 2

    print(character_n_gram(enter.replace(" ", ""), n))
    print(word_n_gram(enter, n))


if __name__ == "__main__":
    main()
