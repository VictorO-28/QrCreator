import tkinter as tk
from tkinter import messagebox, filedialog
from QR import generar_qr
import os

def correr_app():
    root = tk.Tk()
    root.title("Generador QR - v1.0")
    root.geometry("600x500")
    root.configure(bg="#f0f0f0")
    
    COLOR_PRIMARIO = "#0066cc"   
    COLOR_SECUNDARIO = "#ff6b35" 
    COLOR_FONDO = "#ffffff"
    COLOR_TEXTO_LABEL = "#000000"
    COLOR_ENTRADA = "#ffffff"


    frame_titulo = tk.Frame(root, bg=COLOR_PRIMARIO, height=80)
    frame_titulo.pack(fill=tk.X, side=tk.TOP)
    frame_titulo.pack_propagate(False)
    
    lbl_titulo = tk.Label(
        frame_titulo,
        text="🎨 Generador QR",
        font=("Arial", 28, "bold"),
        bg=COLOR_PRIMARIO,
        fg="#ffffff"
    )
    lbl_titulo.pack(pady=15)

    frame_principal = tk.Frame(root, bg=COLOR_FONDO)
    frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    lbl_nombre = tk.Label(
        frame_principal,
        text="📝 Nombre:",
        font=("Arial", 12, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO_LABEL
    )
    lbl_nombre.grid(row=0, column=0, sticky="w", pady=10)
    
    insertar_nombre = tk.Entry(
        frame_principal,
        width=40,
        font=("Arial", 11),
        bg=COLOR_ENTRADA,
        fg=COLOR_TEXTO_LABEL,
        relief=tk.SOLID,
        borderwidth=2
    )
    insertar_nombre.grid(row=0, column=1, sticky="ew", pady=10, padx=10)

    lbl_datos = tk.Label(
        frame_principal,
        text="🔗 Texto o enlace:",
        font=("Arial", 12, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO_LABEL
    )
    lbl_datos.grid(row=1, column=0, sticky="w", pady=10)
    
    insertar_datos = tk.Entry(
        frame_principal,
        width=40,
        font=("Arial", 11),
        bg=COLOR_ENTRADA,
        fg=COLOR_TEXTO_LABEL,
        relief=tk.SOLID,
        borderwidth=2
    )
    insertar_datos.grid(row=1, column=1, sticky="ew", pady=10, padx=10)

    lbl_carpeta_titulo = tk.Label(
        frame_principal,
        text="📁 Carpeta de destino:",
        font=("Arial", 12, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO_LABEL
    )
    lbl_carpeta_titulo.grid(row=2, column=0, sticky="w", pady=10)
    
    lbl_carpeta = tk.Label(
        frame_principal,
        text="(Selecciona una Carpeta)",
        font=("Arial", 10),
        bg=COLOR_ENTRADA,
        fg=COLOR_TEXTO_LABEL,
        anchor="w",
        relief=tk.SOLID,
        borderwidth=2,
        padx=8,
        pady=8
    )
    lbl_carpeta.grid(row=2, column=1, sticky="ew", pady=10, padx=10)
    def seleccionar_carpeta():
        carpeta = filedialog.askdirectory(title="Seleccionar carpeta para guardar")
        if carpeta:
            lbl_carpeta.config(text=carpeta)
        else:
            lbl_carpeta.config(text="Elige la carpeta")
    
    btn_carpeta = tk.Button(
        frame_principal,
        text="📂 Elegir Carpeta",
        command=seleccionar_carpeta,
        font=("Arial", 11, "bold"),
        bg=COLOR_SECUNDARIO,
        fg="#ffffff",
        padx=15,
        pady=10,
        relief=tk.RAISED,
        cursor="hand2"
    )
    btn_carpeta.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")

    def generar():
        nombre = insertar_nombre.get().strip()
        datos = insertar_datos.get().strip()
        out_dir_text = lbl_carpeta.cget("text")
        out_dir = None if out_dir_text == "(Usa carpeta actual)" else out_dir_text
        
        if not nombre or not datos:
            messagebox.showerror("⚠️ Error", "Completa el nombre y el texto/enlace.")
            return
        try:
            ruta = generar_qr(nombre, datos, out_dir)
            messagebox.showinfo("✅ Éxito", f"QR guardado en:\n{ruta}")

            insertar_nombre.delete(0, tk.END)
            insertar_datos.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("❌ Error al generar QR", str(e))
    

    btn_generar = tk.Button(
        frame_principal,
        text="⭐ GENERAR QR",
        command=generar,
        font=("Arial", 14, "bold"),
        bg=COLOR_PRIMARIO,
        fg="#ffffff",
        padx=30,
        pady=15,
        relief=tk.RAISED,
        cursor="hand2"
    )
    btn_generar.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

    frame_principal.columnconfigure(1, weight=1)

    root.resizable(True, True)
    root.mainloop()