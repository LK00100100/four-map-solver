# four-map-solver

**work in progress**

Solves the 4-color-map on MobaXterm.
https://en.wikipedia.org/wiki/Four_color_theorem

Reads an image of the game and outputs the solution image of the game.

Also, reads a text file of a certain format) and outputs the solution

# Running

Uses python 3.7, virtualenv

I use the Pycharm IDE to set all of the dependencies.
File -> Settings -> Project -> Project Interpreter

To install packages:
your_env/pip install -r requirements.txt

OR if you are in pycharm, just open up the pycharm and they will
prompt you if you want to download the still in the requirements.txt 

Run mainReadImage.py

# TODO

- Needs unit tests?
- Screen Reader
- Auto Clicker

# Side notes

To get installed packages:
your_env/pip freeze > requirements.txt

As a safety feature, a fail-safe feature is enabled by default.
When pyautogui.FAILSAFE = True
PyAutoGUI functions will raise a pyautogui.FailSafeException if the mouse cursor is in the upper left corner of the screen.
If you lose control and need to stop the current PyAutoGUI function, keep moving the mouse cursor up and to the left. 