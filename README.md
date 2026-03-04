# linux-clock-hud
A tiny little clock hud that disapears 1.5 seconds after launch.

Meant to be launched using a keybind for tiling window managers. Installing from source makes it launch much faster, but is slightly more work<br><br><br><br><br><br>

_________________________________________________________________
## -____INSTALLATION____-
________________________________________________________________
Click on "Releases"  on the right of this GitHub page, click on the one of the newest releases either configurable if you want to configure the time/date format (eg v1.0.1-configurable) or without configurable (eg v1.0.1) if your fine with the default format. now click time-overlay to download it.
Open a terminal and run the following command replacing /path with the full path to the executable (eg ~/Downloads/time-overlay)

```
chmod +x /path
```

Finally map a keybind to the full path to this executable 

#### If you got a configurable release
Look for the CONFIGURATION section at the bottem of this README<br><br><br><br><br><br>
_________________________________________________________________
## -____INSTALLATION FROM SOURCE____-
________________________________________________________________
(Requires python3 and the Pyqt6 python module, may require qt6-base/qt6-base-dev)
### FIRST
Choose either the main or configurable-time-format branches depending on whether you want to configure your time format. You can switch branches by clicking the dropdown menu right above the source code on this page and selecting a branch.
___________________________________________________________________
### EITHER

Click on the green "<> code" button on the right of this github page, then click on download zip.

Extract the .zip then change directory to the path with the time-overlay.py
file by running the follwing in your terminal replacing <path/to/.py/file> with the actual path to the directory containing time-overlay.py that you downloaded (eg ~/Downloads/):
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

follow normal installation form source then run:

```
sudo apt install python3 python3-pyqt6 qt6-base-dev
```

______________________________________________________________________

Finally bind your prefered key to time-overlay.py (make sure to use the full path.)
Tested on Arch and linux mint if its not working for you install python3 python3-pyqt6 and qt6-base-dev from your package manager<br><br><br><br><br><br>

_________________________________________________________________
## -____CONFIGURATION____-
________________________________________________________________
When you run the application the first time settings.conf will be created in ~/.config/linux_clock_hud/
your time format can be made of most combinations of format codes, which are listed [here](https://strftime.org/), and normal characters.  
  
For example:

```
time_format = %I:%M %p - %B %-d
```

Might output:

#### 07:00 PM - September 12
