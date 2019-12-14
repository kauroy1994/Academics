import cv2
import numpy as np
import os

def main():
   scale = 2
   canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
   cv2.line(canvas,(0,140*scale),(300*scale,140*scale),(255,255,255))
   cv2.line(canvas,(0,190*scale),(300*scale,190*scale),(255,255,255))
   cv2.line(canvas,(170*scale,0*scale),(170*scale,300*scale),(255,255,255))
   cv2.line(canvas,(120*scale,0*scale),(120*scale,300*scale),(255,255,255))
   canvas[0:140*scale,120*scale:170*scale] = [135,135,145]
   canvas[140*scale:190*scale,0:120*scale] = [135,135,145]
   canvas[190*scale:300*scale,120*scale:170*scale] = [135,135,145]
   canvas[140*scale:190*scale,170*scale:300*scale] = [135,135,145]
   y = 0
   while y<140:
     cv2.line(canvas, (145*scale, y*scale), (145*scale, (y+10)*scale), [255,255,255])
     y += 20
   x = 0
   while x<120:
      cv2.line(canvas, (x*scale, 165*scale), ((x+10)*scale, 165*scale), [255,255,255])
      x += 20
   y = 190
   while y<300:
     cv2.line(canvas, (145*scale, y*scale), (145*scale, (y+10)*scale), [255,255,255])
     y += 20
   x = 170
   while x<300:
      cv2.line(canvas, (x*scale, 165*scale), ((x+10)*scale, 165*scale), [255,255,255])
      x += 20
   while 1:
      cv2.putText(canvas,'a. Obtaining foreground objects', (canvas.shape[1] - 600, canvas.shape[0] - 580), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'b. Extract full-colored keyframes', (canvas.shape[1] - 600, canvas.shape[0] - 510), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'c. Extract foreground keyframes', (canvas.shape[1] - 600, canvas.shape[0] - 440), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'d. Find traffic violation', (canvas.shape[1] - 600, canvas.shape[0] - 370), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'e. Calculate sample red signal time', (canvas.shape[1] - 600, canvas.shape[0] - 300), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'f. Extract and recognize license plate number', (canvas.shape[1] - 600, canvas.shape[0] - 230), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'g. Get License plate information', (canvas.shape[1] - 600, canvas.shape[0] - 160), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.putText(canvas,'h. Gaussian Mixture model demo', (canvas.shape[1] - 600, canvas.shape[0] - 90), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 255, 0), 2)
      cv2.imshow('WELCOME! press Q to quit',canvas)
      k = cv2.waitKey(0)
      if k == ord('a'):
         os.system("/anaconda/bin/python tryproj.py 1")
      elif k == ord('b'):
         os.system("/anaconda/bin/python tryproj.py 2")
      elif k == ord('c'):
         os.system("/anaconda/bin/python tryproj.py 3")
      elif k == ord('d'):
         os.system("/anaconda/bin/python tryproj.py 4")
      elif k == ord('e'):
         os.system("/anaconda/bin/python tryproj.py 5")
      elif k == ord('f'):
         os.system("/anaconda/bin/python tryproj.py 6")
      elif k == ord('g'):
         os.system("/anaconda/bin/python tryproj.py 7")
      elif k == ord('h'):
         os.system("/anaconda/bin/python tryproj.py 8")
      elif k == ord('q'):
         break
   exit()

if __name__ == "__main__":
   main()
