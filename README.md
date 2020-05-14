# maia-ds2-bluetooth-socket
Here are my findings of the reverse engineered Maia Ds2 bluetooth protocol

The [Maia Ds2](https://www.project-audio.com/en/product/maia-ds2/) is an excellent audio amplifier. Unfortunately it is not easily controllable without using the proprietary app by pro-ject. This repository contains all nesessary information for one to send the reverse-engineered [commands](https://github.com/Benimautner/maia-ds2-bluetooth-socket/blob/master/commands.txt)  to the amplifier via a raspberry pi or some other bluetooth-capable device.

The commands just have to be sent through a bluetooth serial console. As a test, you can use an app such as [Serial Bluetooth Adapter](https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal) to send test commands to your device. For this to work, you have to be connected to your device.


# Example Setup
You need a device running python3 that is able to connect to a bluetooth device.
I used a Raspberry Pi but theoretically it should work on any device.

Raspberry Pi:

  - Prerequisites:
    - Raspberry Pi that is bluetooth-capable (RPI 3 or above)
    - bluetooth ("pip3 install bluetooth" in command line)
    
  - Open a bluetooth connection to the Amplifier from your Raspberry:
    - Either using the GUI or using rfcomm
    - A more detailed explanation for rfcomm can be found [here](https://gist.github.com/0/c73e2557d875446b9603).
    
  - Edit and run the example and check if it is working.
    - Fill in the mac address of your device, then run the example.
    - The example basically just sends one of the commands to your amplifier. If your amplifier switches to channel 1 when running the example, then it does what it should do.
  - Commands
    - You can find a full list with all commands in the [commands](https://github.com/Benimautner/maia-ds2-bluetooth-socket/blob/master/commands.txt) file.
