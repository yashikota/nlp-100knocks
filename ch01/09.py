import random


def shuffle(enter: str):
    res: str = [
        i[0] + "".join(random.sample(i[1:-1], len(i) - 2)) + i[-1] if len(i) > 4 else i
        for i in enter.split()
    ]
    return " ".join(res)


def main():
    enter: str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

    print(shuffle(enter))


if __name__ == "__main__":
    main()
