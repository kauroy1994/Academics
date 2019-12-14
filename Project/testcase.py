import cv2
import numpy as np

def cnts(image):
   im = image.copy()
   blur = cv2.bilateralFilter(im,11,17,17)
   thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
   can = cv2.Canny(thresh,100,200)
   can2=can.copy()
   contours,hierarchy = cv2.findContours(can,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
   for cnt in contours:
      cv2.drawContours(im,[cnt],-1,(255,255,255),3)
   return im

def diffImg(t1,t2):
   d1=cv2.absdiff(t2,t1)
   gray = cv2.cvtColor(d1, cv2.COLOR_BGR2GRAY)
   #return cnts(gray)
   return gray
   

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err
    
def main():
   cam = cv2.VideoCapture('simple3.mp4')
   f0 = cam.read()[1]
   i = 0
   while(cam.isOpened()):
      string = ""
      t,f = cam.read()
      if mse(f0,f) > 15.0:
         i += 1
         string += "Desktop/testcases/Ccase3/frame"+str(i)+".jpg"
         cv2.imwrite(string,diffImg(f0,f))
         #cv2.imshow('newwindow',diffImg(f0,f))
      f0=f
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break         
   cam.release()
   cv2.destroyAllWindows()
   
if __name__ == "__main__":
   main()