def binary_search(arr: list[int], x: int) -> int:
    high = len(arr) - 1; # C1 // 1
    low = 0; # C2 // 1
    pos = -1; # C3 // 1
    while (low < high and pos == -1): # C4 // log2(n)
        mid = (high + low) // 2; # C5 // log2(n)
        val = arr[mid]; # C6 // log2(n)
        if (val < x): low = mid + 1; # C7 // log2(n)
        elif (val > x): high = mid - 1; # C8 // log2(n)
        else: pos = mid; # C9 // log2(n)
    return pos # C10 // 1

if __name__ == "__main__":
    val = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11);
    print(val);
