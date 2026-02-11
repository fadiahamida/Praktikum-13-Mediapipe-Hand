import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

while True:
    succes, img = cap.read()
    if not succes:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks and results.multi_handedness:

        for hand_landmarks, hand_label in zip(results.multi_hand_landmarks,
                                               results.multi_handedness):

            # Gambar landmark tangan
            mp_drawing.draw_landmarks(img, hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS)

            label = hand_label.classification[0].label  # Left / Right

            # Ambil koordinat landmark
            thumb_tip = hand_landmarks.landmark[4]
            pinky_tip = hand_landmarks.landmark[20]

            # Deteksi depan/belakang (sederhana berdasarkan sumbu X)
            if label == "Right":
                if thumb_tip.x < pinky_tip.x:
                    posisi = "Depan"
                else:
                    posisi = "Belakang"
            else:  # Left
                if thumb_tip.x > pinky_tip.x:
                    posisi = "Depan"
                else:
                    posisi = "Belakang"

            teks = f"{label} - {posisi}"

            cv2.putText(img, teks, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    cv2.imshow("Hand Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
