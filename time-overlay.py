#!/usr/bin/env python3
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPalette, QColor
from datetime import datetime
from PyQt6.QtCore import QTimer

class ClockOverlay(QWidget):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        # Make the window itself translucent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(250, 100)  # small window

        # Center window on screen
        screen = QApplication.primaryScreen().availableGeometry()

        # White text in center
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Monospace", 30, QFont.Weight.Bold)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 255, 186); background: none;")
        layout.addWidget(self.label)

        # Timer to update time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(200)

        # Paint event to fill the entire window with semi-transparent black
        self.opacity = 0.85  # 85%
        QTimer.singleShot(1500, lambda: sys.exit(0))

    def paintEvent(self, event):
        from PyQt6.QtGui import QPainter
        painter = QPainter(self)
        color = QColor(0, 0, 0)
        color.setAlphaF(self.opacity)  # 0.85 alpha
        painter.fillRect(self.rect(), color)

    def update_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.label.setText(now)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = ClockOverlay()
    overlay.show()
    sys.exit(app.exec())
