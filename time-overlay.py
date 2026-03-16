#!/usr/bin/env python3

#    Linux Clock Hud
#    Copyright (C) 2025  racoonraduggy12

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
from pathlib import Path
import configparser
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor
from datetime import datetime
import argparse
from PyQt6.QtGui import QFontMetrics

# Config constants
CONFIG_DIR = Path.home() / ".config" / "linux_clock_hud"
CONFIG_FILE = CONFIG_DIR / "settings.conf"
DEFAULT_FORMAT = "%H:%M:%S"
DEFAULT_STYLE = "color: rgb(0, 255, 186); background: none;"

def load_or_create_config():
    """Load time format from config, or create config with default if missing."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    config = configparser.ConfigParser(interpolation=None)
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)
        time_format = config.get("Clock", "time_format", fallback=DEFAULT_FORMAT)
        style_sheet = config.get("Clock", "style", fallback=DEFAULT_STYLE)
    else:
        config["Clock"] = {"time_format": DEFAULT_FORMAT, "style": DEFAULT_STYLE}
        with open(CONFIG_FILE, "w") as f:
            config.write(f)
        time_format = DEFAULT_FORMAT
        style_sheet = DEFAULT_STYLE
    return time_format, style_sheet

def save_config(time_format=DEFAULT_FORMAT, style_sheet=DEFAULT_STYLE):
    """Save time format and style sheet to .conf file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    config = configparser.ConfigParser(interpolation=None)
    config["Clock"] = {"time_format": time_format, "style": style_sheet}
    with open(CONFIG_FILE, "w") as f:
        config.write(f)
    print(f"Saved time format '{time_format}' and style sheet '{style_sheet}' to {CONFIG_FILE}")

class ClockOverlay(QWidget):
    def __init__(self, time_format=DEFAULT_FORMAT, style_sheet=DEFAULT_STYLE):
        super().__init__()
        self.time_format = time_format

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(250, 100)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.base_font_size = 30
        self.font = QFont("Monospace", self.base_font_size, QFont.Weight.Bold)
        self.label.setFont(self.font)
        self.label.setStyleSheet(style_sheet)
        layout.addWidget(self.label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(200)

        self.opacity = 0.85
        QTimer.singleShot(1500, lambda: sys.exit(0))
    def paintEvent(self, event):
        from PyQt6.QtGui import QPainter, QColor
        painter = QPainter(self)
        color = QColor(0, 0, 0)
        color.setAlphaF(self.opacity)
        painter.fillRect(self.rect(), color)

    def update_time(self):
        now = datetime.now().strftime(self.time_format)
        self.label.setText(now)
        self.adjust_font_to_fit(now)

    def adjust_font_to_fit(self, text):
        """Reduce font size if text is too wide for the window."""
        max_width = self.width() - 10  # small margin
        font_size = self.base_font_size
        font = QFont(self.font)
        font.setPointSize(font_size)
        metrics = QFontMetrics(font)

        while metrics.horizontalAdvance(text) > max_width and font_size > 5:
            font_size -= 1
            font.setPointSize(font_size)
            metrics = QFontMetrics(font)

        self.label.setFont(font)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tiny Linux Clock HUD")
    parser.add_argument(
        "-f", "--format",
        help="Time format string (Python strftime style). Overrides config file."
    )
    parser.add_argument(
        "--save", action="store_true",
        help="Save the given format to the config file for future runs."
    )
    parser.add_argument(
        "-s", "--style",
        help="Qt style sheet string. Overrides config file."
    )
    args = parser.parse_args()
    conf = load_or_create_config()
    # Load existing config or create default if missing
    time_format = conf[0]
    style_sheet = conf[1]

    # Override if --format is given
    if args.format:
        time_format = args.format

    # Override if --style is given
    if args.style:
        style_sheet = args.style

    # Save if requested
    if args.save:
        if args.format:
            save_config(time_format=args.format, style_sheet=style_sheet)
        if args.style:
            save_config(time_format=time_format, style_sheet=args.style)

    app = QApplication(sys.argv)
    overlay = ClockOverlay(time_format=time_format, style_sheet=style_sheet)
    overlay.show()
    sys.exit(app.exec())
