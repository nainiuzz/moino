"""
MAIN SCRIPT
"""
import requests
import os

import config
import colors as color

version_code = "1"
list_commands = ["block", "unblock7", "unblock10", "cmd"]

def main():
    os.system("clear")
    
    if not get_connect(config.SERVER):
        print(color.r + "Failed connecting to " + config.SERVER + color.w)
        raise SystemExit
        
    print(color.b + "For help on commands type '?'")
    getCommand(read_input())

def getCommand(command):
    if command in list_commands:
        try:
            response = requests.get(config.SERVER + "/edit_data.php?password=" + config.PASSWORD + "&function=" + command)
        
            if str(response) == "<Response [200]>":
                print(color.g + "Successfully!")
            else:
                print(color.r + "Failed!")
                
        except Exception:
        	print(color.r + "Failed connecting to " + config.SERVER)
        
    elif command in ["help", "?"]:
        print(color.y + "block " + color.w + "- lock computer")
        print(color.y + "execute <name> " + color.w + "- start program from 'WIN+R' with admin rights")
        print(color.y + "open <url> " + color.w + "- open URL in default browser")
        print(color.y + "write <text> " + color.w + "- write text")
        print(color.y + "echo <text> " + color.w + "- open window with your message")
        print(color.y + "reboot " + color.w + "- reboot computer")
    
    elif command == "exit":
        raise SystemExit
    
    else:
        print(color.r + "Command not found!")
        
    getCommand(read_input())

def read_input():
    return input(color.w + "> ")

def get_connect(server):
	try:
		response = requests.get(server)
		return True
	except Exception:
		return False

try:
    main()
except KeyboardInterrupt:
    raise SystemExit