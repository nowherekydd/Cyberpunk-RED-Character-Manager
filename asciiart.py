#   _____ _____   _____ _      _____ 
#  / ____|  __ \ / ____| |    |_   _|
# | |    | |__) | |    | |      | |  
# | |    |  _  /| |    | |      | |  
# | |____| | \ \| |____| |____ _| |_ 
#  \_____|_|  \_\\_____|______|_____|
#
# Cyberpunk: RED CLI Character Manager
# by nowherekydd // v0d
# ASCII Holder

import txtfrm
import os

# Grabs terminal width
def get_terminal_width():
    try:
        return os.get_terminal_size().columns
    except OSError:
        # Default to 80 if getting terminal size fails
        return 80

# Centers text
def center_text(text, width):
    return text.center(width)

# Non-breaking space
nbsp = "\u00A0"

def charDiv():
    width = get_terminal_width()
    print(txtfrm.rollerheader(center_text(nbsp, width)))

def mainHeader():
    width = get_terminal_width()
    mainheaderASCII = [
    r"______      __                                __        ____  __________",
    r"  / ____/_  __/ /_  ___  _________  __  ______  / /___    / __ \/ ____/ __ \ ",
    r" / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_(_)  / /_/ / __/ / / / / ",
    r"/ /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< _    / _, _/ /___/ /_/ /  ",
    r"\____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_(_)  /_/ |_/_____/_____/   ",
    r"     /____/               /_/                                                ",
    r"Python-based CLI Character Manager by nowherekydd // v0d"
    ]

    charDiv()
    for line in mainheaderASCII:
        print(txtfrm.rollerheader(center_text(line, width)))
    charDiv()
    
#############################################################################################    
def charsheetheader():
    print(txtfrm.bgblack(txtfrm.cred(r"""                                                                                      
       ______      __                                __        ____  __________       
      / ____/_  __/ /_  ___  _________  __  ______  / /___    / __ \/ ____/ __ \      
     / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_(_)  / /_/ / __/ / / / /      
    / /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< _    / _, _/ /___/ /_/ /       
    \____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_(_)  /_/ |_/_____/_____/        
         /____/               /_/                                                     """)))

def charsheetdiv():
    chardiv = "▬▬ι═════════════════════════════════════════ι▬▬"
    chardCenter = chardiv.center(82)
    print(chardCenter)