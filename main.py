# Python PyQt5 Digital Clock

# Import Necessary Modules
import sys   # System
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout   # Layout
from PyQt5.QtCore import QTimer, QTime, Qt     # Time
from PyQt5.QtGui import QFont, QFontDatabase   # Fonts

# Class of main Digital Clock
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()   # Initializes the parent class (QWidget)
        self.time_label = QLabel(self)   # QLabel displays the time
        self.timer = QTimer(self)   # QTimer updates the time
        self.initUI()   # Initializes the Window (UI)

# Function that sets window title / window location / window size
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)   # (x, y, width, height)

        # Create A PyQt5 vertical layout for the time_label widget
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)   # Adds time_label to the layout
        self.setLayout(vbox)   # PyQt5 now handles the widget automatically

        # Centers time_label in the label
        self.time_label.setAlignment(Qt.AlignCenter)

        # Sets font size / color
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: #f27527;")

        # Sets window background color to black
        self.setStyleSheet("background-color: black;")

        # Applies an imported font
        font_id = QFontDatabase.addApplicationFont("resources/DS-DIGIT.TTF")
        # Selects the first font (0) in the imported font family
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150) # my_font = imported font, font size
        self.time_label.setFont(my_font)  # Applies font to time_label

        # Connects the timeout signail to update_time
        self.timer.timeout.connect(self.update_time)
        # Starts the timer with a 1 second interval (1000ms)
        self.timer.start(1000)

        self.update_time()  # Update the time

    # Sets current time to "hh:mm:ss AM"
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time) # Set time_label to current time

# Runs if name = main
if __name__ == "__main__":
    app = QApplication(sys.argv)   # Creates the application
    clock = DigitalClock()   # Defines clock as DigitalClock
    clock.show()            # Displays the clock
    sys.exit(app.exec_())   # Starts the execution loop