import cv2
import numpy as np


def Invert(frame):
  return cv2.bitwise_not(frame)


def OverlayColor(frame, intensity=0.5, blue=0, green=0, red=0):
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # adding alpha channel
  #print(frame.shape)
  bgra = (blue, green, red, 4)
  Overlay = np.full(frame.shape, bgra).astype(np.uint8)
  #print([Overlay.shape,frame.shape])
  cv2.addWeighted(Overlay, intensity, frame, 1.0, 3, frame)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # removing alpha channel
  return frame


def Blur(frame, ind):
  BlurSize = 3 + 2 * (ind % 5)
  Blur = np.ones((BlurSize, BlurSize), dtype=np.float32)
  Blur /= (BlurSize * BlurSize)
  return cv2.filter2D(frame, -1, Blur)


cap = cv2.VideoCapture(0)
while True:
  _, frame = cap.read()
  invert = Invert(frame.copy())
  FuchsiaColorPic = OverlayColor(
      frame.copy(), blue=255, red=255, intensity=0.2)
  GoldColorPic = OverlayColor(frame.copy(), blue=8, red=44, green=26)
  BlueColorPic = OverlayColor(
      frame.copy(), blue=238, red=175, green=238, intensity=0.2)
  BlurImage = Blur(frame.copy(), 1)

  cv2.imshow('Original', frame)
  cv2.imshow('Invert', invert)
  cv2.imshow('FuchsiaColorPic', FuchsiaColorPic)

  cv2.imshow('GoldColorPic', GoldColorPic)
  cv2.imshow('BlueColorPic', BlueColorPic)
  cv2.imshow('BlurImage', BlurImage)

  key = cv2.waitKey(1)
  if key == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()

