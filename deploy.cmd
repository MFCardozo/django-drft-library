@echo off
setlocal enabledelayedexpansion


:: Configuración

set "APP_URL=http://localhost:8000/admin/"
set "WAIT_SECONDS=2"

if "%~1"=="" (
    echo Uso: %~nx0 ^<up^|down^>
    exit /b 1
)

if "%~1"=="up" (
    echo Running containers...
    docker compose up -d --build
    if errorlevel 1 (
        echo  Failed to initialized containers.
        exit /b 1
    )

    echo Waiting for containers...
    timeout /t 5 >nul

    set /a attempts=0
    :wait_loop
    curl -s -f "%APP_URL%" >nul 2>nul
    if errorlevel 1 (
        set /a attempts+=1
        if !attempts! GEQ 30 (
            echo.
            echo  Application failed to start!.
            echo Check logs with: docker compose logs -f
            exit /b 1
        )
        <nul set /p="."
        timeout /t %WAIT_SECONDS% >nul
        goto wait_loop
    )

    echo.
    echo  Deploy completed. Application running on:
    echo   %APP_URL%

    exit /b 0
)

if "%~1"=="down" (
    echo Stopping containers...
    docker compose down -v
    if errorlevel 1 (
        echo Failed to stop containers.
        exit /b 1
    )
    echo  Containers stopped and volumes removed.
    exit /b 0
)

echo Usage: %~nx0 ^<up^|down^>
exit /b 1