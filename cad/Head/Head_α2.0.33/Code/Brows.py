from machine import Pin
from time import sleep
from servo import Servo

led = Pin(25, Pin.OUT)
mode = Pin(1, Pin.IN, Pin.PULL_UP)
SDA = Pin(16, Pin.IN)
SCL = Pin(17, Pin.IN)


# --- ServoConfig Class ---
class SCFG:
    def __init__(self, pin_id, limits):
        self.servo = Servo(pin_id=pin_id)
        self.start, self.end = limits
        self.angle = self.start
        self.direction = 1  # Forward initially

    def move(self, angle):
        self.servo.write(angle)

    def step(self, step_size=1):
        # Calculate current step direction based on start vs end
        step = step_size if self.start < self.end else -step_size
        self.angle += self.direction * step

        # Reverse direction if past bounds
        if (self.direction == 1 and (
                (step > 0 and self.angle >= self.end) or (step < 0 and self.angle <= self.end))):
            self.angle = self.end
            self.direction = -1
        elif (self.direction == -1 and (
                (step > 0 and self.angle <= self.start) or (step < 0 and self.angle >= self.start))):
            self.angle = self.start
            self.direction = 1

        self.move(self.angle)

# --- Servo Setup ---
servos = {
    "LO": SCFG(8, (80,100)),
    "LI": SCFG(9, (100,80)),
    "RI": SCFG(13, (80,100)),
    "RO": SCFG(12, (100,80)),
}

# --- Main Loop ---
while True:
    led.value(not led.value())  # blink onboard LED
#     print(mode.value())
    if (mode.value() == 1):
        if SDA.value() == 0 and SCL.value() == 0: #Down
            servos["LO"].move(80)
            servos["LI"].move(100)
            servos["RI"].move(80)
            servos["RO"].move(100)
        if SDA.value() == 1 and SCL.value() == 1: #Up
            servos["LO"].move(120)
            servos["LI"].move(60)
            servos["RI"].move(120)
            servos["RO"].move(60)
        if SDA.value() == 1 and SCL.value() == 0: #Angry
            servos["LO"].move(120)
            servos["LI"].move(100)
            servos["RI"].move(80)
            servos["RO"].move(60)
        if SDA.value() == 0 and SCL.value() == 1: #Happy
            servos["LO"].move(80)
            servos["LI"].move(60)
            servos["RI"].move(120)
            servos["RO"].move(100)           
    if (mode.value() == 0):
        for s in servos.values():
            s.step(90)
    sleep(0.01)
 
