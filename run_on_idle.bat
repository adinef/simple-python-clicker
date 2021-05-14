@echo off

echo Provide click coordinates

set /p x=X coordinate: 
set /p y=Y coodinate: 
set /p delay=Delay [s]: 
python C:\Users\fian\move_me\mc.py --x %x% --y %y% --delay %delay%