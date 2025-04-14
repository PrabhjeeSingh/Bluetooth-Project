# Bluetooth Traffic Signs Project

This project implements a Bluetooth Low Energy (BLE) based traffic sign system using ESP32 microcontrollers. The system allows for wireless communication between traffic signs and vehicles, enabling smart traffic management and safety features.

## Overview

The project consists of two main components:
1. **Traffic Sign Emitter**: An ESP32 device that broadcasts traffic sign information using BLE advertising
2. **Vehicle Receiver**: An ESP32 device that receives and processes the traffic sign information

<img src="https://github.com/user-attachments/assets/e84c26b5-e853-46b1-8cc5-d7ec8553562f" width=300px />

## Technical Details

### Hardware Requirements
- ESP32 Development Boards
- Power supply for the traffic signs
- Vehicle-mounted ESP32 for receiving signals

### Software Components
- `ble_advertising.py`: Handles BLE advertising payload generation and decoding
- `bluetooth_library.py`: Core Bluetooth functionality implementation
- `esp32advertise.py`: ESP32-specific advertising implementation
- `Bluetooth_Receiver.py`: Vehicle-side receiver implementation

### Features
- Custom BLE advertising payloads for traffic sign information
- Support for multiple service UUIDs
- Custom data field for additional sign information
- Efficient payload encoding/decoding
- Configurable advertising parameters

## Implementation Details

The system uses MicroPython's `ubluetooth` library for BLE communication. The traffic signs broadcast their information using BLE advertising packets, which include:
- Sign type/identifier
- Custom data payload
- Service UUIDs
- Device name

The vehicle receiver scans for these advertisements and processes the received data to display relevant information to the driver.

## Getting Started

1. Flash your ESP32 devices with MicroPython
2. Upload the required Python files to your devices
3. Configure the traffic sign emitter with appropriate sign information
4. Set up the vehicle receiver to scan for and process the advertisements

## Documentation

For detailed information about the Bluetooth implementation, refer to:
- [MicroPython ubluetooth Documentation](https://docs.micropython.org/en/v1.15/library/ubluetooth.html)
- ESP32 Manual (included in the project files)
- [Our implementation Documentation](https://docs.google.com/document/d/1PVvCgbzu3yBJQ18Tuipepngfwge-oK6GRvijR-YQE7k/edit?usp=sharing)

## Project Structure

```
.
├── README.md
├── ble_advertising.py      # BLE advertising payload handling
├── bluetooth_library.py    # Core Bluetooth functionality
├── esp32advertise.py       # ESP32-specific advertising
├── Bluetooth_Receiver.py   # Vehicle-side receiver
└── ESP 32 Manual.pdf       # Hardware documentation
```

## Contributing

Feel free to submit issues and enhancement requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the MIT License.
