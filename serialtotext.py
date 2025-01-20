import subprocess
import serial
import keyboard
import tkinter as tk
import threading

# 
# Create the main window
window = tk.Tk()
window.geometry("150x50")

# Add an exit button to the window
exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack()

def readSerial(comport, baud):
    # Open the serial port
    ser = serial.Serial(comport, baud, timeout=0.1)

    while True:
        # Read data from the serial port
        data = ser.readline().decode().strip()
        if data:
            # Print the data to the console
            print(data)
            # Write the data using the keyboard
            keyboard.write(data)
            # Simulate pressing 'home' and 'right' keys
            keyboard.press_and_release('down, home, right')

def open_xlsx_file(filepath):
    subprocess.Popen(['start', 'excel', filepath], shell=True)

if __name__ == '__main__':
    # Start the serial reading in a separate thread
    serial_thread = threading.Thread(target=readSerial, args=('COM4', 115200))
    serial_thread.daemon = True
    serial_thread.start()
    
    # Open the xlsx file
    open_xlsx_file('./Scrutinize check.xlsx')
    
    # Start the Tkinter event loop
    window.mainloop()
