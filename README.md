# linux-clock-hud
A tiny little clock hud that disapears 1.5 seconds after launch.

Meant to be launched using a keybind for tiling window managers. (requires python3, and the Pyqt6 python module, may require qt6-base/qt6-base-dev)

_________________________________________________________________
-__INSTALLATION__-
________________________________________________________________
_______________________________EITHER_______________________________

First click on the "<> code" button on this github page, then click on download zip.

Extract the .zip then change directory to the path with the time-overlay.py
file by running the follwing in your terminal:

$ cd <path/to/.py/file>

Then add execute permisions:

$ chmod +x time-overlay.py

___________________________________________________________________
___________________________________OR___________________________________
(REQUIRES git)

Open your terminal and run:

$ git clone https://github.com/racoonraduggy12/linux-clock-hud.git

Then:

$ cd ~/linux-clock-hud/

Then:

$ chmod +x time-overlay.py

______________________________________________________________________

Finally bind your prefered key to time-overlay.py (make sure to use the full path.)

tested on Arch and linux mint

__________________________________________
______FOR DEBIEN FORKS(linux mint, ubuntu, kubuntu, debien)______

follow normal installation then run:

$ sudo apt install python3 python3-pyqt6 qt6-base-dev libgl1
