#!.venv/bin/python
import cv2
import shutil
import numpy as np
from time import sleep

# terminal related stuff
terminal_size = shutil.get_terminal_size()
terminal_width = terminal_size.columns
ascii_art_width = terminal_width
# terminal chars are ~2:1 (height:width)
aspect_correction = 0.5 

# colors and ascii related stuff
green_color_code = "\033[1;32m"
default_color_code = "\033[0m"
ascii_ramp_1 = " .:-=+*#%@"
ascii_ramp_2 = " .'`^\",:;Il!i~+_-?][}{1)(|\\/*tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_ramp_3 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/()1{}[]?-_+~<>i!lI;:,\"^`'. "

# globals
ascii_ramp = ascii_ramp_1
ramp_len = len(ascii_ramp) - 1
ascii_lookup = np.full(256, '', dtype='U')


def redraw_screen():
    print("\x1b[H", end="")


def clear_screen():
    print("\x1b[2J\x1b[H", end="")


def create_lookup_table():
    for i in range(256):
        index = int((i / 255) * ramp_len)
        ascii_lookup[i] = ascii_ramp[index]


def frame_to_terminal_ascii(gray_image):
    all_rows = []
    ascii_frame = ascii_lookup[gray_image]
    row = ascii_frame.shape[0]
    for r in range(row):
        row_str = "".join(ascii_frame[r])
        all_rows.append(row_str)
    ascii_image_str = "\n".join(all_rows)
    ascii_image = green_color_code + ascii_image_str + default_color_code
    print(ascii_image)
    

def matrix():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("[Error] Cannot open camera")
        else:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("[Error] Cannot read frame from video capture")
                    break

                mirrored_frame = cv2.flip(frame, 1)

                gray_frame = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2GRAY)

                original_height, original_width = gray_frame.shape
                scale = ascii_art_width / original_width
                ascii_art_height = int(original_height * scale * aspect_correction)

                resized_frame = cv2.resize(gray_frame, (ascii_art_width, ascii_art_height))

                frame_to_terminal_ascii(resized_frame)

                redraw_screen()

                # for test
                #cv2.imshow('cam capture', gray_frame)
                #if cv2.waitKey(1) == ord('q'):
                    #break

    except KeyboardInterrupt:
        print("Exiting matrix..")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        clear_screen()
        

if __name__ == "__main__":
    create_lookup_table()
    sleep(0.5)
    matrix()
