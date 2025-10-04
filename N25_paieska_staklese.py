import os
import threading
from enum import Enum
from colorama import Fore

DARK_GRAY = '\033[38;5;236m'

class SearchStatus(Enum):
    SEARCHING = "SEARCHING", Fore.LIGHTYELLOW_EX
    FOUND = "FOUND", Fore.LIGHTCYAN_EX
    NOT_FOUND = "NOT FOUND", DARK_GRAY
    EXCEPTION = "ERROR", Fore.LIGHTRED_EX

to_find = ""

paths = [
    {
        "name": "1. Venture E-310",
        "path": "//192.168.71.70/d/control/M1-C1/Data/cnc/mp4/A_SPECAI/n25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "2. Venture 22L",
        "path": "//192.168.71.91/mp4/_DARBINES_/_Specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "3. Venture 2M",
        "path": "//192.168.71.106/d$/ww4/a1/mp4/Programos_N/Specai/_IKELTA/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "5. BHT 500 NEW (CBG)",
        "path": "//192.168.71.66/d$/ww4/a1/mp4/Specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "6. BHX 055 NEW  (CBG)",
        "path": "//192.168.71.54/d$/control/m60-c1/data/cnc/mp4/specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "7. BHX055 NEW CNG",
        "path": "//192.168.71.31/d$/control/M60-C1/data/cnc/mp4/SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "8. BHX0551'os CNG",
        "path": "//192.168.71.128/d/control/m60-c1/data/cnc/mp4/SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "9. BHX 2'os CBG",
        "path": "//192.168.71.112/d/control/m60-c1/data/cnc/mp4/specai/n25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "10. BHT DRILLTEQ C-600",
        "path": "//192.168.71.34/d$/ww4/a1/mp4/SPECAI-------/n2500000",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "11. BHT 500",
        "path": "//192.168.71.92/d$/ww4/a1/Mpr/SPECAI--------/n25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "12. BAZ 723",
        "path": "//192.168.71.85/d/control/M1-C1/Data/cnc/mp4/A_SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "14. BHX DRILLTEQ V310",
        "path": "//192.168.71.100/d/control/M1-C1/Data/cnc/mp4/SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "15. CENTATEQ E-700",
        "path": "//192.168.71.61/d$/control/M1-C1/data/cnc/mp4/A_SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "16. BHX 055 DRILLTEQ",
        "path": "//192.168.71.36/d$/control/M60-C1/data/cnc/mp4/specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "17. BST 800",
        "path": "//192.168.71.33/d$/ww4/a1/Mpr/bst/specai",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "18. CENTATEQ E-700 II 23",
        "path": "//192.168.71.101/d$/control/M1-C1/Data/cnc/mp4/mp4/A_SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "19. BAZ CENTATEQ spec",
        "path": "//192.168.71.59/d$/control/M1-C1/Data/cnc/mp4/mp4/A_SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "20. CENTATEQ E-700 I 22",
        "path": "//192.168.71.55/d$/control/M1-C1/Data/cnc/mp4/mp4/A_SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "21. BHX 055 DRILLTEQ 2023",
        "path": "//192.168.71.109/d/control/m60-c1/data/cnc/mp4/specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "22. BHX su keitikliu",
        "path": "//192.168.71.78/d/control/m60-c1/data/cnc/mp4/SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "23. BHX Lenku",
        "path": "//192.168.71.82/d/control/m60-c1/data/cnc/mp4/specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "24. BHX (opera)",
        "path": "//192.168.71.111/d/control/m60-c1/data/cnc/mp4/SPECAI/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "BIESSE FTT insider",
        "path": "//192.168.71.90/p_p/prog/NARBUTAS Test",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "BIESSE VECTOR",
        "path": "//172.20.25.11/programs/Specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "BREMA 2.1",
        "path": "//192.168.71.51/bSolid/Programos/Specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "BREMA 2.2",
        "path": "//192.168.71.57/Programos/Specai/N25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },
    {
        "name": "Rover",
        "path": "//192.168.71.81/c/Users/xp600/Documents/bSolid/Specai/n25",
        "status": SearchStatus.SEARCHING,
        "found_root": "",
    },

]

def check_stakle(path, i):
    try:
        os.listdir(path["path"])
        for root, dirs, files in os.walk(path["path"]):
            for file in files: 
                if to_find.lower() in file.lower():
                    paths[i]["status"] = SearchStatus.FOUND
                    paths[i]["found_root"] = root.replace("/", '\\')
                    display_worker()
                    return

        paths[i]["status"] = SearchStatus.NOT_FOUND
        display_worker()
        return

    except Exception:
        paths[i]["status"] = SearchStatus.EXCEPTION
        display_worker()

def display_worker():
    printing = ""
    for stakle in paths:
        printing += f"{stakle["status"].value[1]}{stakle["name"]}: {stakle["status"].value[0]} {stakle["found_root"]}\n"
    os.system('cls')
    print(printing)

    print(Fore.RESET)


import subprocess
import time
import pyautogui

if __name__ == "__main__":
    os.system('cls')
    text_input = input("Įrasykite N25 kodą: ")
    to_find = text_input

    threads = []

    for i, stakle in enumerate(paths, 0):
        thread = threading.Thread(target=check_stakle, args=(stakle, i))
        threads.append(thread)

    for thread in threads: thread.start()
    for thread in threads: thread.join()

    input("Enter - eiti i folderius.")

    found_list = []

    for path in paths:
        if path["status"] == SearchStatus.FOUND:
            found_list.append(path)

    if len(found_list) > 0:
        subprocess.Popen(f'explorer "{found_list[0]["found_root"]}"')
        time.sleep(2.0)
    
    if len(found_list) > 1:
        for path in found_list[1:]:
            pyautogui.hotkey('ctrl', 't')
            time.sleep(0.5)
            
            pyautogui.hotkey('alt', 'd')
            time.sleep(0.5)
            
            pyautogui.write(path["found_root"], interval=0.01)
            time.sleep(0.5)
            
            pyautogui.press('enter')
            time.sleep(0.5)