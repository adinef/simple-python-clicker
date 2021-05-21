import argparse

__arg_parser = argparse.ArgumentParser()

__arg_parser.add_argument(
    '--x', 
    help='X coordinate of mouse', 
    type=int, 
    default=None
    )

__arg_parser.add_argument(
    '--y', 
    help='Y coordinate of mouse', 
    type=int, 
    default=None
    )

__arg_parser.add_argument(
    '--delay', '--d', 
    help='Delay of click', 
    type=int, 
    default=20
    )

__arg_parser.add_argument(
    '--window', '--w', 
    help='Window title', 
    type=str
    )

__arg_parser.add_argument(
    '--mouse_info', '--mi', 
    help='Show mouse info only',
    action="store_true"
    )

__arg_parser.add_argument(
    '--exit_key', '--e', 
    help='Exit key for application to end clicking', 
    type=str, 
    default='ctrl'
    )

__arg_parser.add_argument(
    '--exit_on_mouse_move', '--mm', 
    help='Exit on mouse move',
    action="store_true"
    )

__arguments = __arg_parser.parse_args()


class Coordinations:
    def __init__(self, args: dict = None, defined_args: tuple = None):
        if defined_args is not None:
            self.coords: tuple = defined_args
        else:
            self.coords: tuple = (args.x, args.y)

    def is_defined(self):
        return self.x() is not None and self.y() is not None

    def x(self):
        return self.coords[0]
    
    def y(self):
        return self.coords[1]

def is_mouse_info_only():
    return __arguments.mouse_info


def get_coordinates():
    return Coordinations(__arguments)


def get_delay():
    return __arguments.delay

def get_window_title():
    return __arguments.window

def exit_on_mouse_move():
    return __arguments.exit_on_mouse_move

def exit_key():
    return __arguments.exit_key