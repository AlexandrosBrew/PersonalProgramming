import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from HandTrackingModule import handDetector

class GestureTracking():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils

    def getModel(self):
        self.model = load_model('/Users/alexandrosbrew/Documents/PersonalProgramming/Tracking/HandGesture/mp_hand_gesture')
        self.f = open('/Users/alexandrosbrew/Documents/PersonalProgramming/Tracking/HandGesture/gesture.names', 'r')
        self.classNames = self.f.read().split('\n')
        return self.model, self.f, self.classNames
    
    def getClassName(self, frame, model):
        x, y, c = frame.shape
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(framergb)
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    lmx, lmy = int(lm.x * x), int(lm.y*y)
                    landmarks.append([lmx, lmy])

                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = self.classNames[classID]
            return className

def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
    mpDraw = mp.solutions.drawing_utils

    while True:
        _, frame = cap.read()
        x, y, c = frame.shape

        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)
        model = load_model('/Users/alexandrosbrew/Documents/PersonalProgramming/Tracking/HandTracking/HandGesture/mp_hand_gesture')

        f = open('/Users/alexandrosbrew/Documents/PersonalProgramming/Tracking/HandTracking/HandGesture/gesture.names', 'r')
        classNames = f.read().split('\n')
        f.close

        className = ''

        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    #print(id, lm)
                    lmx, lmy = int(lm.x * x), int(lm.y*y)

                    landmarks.append([lmx, lmy])
                
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = classNames[classID]
                
            
        cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
        
        cv2.imshow("Output", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()