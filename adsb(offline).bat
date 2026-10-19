@echo off

cd "C:\Users\user\Documents\Master Software\dump1090-rtl-sdr\"

start dump1090.bat
start VirtualRadar/VirtualRadar.exe
start http://127.0.0.1/VirtualRadar/desktop.html?notOnline=1

pause>nul