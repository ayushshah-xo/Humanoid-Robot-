# Quickstart Guide

## Hardware Required
- Raspberry Pi 4 (64-bit OS recommended)
- Adafruit PCA9685 16-channel servo board
- 3 servo motors (jaw, left brow, right brow)
- USB microphone
- 3.5mm speaker connected to audio jack

## Hardware Connections
| Servo | PCA9685 Channel |
|-------|----------------|
| Jaw   | Channel 0      |
| Left Brow | Channel 4  |
| Right Brow | Channel 5 |

## Step 1 — System dependencies
```bash
sudo apt update
sudo apt install espeak python3-pyaudio portaudio19-dev alsa-utils
```

## Step 2 — Install Ollama (offline AI)
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull tinyllama
```

## Step 3 — Clone and install
```bash
git clone https://github.com/ayushshah-xo/Humanoid-Robot-.git
cd Humanoid-Robot-
pip install -r requirements.txt
```

## Step 4 — Configure
```bash
cp config.example.yaml config.yaml
nano config.yaml
```
- Add your Groq API key (get free key at console.groq.com)
- Set your audio output card number (run `aplay -l` to check)
- Set your mic device index (run `python3 -m speech_recognition` to check)

## Step 5 — Run
```bash
python3 main.py
```

## Finding your audio card number
```bash
aplay -l
```
Look for `bcm2835 Headphones` — the card number before it is your `output_card` value.

## Finding your mic device index
```bash
python3 -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```
Count from 0 to find your USB mic index and set it as `input_device` in config.yaml.
