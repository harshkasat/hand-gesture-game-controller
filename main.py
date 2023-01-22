import cv2
import mediapipe as mp
import time
from directkey import ReleaseKey, PressKey, W, A, S, D
move_forward=W
move_backwad=S
move_right=D
move_left=A
video = cv2.VideoCapture(0)
mp_create=mp.solutions.drawing_utils
mp_driving_hand=mp.solutions.hands
with mp_driving_hand.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
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
        lm_list=[]
        # marking hand_landmark using mediapipe
        if hand_result.multi_hand_landmarks:
            for hand_landmark in hand_result.multi_hand_landmarks:
                my_hand=hand_result.multi_hand_landmarks[0]
                # marking co-ordinate of points id-->points of hands & lm--> co-ordinate
                for id, lm in enumerate(my_hand.landmark):
                    # h,w,c height and width of image
                    hig, wid, c = image.shape
                    cord_x,cord_y=int(lm.x*wid),int(lm.y*hig)
                    # botton have more cord_y and right side more cord_x
                    lm_list.append([id,cord_x,cord_y])
                mp_create.draw_landmarks(image,hand_landmark,mp_driving_hand.HAND_CONNECTIONS)
        if len(lm_list)!=0:
            # RIGHT HAND
            if lm_list[5][1]<lm_list[17][1]:
                if lm_list[8][2] > lm_list[6][2] and lm_list[12][2] > lm_list[9][2] and lm_list[16][2] > lm_list[13][2] and lm_list[20][2] > lm_list[17][2]:
                    # To move backward by using pywin32
                    PressKey(S)
                    time.sleep((.08))
                    ReleaseKey(S)
                else:
                    # To move forward by using pywin32
                    PressKey(W)
                    time.sleep((.08))
                    ReleaseKey(W)
            # LEFT HAND
            else:
                if lm_list[2][1]>lm_list[4][1] :
                    # To move left by using pywin32
                    PressKey(D)
                    time.sleep((.08))
                    ReleaseKey(D)
                elif lm_list[2][1]<lm_list[4][1]:
                    # To move right by using pywin32
                    PressKey(A)
                    time.sleep((.08))
                    ReleaseKey(A)
        cv2.imshow("frame", image)
        # ending_game to kill the terminand
        ending_game = cv2.waitKey(1)
        if ending_game == ord('e'):
            break
    video.release()
    cv2.destroyAllWindows