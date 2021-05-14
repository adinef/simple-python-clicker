from time import time, sleep
import sys, threading, keyboard, pyautogui, argparse

###----------------------------------------------Instruction-----------------------------------------------------------###
### Install dependencies: keyboard, pyautogui (python -m pip install ...)                                              ###
### Run <script name> --h to show help.                                                                                ###
### Required arguments: --x and --y to specify coordination. Run with '--mouse_info true' to show mouse coordinates.   ###
### Default interval/delay is 20 seconds, can be specified using --delay.                                              ###
### To exit click hotkey specified with --exit_key, defaulting to 'ctrl'.                                              ###

# Parsing arguments
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--x', help='X coordinate of mouse', type=int, default=None)
arg_parser.add_argument('--y', help='Y coordinate of mouse', type=int, default=None)
arg_parser.add_argument('--delay', help='Delay of click', type=int, default=20)
arg_parser.add_argument('--window', help='Window title', type=str, default='PL CWX Desktop - Desktop Viewer')
arg_parser.add_argument('--mouse_info', help='Show mouse info only', type=bool, default=False)
arg_parser.add_argument('--exit_key', help='Exit key for application to end clicking', type=str, default='ctrl')

args = arg_parser.parse_args()

# Run mouse input check, incl. coordinates
if args.mouse_info:
    pyautogui.mouseinfo.mouseInfo()
    exit()

# Load click coordinates
def fetch_click_coords():
    if args.x is not None and args.y is not None:
        return (args.x, args.y)
    else:
        raise Exception('No coordinates provided!')


# Data holder
class ClickPoint:
    def __init__(self, coords, delay):
        self.coords = coords
        self.delay = delay

    def x(self):
        return self.coords[0]
    
    def y(self):
        return self.coords[1]

# Load click point object based on coordinates and specified delay
try:
    click_point = ClickPoint(fetch_click_coords(), args.delay)
except Exception as exc:
    print(exc)
    exit()

# Mouse click function
def run_mouse_click(click_point):
    # Move to window of concern
    pyautogui.getWindowsWithTitle(args.window)[0].activate()
    # Move mouse to point of click
    pyautogui.moveTo(click_point.x, click_point.y)
    # Click in coordinates location
    pyautogui.click()

# Threading loops
def main_loop():
    print('Starting auto mouse click...')
    while True:
        run_mouse_click(click_point)
        sleep(click_point.delay - time() % click_point.delay)

def breakout_loop():
    while True:
        if keyboard.is_pressed(args.exit_key):
            break

# Main loop is specified as Daemon thread to exit when user breaks out by hotkey (default 'ctrl')
main_loop_thread = threading.Thread(target=main_loop)
main_loop_thread.setDaemon(True)

breakout_loop_thread = threading.Thread(target=breakout_loop)

main_loop_thread.start()
breakout_loop_thread.start()

