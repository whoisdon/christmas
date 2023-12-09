import os
import psutil
from datetime import timedelta
import time

RESET = chr(27) + "[0m"
BOLD_YELLOW = chr(27) + "[1;33m"
BOLD_GREEN = chr(27) + "[1;32m"
BOLD_RED = chr(27) + "[1;31m"
BOLD_BLACK = chr(27) + "[1;30m"
BOLD_BLUE = chr(27) + "[1;34m"
BOLD_MAGENTA = chr(27) + "[1;35m"
BOLD_CYAN = chr(27) + "[1;36m"
BOLD_WHITE = chr(27) + "[1;37m"
RGB_RED = chr(27) + "[38;5;196m"
RGB_GREEN = chr(27) + "[38;5;45m"

USER_EMAIL = "whoisdon"
OS_NAME = os.uname().sysname
KERNEL_VERSION = os.popen('uname -r').read().strip()
ARCHITECTURE = os.uname().machine
UPTIME = timedelta(seconds=psutil.boot_time())
MEMORY_USED = round(psutil.virtual_memory().used / (1024**2))
MEMORY_TOTAL = round(psutil.virtual_memory().total / (1024**2))

tree = f"""
{BOLD_YELLOW}      ☆       {RESET} {BOLD_GREEN} {USER_EMAIL}
{BOLD_GREEN}     /\\*\\     {RESET}  {BOLD_RED}{'—' * 23}
{BOLD_GREEN}    /\\O\\*\\   {RESET}   {BOLD_YELLOW}▪ os{RESET}     {BOLD_GREEN} {OS_NAME}
{BOLD_GREEN}   /*/\\/\\/\\   {RESET}  {BOLD_YELLOW}▪ kernel{RESET} {BOLD_GREEN} {KERNEL_VERSION}  
{BOLD_GREEN}  /\\O\\/\\*\\/\\  {RESET}  {BOLD_YELLOW}▪ arch{RESET}   {BOLD_GREEN} {ARCHITECTURE}
{BOLD_GREEN} /\\*\\/\\*\\/\\/\\  {RESET} {BOLD_YELLOW}▪ uptime{RESET} {BOLD_GREEN} {UPTIME}
{BOLD_GREEN} |O\\/\\/*/\\/O|  {RESET} {BOLD_YELLOW}▪ memory{RESET} {BOLD_GREEN} {MEMORY_USED}m / {MEMORY_TOTAL}m
{BOLD_YELLOW}      ||       {RESET}
{BOLD_YELLOW}      ||       {RESET} \x1b[0;30m███\x1b[0;31m███\x1b[0;32m███\x1b[0;34m███\x1b[0;35m███\x1b[0;36m███\x1b[0;37m███
"""

colors = [
    BOLD_GREEN,
    BOLD_YELLOW,
    BOLD_BLUE,
    BOLD_MAGENTA,
    BOLD_CYAN,
    BOLD_WHITE,
    RGB_RED,
    RGB_GREEN,
    BOLD_BLACK,
    BOLD_RED
]

def christmas():
    while True:
        for color in colors:
            tree_colored = tree.replace('*', f'{color}*{RESET}{BOLD_GREEN}')
            print(tree_colored)
            time.sleep(1)
            os.system('clear')
