#import necessary modules
from sklearn.cluster import MiniBatchKMeans
import cv2
import numpy as np
import time
import argparse
import os
import imutils

#create vehicle Class
class Vehicle(object):
   
   vehicleList = {}
   
   Name_of_Vehicle = None
   Date_of_Registration = None
   Owner_Name = None
   RTO_Number = None
   State_Number = None
   Number_Plate = None
   Owner_Residence = None
   features = None
   number = None
   
   def __init__(self,vname,date,oname,rnumber,snumber,plate,residence):
      self.Name_of_Vehicle = vname
      self.Date_of_Registration = date
      self.Owner_Name = oname
      self.RTO_Number = rnumber
      self.State_Number = snumber
      self.Number_Plate = plate
      self.Owner_Residence = residence
      self.features = list
      self.number = plate[4:len(plate)]
      Vehicle.vehicleList[self.number] = self
      
      lastDigit = vname[len(vname)-1]
      
      if int(lastDigit) == 1:
         self.features = [2.5,2.4,51,501,145,495]
         carName = "Desktop/cars/Car"+lastDigit+".jpg"
         carImage = cv2.imread(carName)
         newCarName = "project/cars/Car"+lastDigit+".jpg"
         cv2.imwrite(newCarName,carImage)
      elif int(lastDigit) == 2:
         self.features = [2.5,2.4,40,470,125,490]
         carName = "Desktop/cars/Car"+lastDigit+".jpg"
         carImage = cv2.imread(carName)
         newCarName = "project/cars/Car"+lastDigit+".jpg"
         cv2.imwrite(newCarName,carImage)
      elif int(lastDigit) == 3:
         self.features = [2.5,2.4,15,430,130,498]
         carName = "Desktop/cars/Car"+lastDigit+".jpg"
         carImage = cv2.imread(carName)
         newCarName = "project/cars/Car"+lastDigit+".jpg"
         cv2.imwrite(newCarName,carImage)
      elif int(lastDigit) == 4:
         self.features = [2.5,2.4,60,550,150,585]
         carName = "Desktop/cars/Car"+lastDigit+".jpg"
         carImage = cv2.imread(carName)
         newCarName = "project/cars/Car"+lastDigit+".jpg"
         cv2.imwrite(newCarName,carImage)
      elif int(lastDigit) == 5:
         self.features = [2.5,2.4,0,628,143,637]
         carName = "Desktop/cars/Car"+lastDigit+".jpg"
         carImage = cv2.imread(carName)
         newCarName = "project/cars/Car"+lastDigit+".jpg"
         cv2.imwrite(newCarName,carImage)
      
   def displayDetails(self):
      print "Name of vehicle: "+self.Name_of_Vehicle
      print "Date of Registration: "+self.Date_of_Registration
      print "Owner Name: "+self.Owner_Name
      print "RTO Number: "+str(self.RTO_Number)
      print "State Number: "+self.State_Number
      print "Number Plate: "+self.Number_Plate
      print "Owner Residence: "+self.Owner_Residence

   def vehicleName(self):
      return self.Name_of_Vehicle
      
   def dateOfRegistration(self):
      return self.Date_of_Registration
      
   def ownerName(self):
      return self.Owner_Name
      
   def rtoNumber(self):
      return self.RTO_Number
      
   def stateNumber(self):
      return self.State_Number
      
   def plateNumber(self):
      return self.Number_Plate
      
   def residence(self):
      return self.Owner_Residence
    
   def getFeatures(self):
      return self.features
      
#function to create car Objects for demonstration
def createCars():
   vehicle_one = Vehicle('Car1','01/03/2015','Kaushik','41','KA','KA412350','RR Nagar')
   vehicle_two = Vehicle('Car2','02/03/2015','Jeevith','06','KA','KA065333','Tumkur')
   vehicle_three = Vehicle('Car3','03/03/2015','Koushik','01','KA','KA014751','Rajajinagar')
   vehicle_four = Vehicle('Car4','04/03/2015','Kunal','41','KA','KA416273','RR Nagar')
   vehicle_five = Vehicle('Car5','05/03/2015','Amit','25','KA','KA251172','Hubli')

#define all required functions
#function to generate green light/red light sequence
def generateLightsequence():
   canvas = np.zeros((300, 300, 3), dtype = "uint8")
   (centerX, centerY) = (canvas.shape[1] / 2, canvas.shape[0] / 2)
   red = (0, 0, 255)
   green = (0,255,0)
   cv2.circle(canvas, (centerX, centerY), 15, red,-1)
   cv2.imwrite("redlight.jpg",canvas)
   cv2.circle(canvas, (centerX, centerY), 15, green,-1)
   cv2.imwrite("greenlight.jpg",canvas)
   
#functions to find center of contour (x,y)
def findXmean(array):
   sum=0
   for i in range(0,len(array)):
      sum+=array[i][0][1]
   return int(sum//len(array))
def findYmean(array):
   sum=0
   for i in range(0,len(array)):
      sum+=array[i][0][0]
   return int(sum//len(array))
   
#initialise light contour to find mean
def init():
   im = cv2.imread('greenlight.jpg',0)
   im2 = cv2.imread('greenlight.jpg')
   blur = cv2.bilateralFilter(im,11,17,17)
   thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
   can = cv2.Canny(thresh,100,200)
   contours,hierarchy = cv2.findContours(can,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
   contour = max(contours, key = cv2.contourArea)
   approx = cv2.approxPolyDP(contour,0.1*cv2.arcLength(contour,True),True)
   return approx
   
#function to simulate a one second delay
def delay():
   for i in range(0,10000000):
      i=i*1
      
#function to calculate red signal time (number of seconds)
def loadVideo(xcenter,ycenter):
   list = ["redlight.jpg","redlight.jpg","redlight.jpg","redlight.jpg","redlight.jpg","greenlight.jpg"]
   secondCount = 0
   for item in list:
      im = cv2.imread(item)
      point = im[xcenter,ycenter]
      if point[1]>250:
         cv2.imshow('press any key to see red signal time',im)
         cv2.waitKey(0)
         break
      else:
         cv2.imshow('current signal',im)
         delay()
         secondCount+=1
   cv2.waitKey(0)
   return secondCount 
   
#mean square error similarity checker function
def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

#cropping function
def crop(image):
   cropped = image[100:image.shape[0], 0:image.shape[1]]
   return cropped
   
#function to identify frame constituting violation and return one
def distanceFromEdge(t1,t2,i):
   black = cv2.imread('black1.jpg')
   d1 = cv2.absdiff(t2,t1)
   d1 = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
   d1 = cv2.cvtColor(d1,cv2.COLOR_GRAY2BGR)
   d1 = kmeans(d1,2)
   x = mse(d1,black)
   if float(x)>123:
      d1 = crop(d1)
      im = d1.copy()
      gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
      blur = cv2.bilateralFilter(gray,11,17,17)
      thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
      can = cv2.Canny(thresh,100,200)
      can2=can.copy()
      contours,hierarchy = cv2.findContours(can,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
      contour = max(contours, key = cv2.contourArea)
      approx = cv2.approxPolyDP(contour,0.1*cv2.arcLength(contour,True),True)
      if int(len(approx))==1:
         xcenter =  approx[0][0][1]
         ycenter = approx[0][0][0]
         im[xcenter,ycenter]=[255,255,255]
         cv2.line(im,(ycenter,xcenter),(im.shape[1],xcenter),(255,255,255))
         if int(im.shape[1]-ycenter)<40:
            #cv2.imwrite('{0:02d}.jpg'.format(i),im)
            return 1
         else:
            return 0
      else:
         xcenter = findXmean(approx)
         ycenter = findYmean(approx)
         im[xcenter,ycenter]=[255,255,255]
         cv2.line(im,(ycenter,xcenter),(im.shape[1],xcenter),(255,255,255))
         if int(im.shape[1]-ycenter)<40:
            #cv2.imwrite('{0:02d}.jpg'.format(i),im)
            return 1
         else:
            return 0

#function to cluster images using k-means clustering
def kmeans(image,clusters):
   (h,w)=image.shape[:2]
   image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
   image = image.reshape((image.shape[0]*image.shape[1],3))
   cluster = MiniBatchKMeans(n_clusters = clusters)
   labels = cluster.fit_predict(image)
   newimage = cluster.cluster_centers_.astype("uint8")[labels]
   newimage = newimage.reshape((h,w,3))
   newimage = cv2.cvtColor(newimage,cv2.COLOR_LAB2BGR)
   return newimage

#function to write coloured keyframes to keyframe folder
def writeFrame(t1,t2,i):
    black = cv2.imread('black1.jpg')
    d1 = cv2.absdiff(t2,t1)
    d1 = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
    d1 = cv2.cvtColor(d1,cv2.COLOR_GRAY2BGR)
    d1 = kmeans(d1,2)
    x = mse(d1,black)
    if float(x)>123:
       cv2.imwrite('project/keyframes/{0:02d}.jpg'.format(i),t2)
       
#function to write keyframes with only foreground objects
def writeClusteredFrame(t1,t2,i):
    black = cv2.imread('black1.jpg')
    d1 = cv2.absdiff(t2,t1)
    d1 = cv2.cvtColor(d1,cv2.COLOR_BGR2GRAY)
    d1 = cv2.cvtColor(d1,cv2.COLOR_GRAY2BGR)
    d1 = kmeans(d1,2)
    x = mse(d1,black)
    if float(x)>123:
       cv2.imwrite('project/clusteredKeyframes/{0:02d}.jpg'.format(i),d1)

#function that returns contoured image
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
   
#function that learns background
def learnbackground():
   c = cv2.VideoCapture('simple.mov')
   _,f = c.read()
   avg = np.float32(f)
   while(1):
      _,f = c.read()
      cv2.accumulateWeighted(f,avg,0.01)
      res = cv2.convertScaleAbs(avg)
      cv2.imshow('Modelling background press esc to stop',res)
      k = cv2.waitKey(20)
      if k == 27:
         break
   cv2.destroyAllWindows()
   c.release()
   return res
   
#function to perform frame differencing and contouring
def diffImg(t1,t2):
   d1=cv2.absdiff(t2,t1)
   gray = cv2.cvtColor(d1, cv2.COLOR_BGR2GRAY)
   return cnts(gray)
   
#string matching algorithm
def findMax(list):
   max = list[0]
   for item in list:
      if item > max:
         max = item
   return max

def stringMatch(str1,str2):
   track,list = 0,[]
   if len(str2) >= len(str1):
      while track < (len(str2) - len(str1) + 1):
         count = 0
         k = track
         for j in range(0,len(str1)):
            if str1[j] == str2[k]:
               count+=1
               k+=1
            else:
               k+=1
         list.append(count)  
         track+=1
   else:
      while track < (len(str1) - len(str2) + 1):
         count = 0
         k = track
         for j in range(0,len(str2)):
            if str2[j] == str1[k]:
               count+=1
               k+=1
            else:
               k+=1
         list.append(count)  
         track+=1
   return findMax(list)

#main function
def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("num",help="The Fibonacci number",type=int)
   args = parser.parse_args()
   '''
   print "1. Obtain foreground\n2. Extract keyframes\n3. Extract key frames foreground only\n4. Find violation"
   print "5. getRedSignalTime\n6. get License plate number\n7. get info\n8. Gaussian mixture model\npress any other key to exit.."
   print "Enter a number as per above instructions.. "
   choice = int(input("Enter your choice: "))
   '''
   if args.num == 1:
      img = learnbackground()
      cam = cv2.VideoCapture('simple.mov')
      while(cam.isOpened()):
         t,f = cam.read()
         cv2.imshow('Foreground objects press Q to stop',diffImg(img,f))
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      cam.release()
      cv2.destroyAllWindows()
   elif args.num == 2:
      scale = 2
      canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
      for i in range(0,300):
         cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
      cv2.putText(canvas,'extracting full colored keyframes...   ', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.putText(canvas,'Press Q to terminate extraction...   ', (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow("CONSOLE",canvas)
      os.system("open ~/project/keyframes")
      cam = cv2.VideoCapture('simple.mp4')
      f0 = cam.read()[1]
      i=0
      while(cam.isOpened()):
          t,f = cam.read()
          writeFrame(f0,f,i)
          f0=f
          i+=1
          if cv2.waitKey(1) & 0xFF == ord('q'):
              break
      cam.release()
      cv2.putText(canvas,'Keyframes extracted in project directory.', (canvas.shape[1] - 600, canvas.shape[0] - 550), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow("CONSOLE",canvas)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
   elif args.num == 3:
      scale = 2
      canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
      for i in range(0,300):
         cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
      cv2.putText(canvas,'extracting keyframes with only foreground objects...  ', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.putText(canvas,'Press Q to terminate extraction...  ', (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow("CONSOLE",canvas)
      cam = cv2.VideoCapture('simple.mp4')
      os.system("open ~/project/clusteredKeyframes")
      f0 = cam.read()[1]
      i=0
      while(cam.isOpened()):
          t,f = cam.read()
          writeClusteredFrame(f0,f,i)
          f0=f
          i+=1
          if cv2.waitKey(1) & 0xFF == ord('q'):
              break
      cam.release()
      cv2.putText(canvas,'Keyframes extracted in project directory.', (canvas.shape[1] - 600, canvas.shape[0] - 550), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow("CONSOLE",canvas)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
   elif args.num == 4:
      scale = 2
      canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
      for i in range(0,300):
         cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
      cv2.putText(canvas,'Finding violation...  ', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow("CONSOLE",canvas)
      cam = cv2.VideoCapture('simple.mp4')
      f0 = cam.read()[1]
      i=0
      while(cam.isOpened()):
          t,f = cam.read()
          n = distanceFromEdge(f0,f,i)
          if n==0:
             f0=f
             i+=1
             if cv2.waitKey(1) & 0xFF == ord('q'):
                 break
          elif n==1:
             cv2.putText(canvas,'Violation found, press Y to capture frames captured to Project directory.', (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
             cv2.imshow('CONSOLE',canvas)
             if cv2.waitKey(0) == ord('y'):
                cv2.putText(f,time.asctime( time.localtime(time.time()) ), (f.shape[1] - 250, f.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)
                cv2.putText(f0,time.asctime( time.localtime(time.time()) ), (f0.shape[1] - 250, f0.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)
                cv2.imwrite('project/violation/{0:02d}.jpg'.format(i+1),f)
                cv2.imwrite('project/violation/{0:02d}.jpg'.format(i),f0)
                break
      cv2.putText(canvas,'Frames captured, Display the frames?(y)', (canvas.shape[1] - 600, canvas.shape[0] - 550), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow('CONSOLE',canvas)
      k = cv2.waitKey(0)
      if k == ord('y'):
         cv2.imshow("Captured frames, press any key to exit", np.hstack([f0, f]))
         cv2.waitKey(0)
      cam.release()
      cv2.destroyAllWindows()
   elif args.num == 5:
      scale = 2
      canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
      for i in range(0,300):
         cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
      cv2.putText(canvas,'calculating red signal time...', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow('CONSOLE',canvas)
      generateLightsequence()
      approx = init()
      xcenter = findXmean(approx)
      ycenter = findYmean(approx)
      count = loadVideo(xcenter,ycenter)
      cv2.putText(canvas,"timespan of red signal is " + str(count)+" seconds.", (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow('CONSOLE',canvas)
      cv2.waitKey(0)
   elif args.num == 6:
      scale = 2
      canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
      for i in range(0,300):
         cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
      cv2.putText(canvas,'Create cars for demonstration?(y)', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow('CONSOLE',canvas)
      if cv2.waitKey(0) == ord('y'):
         cv2.putText(canvas,'Creating cars...', (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.imshow('CONSOLE',canvas)
         createCars()
         cv2.putText(canvas,'Reading car objects...', (canvas.shape[1] - 600, canvas.shape[0] - 550), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.imshow('CONSOLE',canvas)
         delay()
         cv2.putText(canvas,'Extracting plate numbers...', (canvas.shape[1] - 600, canvas.shape[0] - 530), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.imshow('CONSOLE',canvas)
         for vehicle in Vehicle.vehicleList:
            carObject = Vehicle.vehicleList[vehicle]
            features = carObject.getFeatures()
            carName = "project/cars/"+carObject.vehicleName()+".jpg"
            carImage = cv2.imread(carName)
            plateName = "project/plates/"+carObject.vehicleName()+"Plate.jpg"
            tempCarImage = carImage.copy()
            x = tempCarImage.shape[0]//features[0]
            y = tempCarImage.shape[1]//features[1]
            plateImage = tempCarImage[x+features[2]:tempCarImage.shape[0]-features[3],y+features[4]:tempCarImage.shape[1]-features[5]]
            cv2.imwrite(plateName,plateImage)
         delay()
         cv2.putText(canvas,'Extraction of plates in directory plates completed', (canvas.shape[1] - 600, canvas.shape[0] - 510), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.putText(canvas,'Continue with training classifier?(y)', (canvas.shape[1] - 600, canvas.shape[0] - 490), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.imshow('CONSOLE',canvas)
         k = cv2.waitKey(0)
         if k == ord('y'):         
            cv2.destroyAllWindows()
            os.system("/anaconda/bin/python train.py --dataset data/digits.csv --model models/svm.cpickle")
      else:
         exit()
   elif args.num == 7:
      createCars()
      scale = 2
      canvas = np.zeros((300*scale, 300*scale, 3), dtype = "uint8")
      for i in range(0,300):
         cv2.line(canvas,(i*scale,0),(i*scale,300*scale),(0,100,0))
      cv2.putText(canvas,'getting information about number stored in file', (canvas.shape[1] - 600, canvas.shape[0] - 590), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
      cv2.imshow('CONSOLE',canvas)
      file = open("project/number.txt", "r+")
      fstr = file.read(10);
      file.close()
      if len(fstr)==0:
         cv2.putText(canvas, "No match found!", (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.imshow('CONSOLE',canvas)
         cv2.waitKey(0)
      else:
         count = 0
         for vehicle in Vehicle.vehicleList:
            if int(stringMatch(vehicle,fstr)) >= 3:
               count+=1
               cv2.putText(canvas, str(count), (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
               cv2.putText(canvas,'close match found and Vehicle information is as follows:', (canvas.shape[1] - 580, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
               cv2.imshow('CONSOLE',canvas)
               if cv2.waitKey(0) == ord('d'):
                  Vehicle.vehicleList[vehicle].displayDetails()
                  nameString, dorString, oName, rNumber, sNumber, nPlate, oResidence = "","","","","","",""
                  nameString += "Name of Vehicle: "+ Vehicle.vehicleList[vehicle].vehicleName()
                  dorString += "Date of Registration: "+ Vehicle.vehicleList[vehicle].dateOfRegistration()
                  oName += "Owner Name: "+ Vehicle.vehicleList[vehicle].ownerName()
                  rNumber += "RTO Number: "+ str(Vehicle.vehicleList[vehicle].rtoNumber())
                  sNumber += "State Number: "+ Vehicle.vehicleList[vehicle].stateNumber()
                  nPlate += "Plate Number: "+ Vehicle.vehicleList[vehicle].plateNumber()
                  oResidence += "Owner Residence: "+ Vehicle.vehicleList[vehicle].residence()
                  cv2.putText(canvas, nameString, (canvas.shape[1] - 600, canvas.shape[0] - 540+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  cv2.putText(canvas,dorString, (canvas.shape[1] - 600, canvas.shape[0] - 520+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  cv2.putText(canvas,oName, (canvas.shape[1] - 600, canvas.shape[0] - 500+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  cv2.putText(canvas,rNumber, (canvas.shape[1] - 600, canvas.shape[0] - 480+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  cv2.putText(canvas,sNumber, (canvas.shape[1] - 600, canvas.shape[0] - 460+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  cv2.putText(canvas,nPlate, (canvas.shape[1] - 600, canvas.shape[0] - 440+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  cv2.putText(canvas,oResidence, (canvas.shape[1] - 600, canvas.shape[0] - 420+220), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
                  img = cv2.imread("Desktop/cars/"+str(Vehicle.vehicleList[vehicle].vehicleName())+".jpg")
                  img = imutils.resize(img, height = 150)
                  x_offset = 220
                  y_offset = 100
                  canvas[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
                  cv2.imshow('CONSOLE',canvas)
                  cv2.waitKey(0)
            else:
               continue
      if count == 0:
         cv2.putText(canvas, "No match found!", (canvas.shape[1] - 600, canvas.shape[0] - 570), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
         cv2.imshow('CONSOLE',canvas)
         cv2.waitKey(0)
   elif args.num == 8:
      cap = cv2.VideoCapture('simple.mov')
      fgbg = cv2.BackgroundSubtractorMOG2()
      while(1):
         ret, frame = cap.read()
         fgmask = fgbg.apply(frame,learningRate=0.05)
         cv2.imshow('frame',fgmask)
         k = cv2.waitKey(30) & 0xff
         if k == 27:
            break
      cap.release()
      cv2.destroyAllWindows()
   else:
      exit()

#execute the main function to start the program
if __name__ == "__main__":
   main()

