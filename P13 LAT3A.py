import cv2
import mediapipe
cap = cv2.VideoCapture(0)
mediapipehand = mediapipe.solutions.hands
hands = mediapipehand.Hands()

while True:
    succes, img = cap.read()
    if not succes:
        break

    imgRGB =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_handedness:
        for idx, hand in enumerate(results.multi_handedness):
            if hand.classification[0].index == 1:  # klasifikasi tangan kanan
                cv2.putText(img, "kanan", (200, 50),
                            cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0),3)  # memberikan teks pada tampilan jendela dengan font hershey plain dengan font size 5 dan ketebalan 3
            elif hand.classification[0].index == 0:  # klasifikasi tangan kiri
             cv2.putText(img, "kiri", (200, 50),
                     cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 3)

        cv2.imshow("Hand Detection", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
           break

cap.release()
cv2.destroyAllWindows()
