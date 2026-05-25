class Peso:
    def __init__(self, vp_H1: int, vp_H2: int, name: str) -> None:
        self.value = (vp_H1, vp_H2)
        self.name = name

    def __add__(self, other) -> Peso:
        if not isinstance(other, Peso):
            raise Exception("Solamente consideramos la suma entre pesos")
        vp_H1_1, vp_H2_1 = self.value
        vp_H1_2, vp_H2_2 = other.value
        return Peso(vp_H1_1 + vp_H1_2, vp_H2_1 + vp_H2_2, f"{self.name} \\otimes {other.name}")

    def __str__(self) -> str:
        return f"{self.name} &= {self.value}\\\\"

peso_e_1 = Peso( 1,  0, "e_1")
peso_e_2 = Peso(-1,  1, "e_2")
peso_e_3 = Peso( 0, -1, "e_3")

pesos = [peso_e_1, peso_e_2, peso_e_3]

print("\\begin{align*}")
for peso_1 in pesos:
    for peso_2 in pesos:
        print("\t", peso_1 + peso_2)
print("\\end{align*}")
