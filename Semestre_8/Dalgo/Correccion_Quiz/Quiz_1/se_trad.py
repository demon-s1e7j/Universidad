def sumEven(a: list[list[int]]) -> int:
    s = 0;
    i = 0;
    j = 0;
    while (i < len(a)):
        if (a[i][j] % 2 == 0): s = s + a[i][j]
        if (j < len(a[i]) - 1): j += 1;
        else: i += 1; j = 0;
    return s

val = sumEven([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
res = 2 + 4 + 6 + 8
print(f"{res} = {val}")
