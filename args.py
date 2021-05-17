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
    type=str, 
    default='PL CWX Desktop - Desktop Viewer'
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

def args():
    return __arg_parser.parse_args()