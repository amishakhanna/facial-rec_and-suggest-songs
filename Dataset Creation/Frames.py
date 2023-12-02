
import cv2
import os
#import pafy


video_path = 'D:\movies\Fear.mp4' # video name
output_path = 'D:\projects\Music-Recommendation-System-based-on-Facial-Emotions-Recognition-main\Music-Recommendation-System-based-on-Facial-Emotions-Recognition-main\Images\Fear' # location on ur pc

if not os.path.exists(output_path):
     os.makedirs(output_path)


cap = cv2.VideoCapture(video_path)
#cap = cv2.VideoCapture(play.url)
index = 0

while cap.isOpened() :
     Ret, Mat = cap.read()
     
     if Ret :
          index += 1
          if index % 9 != 0 :
               continue
          
          cv2.imwrite(output_path + '/' + str(index) + '.png', Mat)
     
     else:
          break

cap.release()