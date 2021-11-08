
import cv2
import numpy as np

i = 0
colors = [(255, 0, 0), (255, 0, 255), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color = colors[0]
min_area = 1000
cap = cv2.VideoCapture(0)

width = int(cap.get(3))
height = int(cap.get(4))
canvas = np.zeros((height, width, 3), np.uint8)
lower_bound = np.array([50,100,100])
upper_bound = np.array([90,255,255])
kernel = np.ones((10,10), np.uint8)

previous_center_point = 0


while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    mask = cv2.dilate(mask, kernel, iterations=1)
    contours, h    = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        
        # Get the biggest contour from all the detected contours
        cmax = max(contours, key = cv2.contourArea)

        # Find the area of the contour
        area = cv2.contourArea(cmax)
        # print(area)
        if area > min_area:

            # Find center point of the contour
            M = cv2.moments(cmax)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        
            cv2.circle(frame, (cX, cY), 10, (0, 0, 255), 2)
        
            if previous_center_point == 0:
                if cY < 65:
                    # Clear all
                    if cX > 20 and cX < 120:
                        canvas = np.zeros((height, width, 3), np.uint8)
                    
                    elif cX > 140 and cX < 220:
                        color = colors[0]

                    elif cX > 240 and cX < 320:
                        color = colors[1]
                    
                    elif cX > 340 and cX < 420:
                        color = colors[2]
                    
                    elif cX > 440 and cX < 520:
                        color = colors[3]
                    
                    elif cX > 540 and cX < 620:
                        color = colors[4]
                    elif cX > 640 and cX < 780:
                        return_val, image = cap.read()
                        cv2.imwrite('screenshot'+str(i+1)+'.png', canvas)
                        i+=1

            if previous_center_point != 0:
                cv2.line(canvas, previous_center_point, (cX, cY), color, 2)
            previous_center_point = (cX, cY)

        else:
            previous_center_point = 0
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

    _, canvas_binary = cv2.threshold(canvas_gray, 20, 255, cv2.THRESH_BINARY_INV)

    canvas_binary = cv2.cvtColor(canvas_binary, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, canvas_binary)
    frame = cv2.bitwise_or(frame, canvas)
    cv2.rectangle(frame, (20,1), (120,65), (122,122,122), -1)
    cv2.rectangle(frame, (140,1), (220,65), colors[0], -1)
    cv2.rectangle(frame, (240,1), (320,65), colors[1], -1)
    cv2.rectangle(frame, (340,1), (420,65), colors[2], -1)
    cv2.rectangle(frame, (440,1), (520,65), colors[3], -1)
    cv2.rectangle(frame, (540,1), (620,65), colors[4], -1)
    cv2.rectangle(frame, (640, 1), (780, 65), (122, 122, 122), -1)
    cv2.putText(frame, "CLEAR ALL", (30, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (155, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "VIOLET", (255, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (355, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (465, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (555, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA)
    cv2.putText(frame, "SCREENSHOT", (665, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Frame", frame)
    cv2.imshow('Canvas', canvas)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
