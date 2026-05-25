class Peso:
    def __init__(self, vp_H1: int, vp_H2: int, name: str) -> None:
        self.value = (vp_H1, vp_H2)
        self.name = name
        self.B = 1

    def calculate_I_3(self) -> float:
        m_1, _ = self.value
        return m_1 / 2

    def calculate_Y(self) -> float:
        m_1, m_2 = self.value
        return (1 / 3) * m_1 + (2 / 3) * m_2

    def calculate_S(self) -> float:
        return self.calculate_Y() - self.B

    def calculate_Q(self) -> float:
        return self.calculate_I_3() + (self.calculate_Y() / 2)

    def __add__(self, other):
        if not isinstance(other, Peso):
            raise Exception("Solamente consideramos la suma entre pesos")
        vp_H1_1, vp_H2_1 = self.value
        vp_H1_2, vp_H2_2 = other.value
        return Peso(vp_H1_1 + vp_H1_2, vp_H2_1 + vp_H2_2, f"{self.name} \\otimes {other.name}")

    def __sub__(self, other):
        if not isinstance(other, Peso):
            raise Exception("Solamente consideramos la resta entre pesos")
        vp_H1_1, vp_H2_1 = self.value
        vp_H1_2, vp_H2_2 = other.value
        return Peso(vp_H1_1 - vp_H1_2, vp_H2_1 - vp_H2_2, "")

    def __str__(self) -> str:
        def format_latex(val: float) -> str:
            if val.is_integer():
                return str(int(val))
            return f"\\frac{{{int(val * 2)}}}{{2}}"

        i3 = format_latex(self.calculate_I_3())
        y = format_latex(self.calculate_Y())
        s = format_latex(self.calculate_S())
        q = format_latex(self.calculate_Q())
        
        return f"  ${self.name}$ & ${self.value}$ & ${i3}$ & ${y}$ & ${s}$ & ${q}$ \\\\"


alpha_1 = Peso(2, -1, "\\alpha_1")
alpha_2 = Peso(-1, 2, "\\alpha_2")


delta_pp = Peso(3, 0, "\\Delta^{++}")
delta_p  = delta_pp - alpha_1; delta_p.name = "\\Delta^{+}"
delta_0  = delta_p  - alpha_1; delta_0.name = "\\Delta^{0}"
delta_m  = delta_0  - alpha_1; delta_m.name = "\\Delta^{-}"

sigma_p  = delta_p  - alpha_2; sigma_p.name = "\\Sigma^{*+}"
sigma_0  = sigma_p  - alpha_1; sigma_0.name = "\\Sigma^{*0}"
sigma_m  = sigma_0  - alpha_1; sigma_m.name = "\\Sigma^{*-}"

xi_0     = sigma_0  - alpha_2; xi_0.name = "\\Xi^{*0}"
xi_m     = xi_0     - alpha_1; xi_m.name = "\\Xi^{*-}"

omega_m  = xi_m     - alpha_2; omega_m.name = "\\Omega^{-}"

estados = [
    delta_pp, delta_p, delta_0, delta_m,
    sigma_p, sigma_0, sigma_m,
    xi_0, xi_m,
    omega_m
]

print("\\begin{table}[h]")
print("\\centering")
print("\\renewcommand{\\arraystretch}{1.5}")
print("\\begin{tabular}{|c|c|c|c|c|c|}")
print("\\hline")
print("\\textbf{Particula} & \\textbf{Peso $(m_1, m_2)$} & \\textbf{$I_3$} & \\textbf{$Y$} & \\textbf{$S$} & \\textbf{$Q$} \\\\ \\hline")

for estado in estados:
    print(estado)
    print("  \\hline")

print("\\end{tabular}")
print("\\caption{Pesos del decuplete $\\mathbf{10}$ con sus respectivos numeros cuanticos.}")
print("\\label{tab:pesos_decuplete}")
print("\\end{table}")
