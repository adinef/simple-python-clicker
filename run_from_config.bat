@echo off

for /f "tokens=1,2 delims==" %%a in (config.ini) do (
if %%a==x set x=%%b
if %%a==y set y=%%b
if %%a==delay set delay=%%b
if %%a==window set window=%%b
if %%a==hotkey set hotkey=%%b
if %%a==exit_on_mouse_move set exit_on_mouse_move=%%b
)

echo X: %x%
echo Y: %y%
echo Delay: %delay%
echo Window: %window%
echo Hotkey: %hotkey%
echo Exit on mouse move: %exit_on_mouse_move%

python C:\Users\fian\move_me\mc.py --x %x% --y %y% --d %delay% --w %window% --e %hotkey% --mm %exit_on_mouse_move%