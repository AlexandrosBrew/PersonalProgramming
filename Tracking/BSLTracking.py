import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon = 0.8, maxHands=2)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    #hands, img = detector.findHands(img, draw=False) Without drawing
cap.release()
cv2.destroyAllWindows()