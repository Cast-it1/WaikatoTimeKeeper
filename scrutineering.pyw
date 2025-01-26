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
    try:
        ser = serial.Serial(comport, baud, timeout=0.1)
    except serial.SerialException:
        print(f"Could not open {comport}. Exiting...")
        return
    
    list_data = []

    while True:
        # Read data from the serial port
        data = ser.readline().decode().strip()
        if data: # and data not in list_data:
            # Print the data to the console
            print(data)
            # Write the data using the keyboard
            keyboard.write(data)
            #list_data.append(data)

def open_timekeeper(filepath):
    subprocess.Popen(filepath, shell=True)

if __name__ == '__main__':
    # Start the serial reading in a separate thread
    serial_thread = threading.Thread(target=readSerial, args=('COM10', 115200))
    serial_thread.daemon = True
    serial_thread.start()
    
    # Open the xls file
    open_timekeeper('C:\Users\TimeKeeper\Documents\scrutinising.xls')
    
    # Start the Tkinter event loop
    window.mainloop()