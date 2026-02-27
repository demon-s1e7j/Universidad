from typing import Tuple, Dict
from itertools import chain, combinations

Square = Tuple[int, int, int, int]

def E(s: Square) -> Square:
    return s

def T_1(s: Square) -> Square:
    a, b, c, d = s
    return (b, a, d, c)

def T_2(s: Square) -> Square:
    a, b, c, d = s
    return (d, c, b, a)

def D_1(s: Square) -> Square:
    a, b, c, d = s
    return (a, d, c, b)

def D_2(s: Square) -> Square:
    a, b, c, d = s
    return (c, b, a, d)

def R_1(s: Square) -> Square:
    a, b, c, d = s
    return (b, c, d, a)

def R_2(s: Square) -> Square:
    a, b, c, d = s
    return (c, d, a, b)

def R_3(s: Square) -> Square:
    a, b, c, d = s
    return (d, a, b, c)

symmetries = [E, T_1, T_2, D_1, D_2, R_1, R_2, R_3]

identifier = {f((1, 2, 3, 4)):f.__name__ for f in symmetries}

multiplication = {f1.__name__:{f2.__name__:"" for f2 in symmetries} for f1 in symmetries}

for f1 in symmetries:
    for f2 in symmetries:
        multiplication[f1.__name__][f2.__name__] = identifier[f1(f2((1, 2, 3, 4)))]

HEADER_ORDER = ["E", "T_1", "T_2", "D_1", "D_2", "R_1", "R_2", "R_3"]
ROW_ORDER = ["E", "T_1", "T_2", "D_1", "D_2", "R_1", "R_2", "R_3"]  # Can be different if needed

def print_table_fixed_order(data: Dict[str, Dict[str, str]]):
    # Print header using fixed order
    print(f"{''}", end="&")  # Empty top-left cell
    for header in HEADER_ORDER:
        print(f" ${header}$ ", end="&")
    print()
    
    # Print rows using fixed order
    for row_key in ROW_ORDER:
        if row_key not in data:
            continue  # Skip if row key doesn't exist
        
        print(f" ${row_key}$ ", end="&")
        for col_key in HEADER_ORDER:
            value = data[row_key].get(col_key, "")
            print(f" ${value}$ ", end="&")
        print()


print_table_fixed_order(multiplication)


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def check_closure(p) -> bool:
    for f1 in p:
        for f2 in p:
            if multiplication[f1][f2] not in p:
                return False
    return True

for p in powerset(HEADER_ORDER):
    if check_closure(p):
        print(f"{[f for f in p]}")
