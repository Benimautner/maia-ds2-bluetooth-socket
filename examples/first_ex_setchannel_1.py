#!/usr/bin/python3

import bluetooth

bd_addr = "AMPLIFIER_MAC_ADDR"
port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send(b'IR_NUM1')
sock.close()
