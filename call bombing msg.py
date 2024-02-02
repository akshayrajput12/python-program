import pyautogui
import time

# Specify the phone number
phone_number = '919116350746'

# Specify the number of calls
number_of_calls = 10

# Specify the number of messages
number_of_messages = 10

# Specify the message content
message_content = 'This is a test message.'

# Make calls
for i in range(number_of_calls):

    pyautogui.hotkey('win', 'r') # Open the run dialog box
    time.sleep(1)
    pyautogui.typewrite('cmd') # Type cmd
    pyautogui.press('enter') # Press enter
    time.sleep(1)
    pyautogui.typewrite(f'tel:{phone_number}') # Type the phone number command
    pyautogui.press('enter') # Press enter
    time.sleep(1)
    pyautogui.hotkey('win', 'r') # Close the command prompt
    time.sleep(1)

# Send messages
for i in range(number_of_messages):
    pyautogui.hotkey('win', 'r') # Open the run dialog box
    time.sleep(1)
    pyautogui.typewrite('cmd') # Type cmd
    pyautogui.press('enter') # Press enter
    time.sleep(1)
    pyautogui.typewrite(f'msg {phone_number} {message_content}') # Type the send message command
    pyautogui.press('enter') # Press enter
    time.sleep(1)
    pyautogui.hotkey('win', 'r') # Close the command prompt
    time.sleep(1)