@echo off
REM 
REM 
pause
necho Instalacion completada en %INSTALLDIR%.powershell -NoProfile -Command "$W = New-Object -ComObject WScript.Shell; $s = $W.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\\GenerarQR.lnk'); $s.TargetPath = '%INSTALLDIR%\\GenerarQR.exe'; $s.WorkingDirectory = '%INSTALLDIR%'; $s.Save()"
necho Creando acceso directo en el Escritorio del usuario...)  set "INSTALLDIR=%LocalAppData%\Programs\GenerarQR"
  
  powershell -NoProfile -Command "if(-not (Test-Path '%INSTALLDIR%')){ New-Item -ItemType Directory -Path '%INSTALLDIR%' | Out-Null }"
  copy /Y "dist\GenerarQR.exe" "%INSTALLDIR%\GenerarQR.exe" >nul  echo No se pudo copiar en Program Files, usando instalación por usuario en LocalAppData.copy /Y "dist\GenerarQR.exe" "%INSTALLDIR%\GenerarQR.exe" >nul 2>&1
nif %ERRORLEVEL% NEQ 0 (powershell -NoProfile -Command "if(-not (Test-Path '%INSTALLDIR%')){ New-Item -ItemType Directory -Path '%INSTALLDIR%' | Out-Null }"
nrem Intentar copiar a Program Files (requiere elevacion). Si falla, usar LocalAppData.
nset "INSTALLDIR=%ProgramFiles%\GenerarQR"
necho Copiando GenerarQR.exe a %INSTALLDIR% ...)  python -m pip install -r requirements.txt --quiet  echo Instalando dependencias via pip (requiere Python en PATH)...
n:: Opcion para instalar dependencias (solo si NO usaste --onefile)
nif "%1"=="--install-deps" ()  exit /b 1  pause  echo ERROR: dist\GenerarQR.exe no encontrado. Ejecuta Creador.bat primero.nif not exist "dist\GenerarQR.exe" (