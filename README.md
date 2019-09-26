# Moino
Moino - software for the controlled BadUSB. The list of software includes firmware for ATmega32u4 on Arduino, server part in PHP, control panel in Python.

# Firmware
The firmware is written in Arduino C++. When you connect the Board to the USB port of the computer, it goes into standby mode(20-60 seconds), then checks whether the necessary software on the computer to receive data from the server and send them to the Board, if not, it installs via cmd.exe.

# Virus software
Installed from the firmware receives data from the server, giving them a com port badusb, contains a string with the name of the desired function.

# Control panel
The control panel is written by Python 3, runs on all platforms. It has its own "terminal", commands 'help', 'exit', and other commands coincide with the names of functions.

![alt-text](https://sun9-53.userapi.com/c858336/v858336843/88953/JFnCxFOQGPE.jpg)
