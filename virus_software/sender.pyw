"""
MOINO SENDER
"""
import serial
import time
import requests

SERVER = "https://site.ru/server_part"
PASSWORD = "pass"
PORT = 'COM11'

### API ###
def connected():
    return get_request(SERVER + "/edit_data.php", {"password": PASSWORD, "station": "connected"})

def disconnected():
    return get_request(SERVER + "/edit_data.php", {"password": PASSWORD, "station": "disconnected"})

def get_function():
    return get_request(SERVER + "/get_data.php", {"data": "function"})

def set_function(data):
    return get_request(SERVER + "/edit_data.php", {"password": PASSWORD, "function": data})

def get_request(server, dict_params):
    if dict_params != None:
        req = requests.get(server, params=dict_params)
        return req.text
    else:
        req = requests.get(server)
        return req.text

def comport():
    return 'COM11'

def handler(data):
    if data != "NONE":
        conn = serial.Serial(
            port = PORT,\
            baudrate = 9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=10)
        conn.write(data.encode())
        set_function("NONE")
        
### API ###


### MAIN ### 
def main():
    connected()
    PORT = comport()
    
    while True:
        data = get_function()
        handler(data)
        time.sleep(5)

try:
    main()
except KeyboardInterrupt:
    disconnected()
### MAIN ###

# KAK  TEBE TAKOE ? #