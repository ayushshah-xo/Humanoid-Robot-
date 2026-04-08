import serial
import time
from PySide6.QtWidgets import (
    QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel
)
from PySide6.QtGui import QPixmap

# Replace with your Pico's serial port
ser = serial.Serial('COM16', 115200, timeout=1)
time.sleep(2)  # Give time for the Pico to reset and connect

app = QApplication([])

# Create the main window and layout containers
window = QWidget()
main_layout = QHBoxLayout()  # Two columns side by side

# First column of buttons (LED + Eyes)____________________________________
column1 = QVBoxLayout()
btn_on = QPushButton("DEBUG LED On")
btn_off = QPushButton("DEBUG LED Off")
eyes_closed = QPushButton("Close Eyes")
eyes_open = QPushButton("Open Eyes")
move_eyes = QPushButton("Move Eyes")

# Add to first column
column1.addWidget(btn_on)
column1.addWidget(btn_off)
column1.addWidget(eyes_closed)
column1.addWidget(eyes_open)
column1.addWidget(move_eyes)

# Second column of buttons (Eyebrows)__________________________________
column2 = QVBoxLayout()
null_btn = QPushButton("DEBUG NULL")
brows_up = QPushButton("Raise Eyebrows")
brows_down = QPushButton("Lower Eyebrows")
brows_happy = QPushButton("Happy Eyebrows")
brows_angry = QPushButton("Angry Eyebrows")

# Add to second column
column2.addWidget(null_btn)
column2.addWidget(brows_up)
column2.addWidget(brows_down)
column2.addWidget(brows_happy)
column2.addWidget(brows_angry)

# Thhird column of buttons (Mouth)__________________________________
column3 = QVBoxLayout()
mouth_closed = QPushButton("Close Mouth")
mouth_open = QPushButton("Open Mouth")
lips_down = QPushButton("Lower Lips")
lips_up = QPushButton("Raise Lips")
tongue_down = QPushButton("Tongue Down")

# Add to third column
column3.addWidget(mouth_closed)
column3.addWidget(mouth_open)
column3.addWidget(lips_down)
column3.addWidget(lips_up)
column3.addWidget(tongue_down)

# 4th column of buttons (lips)__________________________________
column4 = QVBoxLayout()
tongue_up = QPushButton("Tongue Up") 
smile = QPushButton("Smile")
frown = QPushButton("Frown")
wide = QPushButton("Wide Lips")
narrow = QPushButton("Narrow Lips")
 

# Add to 4th column
column4.addWidget(tongue_up)
column4.addWidget(smile)
column4.addWidget(frown)
column4.addWidget(wide)
column4.addWidget(narrow)

# Add to 5th column
column5 = QVBoxLayout()
diagram = QLabel()
pixmap = QPixmap("image.png")  # Replace with your file path
diagram.setPixmap(pixmap)
column5.addWidget(diagram)

# Add both columns to the main horizontal layout
main_layout.addLayout(column1)
main_layout.addLayout(column2)
main_layout.addLayout(column3)
main_layout.addLayout(column4)
main_layout.addLayout(column5)


# Connect buttons to commands
def send_command(command):
    print(f"Sending: {command}")
    ser.write((command + '\n').encode('utf-8'))

btn_on.clicked.connect(lambda: send_command("on"))
btn_off.clicked.connect(lambda: send_command("off"))
eyes_closed.clicked.connect(lambda: send_command("eyes_close"))
eyes_open.clicked.connect(lambda: send_command("eyes_open"))
move_eyes.clicked.connect(lambda: send_command("eyes_move"))

brows_up.clicked.connect(lambda: send_command("brows_up"))
brows_down.clicked.connect(lambda: send_command("brows_down"))
brows_happy.clicked.connect(lambda: send_command("brows_happy"))
brows_angry.clicked.connect(lambda: send_command("brows_angry"))

mouth_closed.clicked.connect(lambda: send_command("mouth_closed"))
mouth_open.clicked.connect(lambda: send_command("mouth_open"))
lips_down.clicked.connect(lambda: send_command("lips_down"))
lips_up.clicked.connect(lambda: send_command("lips_up"))

tongue_up.clicked.connect(lambda: send_command("tongue_up"))
tongue_down.clicked.connect(lambda: send_command("tongue_down"))
smile.clicked.connect(lambda: send_command("smile"))
frown.clicked.connect(lambda: send_command("frown"))

wide.clicked.connect(lambda: send_command("wide"))
narrow.clicked.connect(lambda: send_command("narrow"))


# Final setup
window.setLayout(main_layout)
window.setWindowTitle("Will Cogley Robotic Head α2.0 Control Panel")
window.show()

app.exec()
