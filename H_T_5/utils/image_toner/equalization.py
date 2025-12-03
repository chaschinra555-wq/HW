import cv2

def equalization(img):
    dst = cv2.equalizeHist(img)
    return dst