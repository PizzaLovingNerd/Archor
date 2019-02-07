#Modules/Libraries
import os
import sys
import random
import time

# Functions:
def clear():  #Clears terminal
    if os.name == "nt": os.system("cls")
    else: os.system("clear")

# Version
version = "Alpha0.0.1"

# SPLASH SCREENS (Picks a random one)
splash = random.randint(1, 5)

if splash == 1:
    print("""
      ______                       __
     /      \                     |  \
    |  $$$$$$\  ______    _______ | $$____    ______    ______  
    | $$__| $$ /      \  /       \| $$    \  /      \  /      \ 
    | $$    $$|  $$$$$$\|  $$$$$$$| $$$$$$$\|  $$$$$$\|  $$$$$$\
    | $$$$$$$$| $$   \$$| $$      | $$  | $$| $$  | $$| $$   \$$
    | $$  | $$| $$      | $$_____ | $$  | $$| $$__/ $$| $$      
    | $$  | $$| $$       \$$     \| $$  | $$ \$$    $$| $$      
     \$$   \$$ \$$        \$$$$$$$ \$$   \$$  \$$$$$$  \$$ 
    """)
    
elif splash == 2:
    print("""       _               
         /\            | |               
        /  \   _ __ ___| |__   ___  _ __ 
       / /\ \ | '__/ __| '_ \ / _ \| '__|
      / ____ \| | | (__| | | | (_) | |   
     /_/    \_\_|  \___|_| |_|\___/|_|   
                                        
    """)

elif splash == 3:
    print("""
     ______     ______     ______     __  __     ______     ______    
    /\  __ \   /\  == \   /\  ___\   /\ \_\ \   /\  __ \   /\  == \   
    \ \  __ \  \ \  __<   \ \ \____  \ \  __ \  \ \ \/\ \  \ \  __<   
     \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
      \/_/\/_/   \/_/ /_/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 
                                                                  
    """)

elif splash == 4:
    print("""
     █████╗ ██████╗  ██████╗██╗  ██╗ ██████╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██║  ██║██╔═══██╗██╔══██╗
    ███████║██████╔╝██║     ███████║██║   ██║██████╔╝
    ██╔══██║██╔══██╗██║     ██╔══██║██║   ██║██╔══██╗
    ██║  ██║██║  ██║╚██████╗██║  ██║╚██████╔╝██║  ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝

    """)
elif splash == 5:
    print("""
     ▄▄▄       ██▀███   ▄████▄   ██░ ██  ▒█████   ██▀███  
    ▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒▓██ ▒ ██▒
    ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░▒██░  ██▒▓██ ░▄█ ▒
    ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░▒██▀▀█▄  
     ▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░░██▓ ▒██▒
     ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
      ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░   ░▒ ░ ▒░
      ░   ▒     ░░   ░ ░         ░  ░░ ░░ ░ ░ ▒    ░░   ░ 
          ░  ░   ░     ░ ░       ░  ░  ░    ░ ░     ░     
                       ░
    """)
print("Archor Version:" + version)
time.sleep(3)

# Welcome Screen + Script Name
print("Welcome to Archor, the easy to use Arch Linux install script generator. This was made by PizzaLovingNerd, Archor also uses code from NekoBit's Archkick\nNote, Archor is in beta. PizzaLovingNerd is not responsible for any damages caused to your system(s) from any generated script.\n\nWithout spaces, please type the name of the script (ex: MyArchInstaller)\n")
scriptname = input()

# Detects if scriptname.bash exists
if os.path.isfile(scriptname + ".bash") == True:
    print('Error: File already exists, please delete "' + scriptname + '.bash", or choose a different name for the script to continue.\n\nPlease press enter to close Archor')
    input()
    sys.exit()

# Generates scriptname.bash
print("\nGenerating new file")
script = open(scriptname + ".bash", "w")

# Checks if user wants base-devel
print("Do you want your script to install base-devel (select using numbers)\n\n1) Yes (Recommended)\n2) No\n")

base-devel? = input()

if base-devel? == 2:
    print("base-devel disabled")
    base-devel? = ""
    time.sleep(1)
else:
    print("base-devel enabled")
    base-devel? = "base-devel"
    time.sleep(1)
clear()

# Choose a desktop
print("""Now it is time to choose a DE/WM... (Select using numbers)
    1) Awesome
    2) bspwm
    3) Budgie (Will also install GNOME)
    4) Cinnamon
    5) Deepin
    6) dwm
    7) Enlightenment
    8) Fluxbox
    9) GNOME
    10) GNOME Flashback
    11) i3wm
    12) ion
    13) KDE Plasma
    14) Liri (AUR)
    15) Lumina (AUR)
    16) LXDE
    17) LXQT
    18) MATE
    19) Moksha (AUR)
    20) Openbox
    21) Pantheon
    22) Ratpoison
    23) Sugar
    24) theShell (AUR)
    25) Trinity
    26) Unity (Expirmental)
    27) Xfce
    28) xmonad
    29) No Desktop
"""
