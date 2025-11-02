#!/usr/bin/env python3
"""
Script de lanzamiento alternativo para evitar problemas con xcb
"""

import os
import sys

# Configurar variables de entorno para evitar problemas con xcb
os.environ['TK_SILENCE_DEPRECATION'] = '1'
os.environ['QT_QPA_PLATFORM'] = 'xcb'

def main():
    try:
        from main import App
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Error al lanzar la aplicación: {e}")
        print("Intentando modo de compatibilidad...")
        compatibility_mode()

def compatibility_mode():
    """Modo de compatibilidad con tkinter estándar"""
    import tkinter as tk
    from tkinter import ttk, messagebox
    
    root = tk.Tk()
    root.title("Catálogos de VizieR - Modo Compatibilidad")
    root.geometry("600x400")
    
    # Interfaz simple de fallback
    frame = ttk.Frame(root, padding="20")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    ttk.Label(frame, text="Catálogos de VizieR", font=('Arial', 16)).grid(row=0, column=0, pady=10)
    ttk.Label(frame, text="Modo de compatibilidad activado").grid(row=1, column=0, pady=5)
    
    # Aquí podrías añadir funcionalidad básica con tkinter estándar
    ttk.Button(frame, text="Salir", command=root.quit).grid(row=2, column=0, pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
