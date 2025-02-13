# import pyautogui
# import time

# # Set the interval in seconds
# interval = 5  # Change tab every 5 seconds

# print("Auto tab switcher started. Press Ctrl+C to stop.")

# try:
#     while True:
#         # Simulate Ctrl+Tab to switch tabs
#         pyautogui.hotkey('ctrl', 'tab')  # Use 'command', 'option', 'right' for Mac
#         time.sleep(interval)  # Wait for the specified time
# except KeyboardInterrupt:
#     print("Auto tab switcher stopped.")

# import pyautogui
# import time
# import keyboard

# # Set the interval in seconds
# interval = 5  # Change tab every 5 seconds
# running = True  # Flag to control the loop

# print("Auto Tab Switcher Started. Press 'p' to pause, 'r' to resume, and 'q' to quit.")

# while True:
#     if keyboard.is_pressed('p'):  # Pause switching
#         print("Paused. Press 'r' to resume.")
#         while keyboard.is_pressed('p'):  # Wait until 'p' is released
#             time.sleep(0.1)
#         while not keyboard.is_pressed('r'):  # Wait for 'r' to resume
#             time.sleep(0.1)
#         print("Resumed.")

#     if keyboard.is_pressed('q'):  # Quit the script
#         print("Exiting...")
#         break

#     # Simulate Ctrl+Tab to switch tabs
#     pyautogui.hotkey('ctrl', 'tab')  # For Mac, use 'command', 'option', 'right'
#     time.sleep(interval)  # Wait for the specified time



import pyautogui
import time
import keyboard

# Settings
idle_time = 5  # Time in seconds to wait for inactivity before switching tabs
typing_interval = 10  # Time interval to type in the file
text_to_type = "This is an automated entry.\n"  # Text to be written
file_path = "auto_typing.txt"  # File where text will be written

last_key_press = time.time()  # Track last key press time
last_typing_time = time.time()  # Track last auto-typing time

def key_pressed(event):
    """Reset the tab switch timer when any key is pressed."""
    global last_key_press
    last_key_press = time.time()

# Listen for any key press
keyboard.on_press(key_pressed)

print("Auto Tab Switcher and Auto Typing started.")
print("Switching tabs after 5 seconds of inactivity.")
print("Writing to file every 10 seconds.")

while True:
    time.sleep(1)  # Prevents CPU overuse

    # If no key is pressed for 'idle_time' seconds,  switch tab
    if time.time() - last_key_press >= idle_time:
        pyautogui.hotkey('ctrl', 'tab')  # For Mac, use ('command', 'option', 'right')
        last_key_press = time.time()  # Reset the timer

    # Automatically write text to file every 'typing_interval' seconds
    if time.time() - last_typing_time >= typing_interval:
        with open(file_path, "a") as f:
            f.write(text_to_type)
        print(f"Text added to {file_path}")
        last_typing_time = time.time()  # Reset typing timer


# import pyautogui
# import time

# # Settings
# tab_switch_interval = 5  # Switch tab every 5 seconds
# typing_interval = 10  # Type text every 10 seconds
# text_to_type = "This is an automated entry.\n"

# print("Auto Tab Switcher and Auto Typing started...")
# print("Press 'Ctrl + C' to stop.")

# while True:
#     # Switch tab
#     pyautogui.hotkey('ctrl', 'tab')  # For Mac, use ('command', 'option', 'right')
#     print("Switched tab.")
#     time.sleep(tab_switch_interval)

#     # Auto type in active window
#     pyautogui.typewrite(text_to_type)
#     print("Typed:", text_to_type.strip())
#     time.sleep(typing_interval)
    