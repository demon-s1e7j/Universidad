from decimal import Decimal, getcontext

# Configurar alta precisión (50 dígitos significativos)
getcontext().prec = 50

# Valores de masa en MeV/c^2 (se introducen como cadena para evitar errores de punto flotante)
m_n = Decimal('939.57')
m_p = Decimal('938.27')
m_e = Decimal('0.51')

M = m_p + m_e

E_pe = (m_n**2 + M**2) / (2 * m_n)
Gamma = (E_pe)/M
E_e = Gamma * m_e
K_e = E_e - m_e
# Impresión con redondeo a 4 cifras decimales (equivalente a "4 números de certeza")
print(f"E_pe = {E_pe}")
print(f"Gamma = {Gamma}")
print(f"E_e = {E_e}")
