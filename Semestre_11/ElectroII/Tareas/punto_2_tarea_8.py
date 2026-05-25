from decimal import Decimal, getcontext

# Configurar alta precisión (50 dígitos significativos)
getcontext().prec = 50

# Valores de masa en MeV/c^2 (se introducen como cadena para evitar errores de punto flotante)
m_n = Decimal('939.57')
m_p = Decimal('938.27')
m_e = Decimal('0.51')

# Cálculo según las fórmulas dadas
E_p = (m_n**2 + m_p**2 - m_e**2) / (2 * m_n)
E_e = m_n - E_p

K_p = E_p - m_p
K_e = E_e - m_e

# Impresión con redondeo a 4 cifras decimales (equivalente a "4 números de certeza")
print(f"E_p = {E_p:.4f}")
print(f"E_e = {E_e:.4f}")
print(f"K_p = {K_p:.4f}")
print(f"K_e = {K_e:.4f}")
