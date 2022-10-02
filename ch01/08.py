def cipher(enter: str) -> str:
    crypt = [chr(219 - ord(i)) if i.islower() else i for i in enter]
    return "".join(crypt)


def main():
    enter: str = "On my business card, I am a corporate president. In my mind, I am a game developer. But in my heart, I am a gamer."
    print("original: ", enter)

    encrypt: str = cipher(enter)
    print("encrypt : ", encrypt)

    decrypt: str = cipher(encrypt)
    print("decrypt : ", decrypt)


if __name__ == "__main__":
    main()
