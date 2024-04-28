
# Hand Gesture Control for Media Player

This Python project enables you to control media playback (play/pause, skip forward, skip backward) using hand gestures detected by a webcam. It utilizes the MediaPipe library for hand detection and OpenCV for image processing.

## Prerequisites

- Python 3.x
- OpenCV (`pip install opencv-python`)
- MediaPipe (`pip install mediapipe`)
- pynput (`pip install pynput`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Shivastoic/Gesture_control_Media.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Gesture_control_Media
   ```

3. Run the script:

   ```bash
   python ezcontrol.py
   ```

4. Place your hand in front of the webcam and perform gestures to control media playback.

## Supported Gestures

- **Pause/Play**: Bring all fingers together and lower the hand.
- **Skip Forward**: Move the hand to the right side of the screen.
- **Skip Backward**: Move the hand to the left side of the screen.

## Configuration

- `cooldown_period`: Adjust the cooldown period (in seconds) between consecutive actions to prevent accidental inputs.
- `max_num_hands`: Maximum number of hands to detect.
- `min_detection_confidence` and `min_tracking_confidence`: Minimum confidence thresholds for hand detection and tracking, respectively.

## License

This project is licensed under the [MIT License](LICENSE).

