import cv2
import mediapipe as mp
video = cv2.VideoCapture(0)
mp_create=mp.solutions.drawing_utils
mp_driving_hand=mp.solutions.hands
with mp_driving_hand.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7) as hands:
    while True:
        kloop, image = video.read()
        # Hands take rgb color only and cv make image bgr
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # flags.writeable=False -->> when arr is immutable
        image.flags.writeable=False
        hand_result=hands.process(image)
        image.flags.writeable = True
        # again convert rgb into brg for
        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        if hand_result.multi_hand_landmarks:
            for hand_landmark in hand_result.multi_hand_landmarks:
                mp_create.draw_landmarks(image,hand_landmark,mp_driving_hand.HAND_CONNECTIONS)
        cv2.imshow("frame", image)
        ending_game = cv2.waitKey(1)
        if ending_game == ord('e'):
            break
    video.release()
    cv2.destroyAllWindowse
