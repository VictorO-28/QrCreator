import qrcode
import os 
import re

_SAFE = re.compile(r'[^A-Za-z0-9 _.-]')

def _safe_nombre(nombre):
    s = (_SAFE.sub('',(nombre or '')).strip())
    return s or "qr"

def generar_qr(nombre, datos, out_dir=None):
    if not datos:
        raise ValueError("El parametro 'datos' es obligatorio")
    safe = _safe_nombre(nombre)
    out_dir = out_dir or os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    ruta = os.path.join(out_dir, f"{safe}.png")
    try: 
        qrcode.make(datos).save(ruta)
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar el QR en '{ruta}': {e}")
    return ruta