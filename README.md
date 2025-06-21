# Local-KeyLogger  

# Keylogger Project

This is a simple keylogger to track the local laptop keylog. The repository contains a Python script (`.pyw`) and its compiled executable (`.exe`) version. The keylogger captures keystrokes and logs them to a text file (`keylog.txt`) in real-time, running silently in the background on your local laptop, you just need to run the .exe file.

## Files
- `keylogger.pyw`: The Python source code for the keylogger.
- `keylogger.exe`: The compiled executable for Windows, runs without a console window.

## Features
- Logs keystrokes continuously to `keylog.txt` in the same directory.
- Runs in the background (no visible window).
- Special keys:
  - Space is logged as a space character.
  - Enter creates a new line.
  - Other special keys (e.g., Shift, Ctrl) are ignored.
- Stops when the ESC key is pressed (the .pyw using the cmd and the .exe in silent).

## Requirements
To run or modify the `.pyw` file:
- Python 3.x (tested with Python 3.13)
- `keyboard` module: Install with `pip install keyboard`
- Windows, Linux, or macOS (`.exe` is Windows-only)


## Installation and Usage

### Running the Executable (`.exe`)
1. Download `keylogger.exe` from this repository.
2. Place it in a directory on your laptop where you have write permissions.
3. **Note**: Add an exception for `keylogger.exe` in Windows Defender (Virus & Threat Protection > Manage Settings > Add or remove exclusions > Add an exclusion > File > select `keylogger.exe`) to prevent it from being deleted while running in the background.
3. Double-click `keylogger.exe` to start tracking your local keylog.
4. Type as usual check `keylog.txt` in the same directory for the log.
5. Press ESC to stop the keylogger (it will exit silently).

### Running the Script (`.pyw`)
1. Clone or download this repository.
2. Install the required module:
   ```bash
   pip install keyboard
