# maia-ds2-bluetooth-socket
Here are my findings of the reverse engineered Maia Ds2 bluetooth protocol


# Setup
You need a device running python3 that is able to connect to a bluetooth device.
I used a Raspberry Pi but theoretically it should work on any device.

Raspberry Pi:

  - Prerequisites:
    - bluetooth (pip3 install bluetooth)
    
  - Open a bluetooth connection to the Amplifier from your Raspberry:
    - Either using the GUI or using rfcomm
    - A more detailed explanation for rfcomm will come eventually.
    
  - Run the example and check if it is working.
    - Fill the mac address of your device in, then run the example.
    - The example basically just sends one of the commands to your amplifier. If your amplifier switches to channel 1 when running the example, then it does what it should do.
  - Commands
    - You can find a full list with all commands in the commands.txt file.
