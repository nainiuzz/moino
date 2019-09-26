"""
MAIN SCRIPT
"""
import requests

import config
import colors as color

version_code = "1"
list_commands = ["block", "unblock7", "unblock10", "cmd"]

def main():
    print(color.b + "For help on commands type 'help'");
    getCommand(readInput())

def getCommand(command):
    if command in list_commands:
        response = requests.get(config.SERVER + "/edit_data.php?password=" + config.PASSWORD + "&function=" + command)
        
        if str(response) == "<Response [200]>":
            print(color.g + "Successfully!")
        else:
            print(color.r + "Failed!")
        
    elif command in ["help", "?"]:
        print("")
        print(color.y + "block " + color.w + "- lock computer")
        print(color.y + "unblock7 " + color.w + "- unlock computer with Windows 7")
        print(color.y + "unblock10 " + color.w + "- unlock computer with Windows 10")
        print(color.y + "cmd " + color.w + "- open cmd.exe with admin right")
        print("")
    
    elif command == "exit":
        raise SystemExit
    
    else:
        print(color.r + "Command not found!")
        
    getCommand(readInput())

def readInput():
    return input(color.g + "moino" + color.w + "> ")

try:
    main()
except KeyboardInterrupt:
    raise SystemExit