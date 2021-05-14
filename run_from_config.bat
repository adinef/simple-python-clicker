@echo off

for /f "tokens=1,2 delims==" %%a in (config.ini) do (
if %%a==x set x=%%b
if %%a==y set y=%%b
if %%a==delay set delay=%%b
if %%a==window set window=%%b
)

echo X: %x%
echo Y: %y%
echo Delay: %delay%
echo Window: %window%

python C:\Users\fian\move_me\mc.py --x %x% --y %y% --delay %delay% --window %window%