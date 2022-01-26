@echo off

set /p sc="Delete bin/ folder? [y/n] :> "

if "%sc%"=="y" goto delbin
goto main

:delbin
del /S bin
@RD /Q bin
rmdir bin
md bin

:: Going to Bin Folder
cd bin

  :: Build Logs -- USELESS LOL
  ::md logs
  ::cd logs
  ::echo D|xcopy "../../logs/*" "bin" /E
  ::cd ..

:: Build Source Folder
:main

md src
cd src
  ::echo D|xcopy "../../src/*" "bin/" /E :: SHITTY
robocopy /S "..\..\..\src" "..\..\bin\src"

cd ..
cd ..
::

:: Build Process
if "%1"==nul goto BUILD

:DEBUG_BUILD
pyinstaller --noconfirm --onefile --console --icon "../src/debug_stpyi.ico"  "..\main.py"
goto :n

:BUILD
pyinstaller --noconfirm --onefile --windowed --icon "../src/stpyi.ico"  "..\main.py"
goto :n
::

:: Little things
:n
cd bin
move "../dist/main.exe" ""
ren "main.exe" "CryPe.exe"

cd src
echo Y|rmdir "__pycache__"
goto :exit


:: EXIT
:exit
cd ..
cd ..
@echo on