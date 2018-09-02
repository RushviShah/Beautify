import cv2
import numpy as np


def Invert(frame):
  return cv2.bitwise_not(frame)


def OverlayColor(frame, intensity=0.5, blue=0, green=0, red=0):
  #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)   #adding alpha channel
  #print(frame.shape)
  bgra = (blue, green, red)
  Overlay = np.full(frame.shape, bgra).astype(np.uint8)
  #print([Overlay.shape,frame.shape])
  cv2.addWeighted(Overlay, intensity, frame, 1.0, 0, frame)
  #frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  #removing alpha channel
  return frame


cap = cv2.VideoCapture(0)
while True:
  _, frame = cap.read()
  invert = Invert(frame)
  FuchsiaColorPic = OverlayColor(frame.copy(), blue=255, red=255)
  cv2.imshow('Original', frame)
  cv2.imshow('FirstFilter', invert)
  cv2.imshow('FuchsiaColorPic', FuchsiaColorPic)
  key = cv2.waitKey(1)
  if key == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
