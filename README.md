# four-map-solver
![GitHub](https://img.shields.io/github/license/LK00100100/four-map-solver)
![RepoSize](https://img.shields.io/github/repo-size/LK00100100/four-map-solver.svg)
![GitHub stars](https://img.shields.io/github/stars/LK00100100/four-map-solver.svg?style=social)

![alt text](https://raw.githubusercontent.com/LK00100100/four-map-solver/master/map-solver-demo.gif "Demo")

Solves the 4-color-map on MobaXterm.
https://en.wikipedia.org/wiki/Four_color_theorem

If the game is running on the screen, this script will click in a solution.

Also, reads an image of the game and outputs the solution image of the game.

Also, reads a text file of a certain format) and outputs the solution

# Build and running

Uses python 3.7, virtualenv

I use the Pycharm IDE to set all of the dependencies.
File -> Settings -> Project -> Project Interpreter

To install packages:
your_env/pip install -r requirements.txt

OR if you are in pycharm, just open up the pycharm and they will prompt you if you want to download the stuff in the requirements.txt 

Run main-read-screen-clicker.py and the script will read the game screen and click in a solution.

main-read-image.py is used to read a specific image (hard-coded) and output an image (hard-coded)

# TODO

- Needs unit tests?

# Side notes

To get installed packages:
your_env/pip freeze > requirements.txt

As a safety feature, a fail-safe feature is enabled by default.
When pyautogui.FAILSAFE = True
PyAutoGUI functions will raise a pyautogui.FailSafeException if the mouse cursor is in the upper left corner of the screen.
If you lose control and need to stop the current PyAutoGUI function, keep moving the mouse cursor up and to the left. 
