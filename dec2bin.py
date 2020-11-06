from typing import List


def dec2bin(dec: int) -> List[int]:
    remainders = []

    while dec != 0:
        remainders.append(dec % 2)
        dec //= 2

    remainders.reverse()

    return remainders


if __name__ == '__main__':
    import random
    num = random.randint(1, 10)
    print(dec2bin(num))
