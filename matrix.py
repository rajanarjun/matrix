#!.venv/bin/python
import cv2

def matrix():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[Error] Cannot read frame from video capture")
                break

            cv2.imshow('cam capture', frame)
            if cv2.waitKey(1) == ord('q'):
                break
    else:
        print("[Error] Cannot open camera")

    cap.release()
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
    matrix()
