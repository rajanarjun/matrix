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

            mirrored_frame = cv2.flip(frame, 1)

            gray_frame = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2GRAY)

            # for test
            cv2.imshow('cam capture', gray_frame)



            if cv2.waitKey(1) == ord('q'):
                break
    else:
        print("[Error] Cannot open camera")

    cap.release()
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
    matrix()
