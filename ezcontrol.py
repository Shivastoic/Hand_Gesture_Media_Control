import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
import time


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)


keyboard = Controller()


cooldown_period = 2  


last_action_time = 0


def perform_action(gesture):
    global last_action_time
    current_time = time.time()
    
    if current_time - last_action_time < cooldown_period:
        return
    
    if gesture == "pause_play":
        print("Pause/Play")
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif gesture == "left_skip":
        print("Left skip")
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif gesture == "right_skip":
        print("Right skip")
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    
    last_action_time = current_time


def detect_gestures():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                draw_landmarks(frame, hand_landmarks)
                
                
                gesture = classify_gesture(hand_landmarks)
                if gesture:
                    perform_action(gesture)

        cv2.imshow('Hand Gestures', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def classify_gesture(hand_landmarks):
    
    if (hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y <
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y):
        return "pause_play"
    
    
    if (hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x <
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x <
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x <
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x <
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x <
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x):
        return "left_skip"
    
    
    if (hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x >
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x >
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x >
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x >
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x >
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x):
        return "right_skip"
    
   
    if (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y >
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y >
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y >
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y >
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y and
        hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y >
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y):
        return "pause_play"

    return None



def draw_landmarks(frame, landmarks):
    for landmark in landmarks.landmark:
        x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

if __name__ == "__main__":
    detect_gestures()
