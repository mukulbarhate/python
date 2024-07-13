# import pywhatkit as kit
# import pyautogui

# # here 7,52 is time on which you want whatsapp message to go to the receiver

# kit.sendwhatmsg('+919096548909','Jevan Zala ka 😊',10,34)

# pyautogui.press('enter')
# # kit.search("Python programming")
# # kit.playonyt("End of Begining")

import pywhatkit as kit
import pyautogui
import time

# Define the message and contact details
message = 'Jevan Zala ka 😊'
contact = '+919096548909'

# Set the delay in seconds before sending the message
delay_seconds = 10

# Schedule the message to be sent after the specified delay
kit.sendwhatmsg_in(contact, message, delay_seconds)

# Wait for the message to be sent
time.sleep(delay_seconds)

# Automatically hit the Enter key to send the message
pyautogui.press('enter')
