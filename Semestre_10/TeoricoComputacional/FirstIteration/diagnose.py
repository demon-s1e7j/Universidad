import os
import sys

print("=== Diagnóstico del entorno ===")
print(f"Python: {sys.version}")
print(f"Display: {os.environ.get('DISPLAY', 'NO SET')}")
print(f"Wayland: {os.environ.get('WAYLAND_DISPLAY', 'NO SET')}")
print(f"XDG Session: {os.environ.get('XDG_SESSION_TYPE', 'NO SET')}")
print(f"GDK Backend: {os.environ.get('GDK_BACKEND', 'NO SET')}")

try:
    import tkinter as tk
    print("✓ tkinter importa correctamente")
    
    root = tk.Tk()
    root.withdraw()  # No mostrar ventana
    print("✓ tkinter puede crear ventana")
    root.destroy()
    
except Exception as e:
    print(f"✗ Error con tkinter: {e}")
    import traceback
    traceback.print_exc()
