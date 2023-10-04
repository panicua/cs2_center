import keyboard
import mouse
import time
import cv2
import numpy as np
import mss

screen = {
    'left': 958,
    'top': 538,
    'width': 4,
    'height': 4
}


def trigger_click():
    while True:
        time.sleep(0.01)
        if keyboard.is_pressed('f'):
            sct = mss.mss()
            scr = np.array(sct.grab(screen))
            time.sleep(0.01)
            scr_2 = np.array(sct.grab(screen))
            scr_remove = scr[:, :, :3]
            scr_2_remove = scr_2[:, :, :3]
            gray_frame = cv2.cvtColor(scr_remove, cv2.COLOR_BGR2GRAY)
            gray_frame_2 = cv2.cvtColor(scr_2_remove, cv2.COLOR_BGR2GRAY)
            result = cv2.matchTemplate(gray_frame, gray_frame_2, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            print(max_val)
            if max_val != 1:
                time.sleep(0.025)
                mouse.click()
                time.sleep(0.1)


trigger_click()
