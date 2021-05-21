from time import time, sleep
import sys, keyboard, pyautogui, args, threads

###----------------------------------------------Instruction-----------------------------------------------------------###
### Install dependencies: keyboard, pyautogui (python -m pip install ...)                                              ###
### Run <script name> --h to show help.                                                                                ###
### Required arguments: --x and --y to specify coordination. Run with '--mouse_info true' to show mouse coordinates.   ###
### Default interval/delay is 20 seconds, can be specified using --delay.                                              ###
### To exit click hotkey specified with --exit_key, defaulting to 'ctrl'.                                              ###

# Run mouse input check, incl. coordinates
if args.is_mouse_info_only():
    pyautogui.mouseinfo.mouseInfo()
    exit()

# Data holder
class ClickPoint(args.Coordinations):
    def __init__(self, coords: args.Coordinations, delay: int):
        super().__init__(defined_args = (coords.x(), coords.y()))
        self.delay = delay

    def delay(self):
        return self.delay

# Load click point object based on coordinates and specified delay
click_point = ClickPoint(args.get_coordinates(), args.get_delay())
if not click_point.is_defined():
    print("Please specify X and Y point of click.")
    exit()

# Mouse click function
def run_mouse_click(click_point):
    # Move to window of concern
    pyautogui.getWindowsWithTitle(args.get_window_title())[0].activate()
    # Move mouse to point of click
    pyautogui.moveTo(click_point.x(), click_point.y())
    # Click in coordinates location
    pyautogui.click()

# Threading loops
@threads.start_thread
@threads.daemon_thread
def main_loop():
    print('Starting auto mouse click...')
    while True:
        run_mouse_click(click_point)
        sleep(click_point.delay - time() % click_point.delay)

@threads.start_thread
@threads.simple_thread
def breakout_loop():
    # Sleep for thread to assure that mouse is moved before starting mouse position checking
    sleep(1)
    starting_mouse_pos = pyautogui.position()
    exit = False
    while not exit:
        if args.exit_on_mouse_move():
            current_mouse_pos = pyautogui.position()
            if current_mouse_pos.x != starting_mouse_pos.x or current_mouse_pos.y != starting_mouse_pos.y:
                exit = True
        if keyboard.is_pressed(args.exit_key()):
            exit = True
        if exit:
            print('Exiting...')

# Main loop is specified as Daemon thread to exit when user breaks out by hotkey (default 'ctrl')
main_loop()
breakout_loop()

