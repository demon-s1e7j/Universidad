from functools import wraps
from typing import Sequence, Union
import math as mt

Numeric = Union[int, float, complex]


def mean(data: Sequence[Numeric]) -> Numeric:
    return sum(data) / len(data)


def autofill_valmean(func):
    @wraps(func)
    def wrapper(
            data: Sequence[Numeric],
            *args,
            valmean: Numeric | None = None,
            **kwargs):
        if valmean is None:
            valmean = mean(data)
        return func(data, *args, valmean=valmean, **kwargs)
    return wrapper


@autofill_valmean
def list_deviation(
        data: Sequence[Numeric],
        valmean: Numeric | None = None) -> Sequence[Numeric]:
    def deviation(x): return abs(valmean - x)
    return [deviation(x) for x in data]


@autofill_valmean
def standard_rough_and_ready(
        data: Sequence[Numeric],
        valmean: Numeric | None = None) -> Numeric:
    return (2 / 3) * (max(list_deviation(data, valmean=valmean)))


@autofill_valmean
def standard_2_3(
        data: Sequence[Numeric],
        valmean: Numeric | None = None) -> Numeric:
    return mt.sqrt(
        (sum(list_deviation(data, valmean=valmean))) / (len(data) - 1))


def standar_error(standard_deviation: Numeric, N: int) -> Numeric:
    return standard_deviation / mt.sqrt(N)


data = [25.8, 26.2, 26.0, 26.5, 25.8, 26.1, 25.8, 26.3]

if __name__ == "__main__":
    promedio = mean(data)
    desviacion_rar = standard_rough_and_ready(data)
    desviacion_2_3 = standard_2_3(data)
    error_rar = standar_error(desviacion_rar, len(data))
    error_2_3 = standar_error(desviacion_2_3, len(data))
    print(f"""\
    {promedio=}
    {desviacion_rar=}
    {desviacion_2_3=}
    {error_rar=}
    {error_2_3=}
    """)
