# GeneradorQR 🎨

Una aplicación simple y rápida para generar códigos QR con interfaz gráfica en Windows.

## Características

✨ **Interfaz intuitiva** — Diseño limpio con Tkinter.  
📱 **Generación rápida** — Convierte texto o enlaces en QR al instante.  
📁 **Selección de carpeta** — Elige dónde guardar tus QR (o usa carpeta actual).  
🎯 **Sin dependencias externas** — Todo incluido en el `.exe`.

## Instalación

### Opción 1: Ejecutable directo (Recomendado)
1. Descarga `GenerarQR.exe`
2. Ejecuta el archivo.
3. ¡Listo! No requiere instalación ni Python.


## Uso

1. Abre `GenerarQR.exe`.
2. Ingresa un **nombre** para el archivo QR.
3. Ingresa el **texto o enlace** que deseas codificar.
4. (Opcional) Haz clic en "Elegir carpeta" para seleccionar dónde guardar.
5. Haz clic en **"Generar QR"**.
6. El archivo `.png` se guardará en la carpeta seleccionada.

## Requisitos

- **Windows 7 o superior**.
- No requiere Python ni librerías adicionales.

## Desarrollo

### Estructura del proyecto
```
GeneradorQR/
├── main.py              # Punto de entrada
├── gui.py               # Interfaz gráfica
├── QR.py                # Lógica de generación de QR
├── requirements.txt     # Dependencias (para desarrollo)
├── Creador.bat          # Script para construir el .exe
├── generar_icono.py     # Script para generar icono
└── README.md            # Este archivo
```

### Construir el .exe localmente
```bash
# 1. Instala dependencias
python -m pip install -r requirements.txt

# 2. Ejecuta Creador.bat para generar GenerarQR.exe
.\Creador.bat
```

## Licencia

Este proyecto está bajo licencia **MIT**. Siéntete libre de usarlo, modificarlo y distribuirlo.

## Autor

Desarrollado con ❤️ por [Tu Nombre].

## Contribuciones

¿Ideas o mejoras? Abre un [Issue](../../issues) o envía un [Pull Request](../../pulls).

## Changelog

### v1.0 (2025-11-28)
- 🎉 Lanzamiento inicial.
- Generación de QR desde texto o enlaces.
- Interfaz gráfica con tkinter.
- Empaquetado como `.exe` sin dependencias.
