import cv2
import mediapipe as mp
import time


class handDetector():
    #Initlising the parameters used in the Hand module in mediapipe
    def __init__(self, mode = False, maxHands = 4, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    #Locate the hands on the capture and draw the connections.
    def findHands(self, img, draw = True):
            
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #Checking if there are multiple landmarks
        if self.results.multi_hand_landmarks:
            #selecting the different landmarks out of the landmarks found.
            for handLms in self.results.multi_hand_landmarks:
                #Draw the landmarks
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        #Return the img that is being drawn on
        return img
                
    #Find the exact position of each landmark
    def findPosition(self, img, handNum = 0, draw = True):
        lmList = []
        #Check if there are multiple points on the video capture
        if self.results.multi_hand_landmarks:
            #Select a single hand 
            myHand = self.results.multi_hand_landmarks[handNum]
            #Select the ID of the landmark of each point on the hand.
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                #Take the height, width of the image being rendered
                h, w, c = img.shape
                #Find the exact position reletive the pixels used in the video capture
                cx, cy = int(lm.x*w), int(lm.y*h)
                #Append the location(using the pixels) with the ID of the landmarks
                lmList.append([id, cx, cy])
                #Draw a circle on each landmark of the hands
                # if draw:
                #     cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
        #Return the landmark list.
        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()


    while True:
        success, img = cap.read()        
        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        #Print a specific point out of the landmark list.
        if len(lmList) != 0:
            print(lmList[4])

        #Calculate the frame rate that is being used.
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        #Place the framerate on the screen and the connectections.
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,255,255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)




if __name__ == "__main__":
    main()