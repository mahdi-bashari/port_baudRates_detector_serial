import serial
import time
import serial.tools.list_ports
import re
import unicodedata
import string

def Identicate_Port_and_baudrate(length=50):
    """
    Scan available serial ports and test common baud rates.

    This function automatically scans connected serial (COM) ports,
    tries multiple common baud rates, and returns any ports and
    baud rates that appear to be transmitting valid data.

    Parameter
    ----------
    length : int, optional
        Maximum length (in characters) of received data to consider valid. Default is 50.

    Returns
    -------
    tuple
        (ports_found, baud_rates_found, data)
        - ports_found: list of detected port names (e.g. ['COM3'])
        - baud_rates_found: list of working baud rates (e.g. [9600])
        - data: list of received data

    Example
    -------
    Python usage:

    >>> from identify_serial import Identicate_Port_and_baudrate
    >>> ports, baud_rates, data = Identicate_Port_and_baudrate()
    >>> print(ports, baud_rates, data)
    ['COM3'] [9600] ['F6 8E 87 32 FA 26 8E BE 208']
        Arduino test code:

    Arduino Test:
    ```cpp
    void setup() {
      Serial.begin(9600); // Change this to test other baud rates
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
    ```

    Upload this code to your Arduino board, then run the Python script.
    The function will automatically detect both the correct port
    and the baud rate.
    """
    ports_final=[]
    baud_rates_final=[]
    data_final=[]
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "USB Serial Device" in port.description:
            port_f = port.name
    ports_final.append(port_f)

    baud_rates = [9600, 19200, 38400, 57600, 115200, 230400]
    for rate in baud_rates:
        try:
            ser = serial.Serial(port_f, rate, timeout=1)
            time.sleep(1)
            data = ser.read_until('\n').decode(errors='ignore').strip()
            ser.close()
            t1= data.split('\r\n')[0]
            if len(t1)<length:
                baud_rates_final.append(rate)  
                data_final.append(t1)   
        except Exception as e:
            print(f"{rate}: {e}")
    return ports_final,baud_rates_final,data_final

#--------------------------------This part is intended to detect invalid or garbage data------------------------------------
# premis = has_unprintable_chars(data)
# print(premis)
# if not premis:
#     print(f"✅ baudrate = {rate} -- {data}")
# else:
#     print(f"❌{rate}")
# if data:
#     ser.readline().decode(errors='ignore').strip()
# def has_unprintable_chars(s: str):
#     ALLOWED_ASCII = set(string.printable)
#     for ch in s:
#         cat = unicodedata.category(ch)
#         if cat.startswith('C') or ch not in ALLOWED_ASCII:
#             return True
#     return False
