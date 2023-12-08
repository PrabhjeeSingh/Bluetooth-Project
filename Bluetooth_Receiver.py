import machine, ubluetooth
from micropython import const


            
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)


def turn(val):
    if val:  # Turn LED on]
          led.value(1)
    else:
            led.value(0)


def check_device(adv_data,mac):
    if(mac == "24:DC:C3:98:B3:9E"):
        get_readable_data(str(bytearray(adv_data)))
        print("yay")
        turn(1)


def get_readable_data(string):
    split_payload = string.split('\\')
    name= split_payload[5][1:]
    payload = split_payload[7][3:-2]
    print("name=", name)
    print("Payload=",payload)
    turn(0)

def bt_irq(event, data):
    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data   
        pop = ':'.join(['%02X' % i for i in addr])
        try:
            check_device(adv_data,pop)
        except Exception as e:
            print(e)
      
        

        
        
led = machine.Pin(2, machine.Pin.OUT)


# Example usage

bt = ubluetooth.BLE()
bt.active(True)
bt.irq(bt_irq)
bt.gap_scan(0, 1280000, 11250, True)
turn(0)

print("Scanning started.")
