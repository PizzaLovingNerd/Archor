# Modules/Libraries and some Variables
import os
import sys
import random
import time
import string   

# Functions:
def clear():  #Clears terminal
    if os.name == "nt": os.system("cls")
    else: os.system("clear")
AUR = 0

# Version
version = "Commit 20"

# SPLASH SCREENS (Picks a random one)
splash = random.randint(1, 4)

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
    print("""
                        _               
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
print("Archor Version: " + version)
time.sleep(1)
clear()

# Welcome Screen + Script Name
print("Welcome to Archor, the easy to use Arch Linux install script generator.\nThis was made by PizzaLovingNerd, Archor also uses code from NekoBit's Archkick\nNote, Archor is in alpha. PizzaLovingNerd is not responsible for any damages caused to your system(s) from any generated script.\n\nWithout spaces (or special charactors), please type the name of the script (ex: MyArchInstaller)\n")
scriptname = input()

# Detects if scriptname.bash exists
if os.path.isfile(scriptname + ".bash") == True:
    print('Error: File already exists, please delete "' + scriptname + '.bash", or choose a different name for the script to continue.\n\nPlease press enter to close Archor\n')
    input()
    sys.exit()

# Generates scriptname.bash
print("\nGenerating new file")
script = open(scriptname + ".bash", "w")
step = 1

while True: #Creates a forever loop (used for back feature)

    if step == 1:
        # Checks if user wants base-devel
        print("Do you want your script to install base-devel (select using numbers)\n\n1) Yes (Recommended)\n2) No")

        base = input()

        clear()
        if base == "2":
            print("base-devel disabled")
            base = "base"
            time.sleep(1)
        else:
            print("base-devel enabled")
            base = "base base-devel"
            time.sleep(1)
        step = 2
        clear()

    if step == 2:
        # Choose a desktop
        print("""Choose a DE/WM... (Select using numbers) (Note: AUR packages currently do not work)
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
        11) i3-gaps
        12) i3wm
        13) ion
        14) KDE Plasma
        15) Liri (AUR)
        16) Lumina (AUR)
        17) LXDE
        18) LXQT
        19) MATE
        20) Moksha (AUR)
        21) Openbox
        22) Pantheon (AUR)
        23) Ratpoison
        24) Sway (i3wm with Wayland)
        25) Sugar
        26) theShell (AUR)
        27) Trinity
        28) Unity (Expirmental)
        29) Window Maker (AUR)
        30) Xfce
        31) xmonad
        32) No Desktop

        b) Back

        """)

        desktop = input()
        clear()

        if desktop == "b": # Back
            step = 1

        if desktop == "1": # Awesome
            print("Setting desktop to awesome (awesome choice btw)")
            desktop = "awesome"

        elif desktop == "2": # Bspwm
            print("Setting desktop to bspwm")
            desktop = "bspwm"

        elif desktop == "3": #Budgie (Asks if they want GNOME)
            clear()
            print("It's recommended to install GNOME with Budgie. Would you like to install GNOME?\n\n1) Install gnome \n2. Install gnome and gnome-extra (Recommended) \n3) Don't install gnome\n") # Install Budgie with GNOME
            desktop = input()
            clear()

            if desktop == "1":
                desktop = "budgie-desktop gnome"
                print("Setting desktop to budgie + gnome")
            elif desktop == "2":
                desktop = "budgie-desktop gnome gnome-extra"
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
                print("Setting desktop to deepin") # Just Deepin
                desktop = "deepin"
            else:
                print("Setting desktop to deepin + deepin-extra") # Deepin Extra
                desktop = "deepin deepin-extra"

        elif desktop == "6": # dwm
            AUR = 1
            print("AUR package, not added yet")

        elif desktop == "7": # Enlightenment
            print("Setting desktop to enlightenment")
            desktop = "enlightenment terminology"

        elif desktop == "8": # Fluxbox
            print("Setting desktop to fluxbox")
            desktop = "fluxbox"

        elif desktop == "9": # GNOME
            print("Would you like to install gnome-extra?\n\n1) Yes (Recommended)\n2) No") # Install gnome-extra?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to gnome") # Install just GNOME
                desktop = "gnome"
            else:
                print("Setting desktop to gnome + gnome-extra") # Installing GNOME-extra
                desktop = "gnome gnome-extra"

        elif desktop == "10": # GNOME Flashback
            print("Would you like to install gnome-extra?\n\n1) Yes (Recommended)\n2) No") # Install gnome-extra?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to gnome-flashback + gnome") # Install just GNOME
                desktop = "gnome-flashback gnome"
            else:
                print("Setting desktop to gnome-flashback + gnome + gnome-extra") # Install gnome-extra
                desktop = "gnome-flashback gnome gnome-extra"

        elif desktop == "11": # i3-gaps
            print("Setting desktop to i3-gaps")
            desktop  = "i3-gaps"

        elif desktop == "12": # i3wm
            print("Setting desktop to i3-gaps")
            desktop  = "i3wm"

	    elif desktop == "13": # ion
            AUR = 1
            print("AUR package, not added yet")

	    elif desktop == "14": # KDE Plasma
            print("Would you like to install kde-applications?\n\n1) Yes (Recommended)\n2) No") # Install kde-applications?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to plasma") # Install just GNOME
                desktop = "plasma"
            else:
                print("Setting desktop to plasma + kde-applications") # Install gnome-extra
                    desktop = "plasma kde-applications"

	    elif desktop == "15": # Liri
            AUR = 1
            print("AUR package, not added yet")

	    elif desktop == "16": # Lumina
			AUR = 1
            print("AUR package, not added yet")

	    elif desktop == "17": # LXDE
	        print("Setting desktop to lxde")
	        desktop = "lxde"

	    elif desktop == "18": # LXQT
            print("Setting desktop to lxqt")
	        desktop = "lxqt breeze-icons"

	    elif desktop == "19": # MATE
            print("Would you like to install mate-extra?\n\n1) Yes (Recommended)\n2) No") # Install mate-extra?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to mate") # Install just MATE
                desktop = "mate"
            else:
                print("Setting desktop to mate + mate-extra") # Installing MATE-extra
                desktop = "mate mate-extra"

	    elif desktop == "20": # Moksha
            AUR = 1
            print("AUR package, not added yet") 

	    elif desktop == "21": # OpenBox
			print("Setting desktop to Openbox")
	    	desktop = "openbox"

        elif desktop == "22": # Pantheon
			AUR = 1
            print("AUR package, not added yet")

        elif desktop == "23": # Ratpoison
            print("Setting desktop to Ratpoison")
		    desktop = "ratpoison"

        elif desktop == "24": # Sway
            print("Setting desktop to Sway")
            desktop = "sway"

        elif desktop == "25": # Sugar
            print("Would you like to install sugar-fructice?\n\n1) Yes (Recommended)\n2) No") # Install sugar-fructice?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to sugar") # Install just Sugar
                desktop = "sugar sugar-runner webkit2gtk"
            else:
                print("Setting desktop to sugar + sugar-fructice") # Installing Sugar Fructice
                desktop = "sugar sugar-runner sugar-fructice webkit2gtk"
				
		elif desktop == "26": # theShell
            AUR = 1
            print("AUR package, not added yet")
			
		elif desktop == "27": # Trinity
			print("Setting desktop to Trinity")
			
			# Add
			# [trinity]
			# Server = https://repo.nasutek.com/arch/contrib/trinity/x86_64
			# to /etc/pacman.conf
			
			desktop = "trinity"
			
		elif desktop == "28": # Unity 
			print("Setting desktop to Unity")
			
			# Commands for Unity
			# git clone https://github.com/chenxiaolong/Unity-for-Arch.git
			# cd Unity-for-Arch
			# makepkg -sci
			# Other stuff to install
			
            print("It's recommended to install GNOME with Unity. Would you like to install GNOME?\n\n1) Install gnome \n2. Install gnome and gnome-extra (Recommended) \n3) Don't install gnome\n") # Install Unity with GNOME
            desktop = input()
            clear()

            if desktop == "1":
                desktop = "unity-gnome"
                print("Setting desktop to unity + gnome")
            elif desktop == "2":
                desktop = "unity-gnome-extra"
                print("Setting desktop to unity + gnome + gnome-extra")
            else:
                desktop = "unity"
                print("Setting desktop to unity")
			
		elif desktop == "29": # Window Maker
			AUR = 1
            print("AUR package, not added yet")
            
        elif desktop == "30": # xfce4
			print("Would you like to install xfce4-goodies?\n\n1) Yes (Recommended)\n2) No") # Install xfce4-goodies?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to xfce4") # Install just MATE
                desktop = "xfce4"
            else:
                print("Setting desktop to xfce4 + xfce4-goodies") # Installing MATE-extra
                desktop = "xfce4 xfce4-goodies"
                
        elif desktop == "31": #xmonad
			print("Would you like to install xmonad?\n\n1) Yes (Recommended)\n2) No") # Install xmodad?
            desktop = input()

            if desktop == "2":
                print("Setting desktop to xmonad") # Install just xmonad
                desktop = "xmonad"
            else:
                print("Setting desktop to xmonad + xmonad-contrib") # Installing xmonad
                desktop = "xmonad xmonad-contrib"
                
        elif desktop == "b": step = 1 # Back
        
        else:
			print("Setting desktop to none")
			desktop = ""
		
		time.sleep(1)
		clear()
		step = 3
			
	if step == 3:
        # Choose a browser
        print("""Choose a Web Browser... (Select using numbers) (Note: AUR packages currently do not work)
        1) Basilisk (AUR)
        2) Beaker Broswer (AUR)
        3) Brave (AUR)
        4) Crusta (AUR)
        5) Chromium
        6) Cliqz (AUR)
        7) Cyberfox (AUR)
        8) Dooble (AUR)
        9) Eolie
        10) Eric
        11) Falkon
        12) Firefox
        13) GNOME Web (Epiphany) (Preinstalled with GNOME)
        14) GNU IceCat (AUR)
        15) Google Chrome (AUR)
        16) Inox (AUR)
        17) Iridium (AUR)
        18) Konqueror
        19) Liri (AUR)
        20) Midori
        21) Min
        22) Opera
        23) Otter (AUR)
        24) Palemoon
        25) qutebrowser
        26) Seamonkey
        27) Slimjet (AUR)
        28) Surf
        29) Ungoogled Chromium (AUR)
        30) Vivaldi (AUR)
        31) Waterfox (AUR)
        32) No Web browser
        b) Back
        """)
        
		browser = input("")
		clear()
		
		if browser == "1": # Basilisk
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "2": # Beaker
			AUR = 1
			print("AUR Package, not added yet")
		
		if browser == "3": # Brave
			AUR = 1
			print("AUR Package, not added yet")
		
		if browser == "4": # Crusta
			AUR = 1
			print("AUR Package, not added yet")
		
		if browser == "5": # Chromium
			print("Setting browser to Chromium")
			browser = "chromium"
		
		if browser == "6": # Cliqz
			AUR = 1
			print("AUR Package, not added yet")
		
		if browser == "7": # Cyberfox
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "8": # Dooble
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser = "9": # Eolie
			print("Setting browser to Eolie")
			browser = "eolie"
			
		if browser == "10": # Eric
			print("Setting browser to eric")
			browser = "eric"
			
		if browser == "11": # Falkon
			print("Setting browser to Falkon")
			browser = "falkon"
			
		if browser == "12": # Firefox
			print("Setting browser to Firefox")
			browser = "firefox"
		
		if browser == "13": # GNOME Web
			print("Setting browser to GNOME Web")
			browser = "epiphany"
			
		if browser == "14": # IceCat
			AUR = 1
			print("AUR Package, not added yet")
		
		if browser == "15": # Chrome
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "16": # Inox
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "17": # Iridium
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "18": # Konqueror
			print("Setting browser to Konqueror")
			browser = "konqueror"
			
		if browser == "19": # Liri
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "20": # Midori
			print("Setting browser to Midori")
			browser = "midori"
			
		if browser == "21": # Min
			print("Setting browser to Min")
			browser = "min"
		
		if browser == "22": # Opera
			print("Setting browser to Opera")
			browser = "opera"
			
		if browser == "23": # Otter
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "24": # Palemoon
			print("Setting browser to Palemoon")
			browser = "palemoon"
			
		if browser == "25": # qutebrowser
			print("Setting browser to qutebrowser")
			browser = "qutebrowser"
		
		if browser == "26": # Seamonkey
			print("Setting browser to Seamonkey")
			browser = "seamonkey"
			
		if browser == "27": # Slimjet
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "28": # Surf
			print("Setting browser to surf")
			browser = "surf"
			
		if browser == "29": # Ungoogled Chromium
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "30": # Vivaldi
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "31": # Waterfox
			AUR = 1
			print("AUR Package, not added yet")
			
		if browser == "b": step = 2 # Back
		
		else:
			print("Setting browser to none")
			desktop = ""
		
		time.sleep(1)
		clear()
		step = 4
		
	if step == 4: # Other Programs, Not functional yet
		step = 5
		
	if step == 5: # AUR Stuff
		if AUR != 1:
			print("""Would you like to install an AUR helper?
			1) Yes
			2) No
			b) Back
			""")
			
			aur = input()
			
			if aur == b:
				step = 4
			elif aur == 1: 
				print("AUR Enabled")
				AUR == 1:
				step = 6
			else: 
				print("AUR Disabled")
				AUR = 0
				step = 6
				
	if step == 6: # AUR Helper
		if AUR == 1:
			print("""Please choose an AUR helper
			
			1) pacaur
			2) pikaur
			3) trizen
			4) yay
			""")
			helper = input()
			
			
			
		
