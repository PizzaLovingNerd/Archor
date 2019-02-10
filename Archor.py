# Modules/Libraries
import os
import sys
import random
import time

# Functions:
def clear():  #Clears terminal
    if os.name == "nt": os.system("cls")
    else: os.system("clear")

# Version
version = "Alpha 0.0.1"

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

clear()
if base-devel? == "2":
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
6) dwm (AUR)
7) Enlightenment
8) Fluxbox
9) GNOME
10) GNOME Flashback (Will also installed standard GNOME)
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
22) Rat0poison
23) Sway (i3wm with Wayland)
24) Sugar
25) theShell (AUR)
26) Trinity
27) Unity (Expirmental)
28) Window Maker
29) Xfce
30) xmonad
31) No Desktop

"""
desktop = input()
clear()
      
if desktop == "1": # Awesome
    print("Setting desktop to awesome (awesome choice btw)"
    desktop = "awesome"
            
elif desktop == "2": # Bspwm
    print("Setting desktop to bspwm")
    desktop = "bspwm"
            
elif desktop == "3": #Budgie (Asks if they want GNOME)
    clear()
    print("It's recommended to install GNOME with Budgie. Would you like to install GNOME?\n\n1) Install gnome\n2. Install gnome and gnome-extra\n3) Don't install gnome\n")
    desktop = input()
    clear()
          
    if desktop == "1":
        desktop = "budgie-desktop gnome"
        print("Setting desktop to budgie + gnome")
    elif desktop == "2":
        desktop = "budgie-desktop gnome gnome-extra")
        print("Setting desktop to budgie + gnome + gnome-extra")
    else:
        desktop = "budgie-desktop"
        print("Setting desktop to budgie")
      
elif desktop == "4": # Cinnamon
    print("Setting desktop to cinnamon (My favorite spice)")
    desktop = "cinnamon nemo-fileroller"
      
elif desktop == "5": # Deepin (Asks if they want deepin-extra)
    print("Would you like to install deepin-extra?\n\n1) Yes (Recommended)\n2) No")
    desktop = input()
      
    if desktop == "2":
        print("Setting desktop to deepin")
	desktop = "deepin"
    else:
	print("Setting desktop to deepin + deepin-extra")
        desktop = "deepin deepin-extra"
	  
elif desktop == "6": # dwm
    # Insert code here
	  
elif desktop == "7": # Enlightenment
    print("Setting desktop to enlightenment")
    desktop = "enlightenment terminology"

elif desktop == "8": # Fluxbox
    print("Setting desktop to fluxbox")
    desktop = "fluxbox"
	  
elif desktop == "9": # GNOME
    print("Would you like to install gnome-extra?\n\n1) Yes (Recommended)\n2) No")
    desktop = input()
      
    if desktop == "2":
        print("Setting desktop to gnome")
        desktop = "gnome"
    else:

	print("Setting desktop to gnome + gnome-extra")
        desktop = "gnome gnome-extra"
	  
elif desktop == "10": # GNOME FLashback
    print("Would you like to install gnome-extra?\n\n1) Yes (Recommended)\n2) No")
    desktop = input()
    
    if desktop == "2":
        print("Setting desktop to gnome-flashback + gnome")
	desktop = "gnome-flashback gnome"
    else:
	print("Setting desktop to gnome-flashback + gnome + gnome-extra")
        desktop = "gnome-flashback gnome gnome-extra"
	  
time.sleep(1)
      

