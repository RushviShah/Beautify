import cv2
cap=cv2.VideoCapture(0)
def Invert(frame):
  return cv2.bitwise_not(frame)
while True:
  _, frame=cap.read()
  invert=Invert(frame)
  cv2.imshow('Original', frame)
  cv2.imshow('FirstFilter',invert)
  key=cv2.waitKey(1)
  if key==ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
