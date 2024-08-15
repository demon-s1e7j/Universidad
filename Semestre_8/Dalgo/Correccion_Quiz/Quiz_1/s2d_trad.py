import bs_trad

def search(arr: list[list[int]], x: int) -> tuple[int, int]:
    for i, l in enumerate(arr):
        pos = bs_trad.binary_search(l, x);
        if pos != -1:
            return i, pos
    return -1, -1

val = search([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 11)
print(val)
