# linux-clock-hud
A tiny little clock hud that disapears 1.5 seconds after launch.

Meant to be launched using a keybind for tiling window managers. (requires python3, and the Pyqt6 python module, may require qt6-base/qt6-base-dev)

_________________________________________________________________
## -____INSTALLATION____-
________________________________________________________________
### EITHER

First click on the green "<> code" button on the right of this github page, then click on download zip.

Extract the .zip then change directory to the path with the time-overlay.py
file by running the follwing in your terminal replacing <path/to/.py/file> with the actual path to time-overlay.py that you downloaded:
```
cd <path/to/.py/file>
```

Then add execute permisions:

```
chmod +x time-overlay.py
```
___________________________________________________________________
### OR
(REQUIRES git)

Open your terminal and run:

```
git clone https://github.com/racoonraduggy12/linux-clock-hud.git
```

Then:

```
cd ~/linux-clock-hud/
```

Then:

```
chmod +x time-overlay.py
```

__________________________________________

### FOR DEBIEN FORKS(linux mint, ubuntu, kubuntu, debien)______

follow normal installation then run:

```
sudo apt install python3 python3-pyqt6 qt6-base-dev libgl1
```

______________________________________________________________________

Finally bind your prefered key to time-overlay.py (make sure to use the full path.)

tested on Arch and linux mint


