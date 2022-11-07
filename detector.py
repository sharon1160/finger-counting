import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils



class Detector:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        #when the mediapipe is first started, it detects the hands. After that it tries to track the hands
        #as detecting is more time consuming than tracking. If the tracking confidence goes down than the
        #specified value then again it switches back to detection
        self.hands = mpHands.Hands(max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence,
                                   min_tracking_confidence=min_tracking_confidence)


    def findHandLandMarks(self, image, handNumber=0, draw=False):
        originalImage = image
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # mediapipe requiere RGB
        results = self.hands.process(image)
        hand_list=[]
        
        if results.multi_handedness:
            for i in range(len(results.multi_handedness)):
                landMarkList = []
                label = results.multi_handedness[i].classification[0].label  # se invierte las etiquetas por que la camara esta en modo reflejo
                if label == "Left":
                    label = "Right"
                elif label == "Right":
                    label = "Left"

                hand = results.multi_hand_landmarks[i] #results.multi_hand_landmarks retorna los landmarks 

                for id, landMark in enumerate(hand.landmark):
                    # landMark holds x,y,z ratios of single landmark
                    imgH, imgW, imgC = originalImage.shape  # height, width, channel for image
                    xPos, yPos = int(landMark.x * imgW), int(landMark.y * imgH)
                    landMarkList.append([id, xPos, yPos, label])

                if draw:
                    mpDraw.draw_landmarks(originalImage, hand, mpHands.HAND_CONNECTIONS)
                hand_list.append(landMarkList)
        return hand_list