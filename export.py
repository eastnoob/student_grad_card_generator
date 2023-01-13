import os

# Initialize path 
path = ""

with open("path.txt", 'r') as f:
    path = f.read()

# Check if path exists 
while not os.path.exists(path):
    print("Path doesn't exist! Please adjust the path in path.txt")

    if input('Press Enter when path.txt is updated: ')  == '':
        with open("path.txt", 'r') as f:
            path = f.read()

# If path exists, open the path and execute the code 
if os.path.exists(path):
    import subprocess
    subprocess.Popen(path)
    
    import pyautogui
    pyautogui.hotkey('ctrl', 'shift', 'p')
    pyautogui.typewrite("markdown.marp.export") 
    pyautogui.press("enter") 
