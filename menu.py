#!/usr/bin/python3
#Copyright 2023 AllHackingTools
#ReWritten by : Radius Y. Monim
#Github     : http://github.com/xerxes888                                                                           
import os
import time
import sys

os.system("clear")
os.system("cd && cd AllHackingTools")
os.system("bash Logo.sh")
os.system("bash src/MenuOps.sh")

op = str(input("Options: "))
if op == "1":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/IpMenu.py")
elif op == "2":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/RouterMenu.py")
elif op == "3":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/MailMenu.py")
elif op == "4":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/WebMenu.py")
elif op == "5":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/CamHackMenu.py")
elif op == "6":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/AndroidMenu.py")
elif op == "7":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/SQLinjectionMenu.py")
elif op == "8":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/SocialMenu.py")
elif op == "9":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/SpamMenu.py")
elif op == "10":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/AnalistickMenu.py")
elif op == "11":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/DarkSearchMenu.py")
elif op == "12":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/PhishingMenu.py")
elif op == "13":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/PassworldMenu.py")
elif op == "14":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/WordlistGeneratorMenu.py")
elif op == "15":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/XSSAttackMenu.py")
elif op == "16":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/discordMenu.py")
elif op == "17":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/telegramMenu.py")
elif op == "18":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/Other.py")
elif op == "19":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 Files/TermuxS.py")
elif op == "20":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("cd && cd AllHackingTools && python2 .settings/settingsMenu.py")
elif op == "21":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("clear && cd && cd AllHackingTools && bash .settings/LICENSE.sh && cd && cd AllHackingTools && python3 src/Timer2.py && python2 MainMenu.py")
elif op == "22":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 time.sleep(1)
 os.system("cd $HOME && git clone https://github.com/mishakorzik/AutoUpdateMyTools && cd AutoUpdateMyTools && bash AllHackingToolupdate.sh")
 #os.system("cd && cd AllHackingTools && bash src/UpdateTool.sh")
elif op == "23":
 os.system("bash src/Inf.sh")
 time.sleep(0.3)
 os.system("bash src/About.sh")
elif op == "13324715":
 print("[DEBUG] Developer mode successfully enabled!")
 time.sleep(0.8)
 os.system("cd && cd AllHackingTools && cd .settings && mv DesingLogo.py /data/data/com.termux/files/home/AllHackingTools/.temp/ && mv DesingMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/")
 print("[DEBUG] Please restart AllHackingTools!")
 os.system("cd && cd AllHackingTools && mv MainMenu.py /data/data/com.termux/files/home/AllHackingTools/.temp/temp && cd .settings && cd debug && cp MainMenu.py /data/data/com.termux/files/home/AllHackingTools/")
 print("[DEBUG] Warning! Customization has been disabled.")
elif op == "24":
 os.system("clear && cd && cd AllHackingTools && bash Logo.sh")
 print("\033[1;31;40mExiting System...")
 time.sleep(0.7)
else:
 print("\033[1;31;40mInvalid input. Reloading Tools")
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
