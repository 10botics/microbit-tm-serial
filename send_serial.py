import serial
import time
import random

# Replace '/dev/ttyACM0' with the correct port for your system
# On Windows, it might be 'COM3', 'COM4', etc.
# On macOS, it might be '/dev/tty.usbmodemXXXX'
port = '/dev/ttyACM1'
baud_rate = 115200

try:
    # Open the serial port
    with serial.Serial(port, baud_rate, timeout=1) as ser:
        print(f"Connected to {port} at {baud_rate} baud rate.")
        
        while True:
            # Generate a random number
            random_number = random.randint(0, 9)
            
            # Send the random number to the micro:bit
            ser.write(f"{random_number}\n".encode('utf-8'))
            print(f"Sent: {random_number}")
            
            # Wait for a second before sending the next number
            time.sleep(1)

except serial.SerialException as e:
    print(f"Error: {e}")