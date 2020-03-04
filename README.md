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
    
  - Run the example and check if it is working.
