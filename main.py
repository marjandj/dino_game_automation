import pyautogui
import pygetwindow as gw
import time

# === Settings ===
ground_y = 880        # Y-coordinate for cactus detection
air_y = 790           # Y-coordinate for bird detection
start_x = 385         # X-coordinate (in front of dino)
box_width = 110       # How far ahead to scan
dark_threshold = 100  # Brightness threshold

print("Starting in 3 seconds...")
time.sleep(3)

# Focus Chrome window
for window in gw.getWindowsWithTitle("Chrome"):
    if not window.isActive:
        window.activate()
        break
time.sleep(1)

# Start the game
pyautogui.press("space")

while True:
    # Check horizontal range in both zones
    for offset in range(0, box_width, 5):
        # Check ground zone
        r, g, b = pyautogui.pixel(start_x + offset, ground_y)
        brightness = (r + g + b) / 3
        if brightness < dark_threshold:
            pyautogui.press("space")  # Jump
            time.sleep(0.1)
            break

        # Check air zone
        r, g, b = pyautogui.pixel(start_x + offset, air_y)
        brightness = (r + g + b) / 3
        if brightness < dark_threshold:
            pyautogui.keyDown("down")  # Duck
            time.sleep(0.3)
            pyautogui.keyUp("down")
            break


   