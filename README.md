# simple-python-clicker

# Simple application for in window clicking

Purpose of the application is to keep window / session active when user is on idle.\
Some computer's policies do not allow turning off sleep or force lock after a while.\
This simple app runs in terminal and keeps the session active.

## Dependencies

Python 3+

### Libraries

keyboard v0.13.5\
PyAutoGUI v0.9.52

## Necessary parameters

[--x $X$] - x position of mouse click.\
[--y $Y$] - y position of mouse click.\
[--window $WINDOW_TITLE$] - active window title\

## Optional parameters

[--e $EXIT_KEY$] - hotkey used to exit, default "ctrl".\
[--mi] - run mouse info only.\
[--mm] - exit application if mouse is moved by user.\
[--d $DELAY$] - specify delay of click, default 20.

## How to start

Install dependencies: keyboard, pyautogui (python -m pip install ...)\                                      
Run "mc.py --h to show help".\
\
run_from_config.bat contains example of how to run application, incl. running from configuration file 'config.ini' where basic parameters can be specified.
