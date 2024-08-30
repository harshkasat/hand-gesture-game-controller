# Hand Gesture Game Controller

This project uses computer vision and hand tracking to control a game using hand gestures. It captures video from a webcam, detects hand movements, and translates them into keyboard inputs for game control.

## Features

- Real-time hand tracking using MediaPipe
- Gesture recognition for game control
- Keyboard input simulation for game interaction
- Support for forward, backward, left, and right movements

## Prerequisites

- Python 3.9
- OpenCV
- MediaPipe
- PyWin32 (for Windows key simulation)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/harshkasat/hand-gesture-game-controller.git
   cd hand-gesture-game-controller
   ```

2. Install the required packages:
   ```
   pip install opencv-python mediapipe pywin32
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. Position your hand in front of the webcam:
   - Right hand controls forward/backward movement
   - Left hand controls left/right movement

3. Use the following gestures:
   - Right hand: 
     - Fingers up: Move forward
     - Fingers down: Move backward
   - Left hand:
     - Thumb left of fingers: Move left
     - Thumb right of fingers: Move right

4. Press 'e' to exit the program

## How it works

1. The script captures video from the default webcam
2. MediaPipe is used to detect and track hand landmarks
3. Based on the position of specific landmarks, gestures are recognized
4. Recognized gestures are translated into keyboard inputs (W, A, S, D)
5. These inputs can be used to control games that use standard WASD controls

## Customization

You can modify the `directkey.py` file to change the key mappings or add new gestures and corresponding actions in the main script.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
