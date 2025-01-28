import sys

def change(origin:str, destiny: str):
    def inner(func):
        def wrapper(*args):
            return func(*args).replace(origin, destiny)
        return wrapper
    return inner


@change("&&", " and ")
@change("||", " or ")
@change("!", " not ")
def get_function() -> str:
    return sys.stdin.readline().strip()

@change("=", " = ")
@change("true", "True")
@change("false", "False")
@change(",", "; ")
def get_values() -> str:
    return sys.stdin.readline().strip()

def get_expresion(fun: str, vars: str) -> str:
    return f"{vars}\nprint(str({fun}).lower())"

cases = int(sys.stdin.readline())
for __ in range(cases):
    fun = get_function()
    vars = get_values()
    expresion = get_expresion(fun, vars)
    exec(expresion)
