import machine, utime, bluetooth, ubluetooth
from micropython import const

_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)

def check_device(mac):
    if(mac == "24:DC:C3:98:B3:9E"):
        print("yay")

def bt_irq(event, data):
    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data
        pop = ':'.join(['%02X' % i for i in addr])
        print(pop)
        check_device(pop)
        

bt = ubluetooth.BLE()
bt.active(True)
bt.irq(bt_irq)
bt.gap_scan(0, 1280000, 11250, True)

print("Scanning started.")
