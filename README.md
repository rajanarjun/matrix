# Matrix
A fun Python script that captures live video using OpenCV and converts each frame into green ASCII characters, recreating the classic **Matrix** terminal effect.

## Features
- Live video feed processed via **OpenCV**
- Converts pixel intensity to ASCII characters
- Displays output in green text live in the terminal

## Dependencies
- Check requirements.txt
- Tested on Linux only

### Installing dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run matrix:
```python
python3 matrix.py
```

The program will start capturing live video from your webcam and render it as ASCII characters directly in your terminal.

Press Ctrl + C at any time to safely quit the program, this will stop the video feed, release the camera, and clear the terminal screen.
