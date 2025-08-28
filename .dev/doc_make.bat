@echo off
setlocal enabledelayedexpansion

rem Get current path to .bat
set "CURRENT_DIR=%~dp0"
rem Remove final backslash
set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

:loop
rem Check if current folder is called pythonLP
for %%I in ("%CURRENT_DIR%") do set "DIRNAME=%%~nxI"

if /i "%DIRNAME%"=="pythonLP" (
    cd /d "%CURRENT_DIR%"
    goto run_script
) else (
    rem Check parent
    for %%I in ("%CURRENT_DIR%\..") do set "CURRENT_DIR=%%~fI"
    rem Exit if arrived to root
    if "%CURRENT_DIR%"=="%CURRENT_DIR%\.." (
        echo Folder pythonLP not found
        exit /b 1
    )
    goto loop
)

:run_script
call "%CURRENT_DIR%\.venv\Scripts\activate.bat"

REM Check Sphinx
if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)

REM Folders
set SOURCEDIR=".\libsLP\appLP\docs\source"
set BUILDDIR=".\libsLP\appLP\docs\build"

REM Check if sphinx-build is available
%SPHINXBUILD% --version >NUL 2>NUL
if errorlevel 9009 (
    echo.
    echo The 'sphinx-build' command was not found. Make sure you have Sphinx
    echo installed and added to your PATH.
    echo Alternatively, set the SPHINXBUILD environment variable to the full path.
    echo.
    exit /b 1
)

REM Build HTML
echo Building HTML documentation...
%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR%\html
if errorlevel 1 (
    echo HTML build failed!
    goto end
)

REM Build LaTeX PDF
echo Building LaTeX documentation...
%SPHINXBUILD% -b latex %SOURCEDIR% %BUILDDIR%\latex
if errorlevel 1 (
    echo LaTeX build failed!
    goto end
)

REM Compile PDF from LaTeX
echo Compiling PDF from LaTeX...
pushd %BUILDDIR%\latex
make all-pdf
popd

echo.
echo Build finished successfully!
:end
popd
pause