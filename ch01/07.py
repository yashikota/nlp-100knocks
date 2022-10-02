def temperature(x: int, y: str, z: float) -> str:
    return f"{x}時の{y}は{z}"


def main():
    x: int = 12
    y: str = "気温"
    z: float = 22.4

    print(temperature(x, y, z))


if __name__ == "__main__":
    main()
