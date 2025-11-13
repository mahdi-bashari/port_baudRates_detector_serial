# 🔌 Serial Port & Bund Rate Identifier

A simple and lightweight Python tool to **automatically detect the correct serial port and bund rate** for devices like **Arduino**, **ESP32**, **STM32**, and other serial-based boards.

---

## 🎯 Purpose

When working with serial devices (like Arduino), it's often unclear:
- which **COM port** the board is connected to, and  
- which **bund rate** is being used for communication.  

This script automatically scans available ports and tests common baud rates to identify the correct one — so you don’t have to guess or manually change settings.

---

## ⚙️ Features

✅ Automatically detects active USB serial ports  
✅ Tests multiple common baud rates  
✅ Reads incoming data to find the correct rate  
✅ Works with Arduino, ESP32, STM32, and similar devices  
✅ Pure Python implementation (no external tools)

---

## 🧠 How It Works

1. Lists available serial ports using `serial.tools.list_ports`.  
2. Filters ports that likely correspond to USB-serial devices (`USB Serial`, `ttyUSB`, `ttyACM`, etc.).  
3. Iterates through common baud rates:
9600, 19200, 38400, 57600, 115200, 230400
4. Returns detected ports, candidate baud rates, and data samples.

---

## 🖥️ Usage

### 1️⃣ Install dependencies:
!bash
pip install pyserial
### 2️⃣ Run the script:
python identify_serial.py
###  3️⃣Example output:

Detected Ports: ['COM3']

Detected Baud Rates (candidates): [115200]

Sample Data:

  [0] F6 8E 87 32 FA 26 8E BE 512

Python example:

from identify_serial import identify_port_and_baudrate

ports, baud_rates, data = identify_port_and_baudrate()

print("Ports:", ports)

print("Baud rates (candidates):", baud_rates)

print("Sample data:", data)

Arduino Example:
void setup() {

  Serial.begin(9600); // You can change to any other baud rate to test
  
}

void loop() {

  Serial.print("F6 ");
  
  Serial.print("8E ");
  
  Serial.print("87 ");
  
  Serial.print("32 ");
  
  Serial.print("FA ");
  
  Serial.print("26 ");
  
  Serial.print("8E ");
  
  Serial.print("BE ");
  
  Serial.println(analogRead(A0));
  
  delay(100);
  
}

## 💡Notes:

On macOS/Linux, the serial port descriptions differ — script attempts common identifiers (USB Serial, ttyUSB, ttyACM). Adjust as needed.

Default length checked for received data is 50 characters; change length parameter if needed.

If your device transmits only after a command, the script might not capture data — ensure the device is sending continuously while scanning 

## 👨‍💻 Author:

Mahdi Bashari

## 📜 License:

This project is released under the MIT License — free to use, modify, and distribute.

enjoy...
