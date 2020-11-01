import sys
import cv2
import os
import Tkinter as tk
import sqlite3
import sys
import tkMessageBox
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
face_id=00

def getID ():
    face_id=entry1.get();
    root.destroy();
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    sql="SELECT * from MASTER WHERE RNO = {}".format(face_id);
    cur.execute(sql);
    rows=cur.fetchall()
    if(len(rows)==0):
      print("RECORD DOESN'T EXIST IN MASTER TABLE")
      tkMessageBox.showerror("INVALID ID", "Record with the provided ID not found in MASTER Table");
      sys.exit()
    else:
      take_img(face_id);
      #label1 = tk.Label(root, text= float(x1)**0.5)
      #canvas1.create_window(200, 230, window=label1) 
entry1 = tk.Entry(root) 
canvas1.create_window(200, 140, window=entry1)
button1 = tk.Button(text='Submit ID', command=getID)
canvas1.create_window(200, 180, window=button1)

def take_img(face_id):
 cam = cv2.VideoCapture(0)
 cam.set(3, 640) # set video width
 cam.set(4, 480) # set video height

 face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 # For each person, enter one numeric face id
 #face_id = input('\n enter user id end press <return> ==>  ')
 #print("\n [INFO] Initializing face capture. Look the camera and wait ...")
 # Initialize individual sampling face count
 count = 0

 while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

 # Do a bit of cleanup
 print("\n [INFO] Exiting Program and cleanup stuff")
 cam.release()
 cv2.destroyAllWindows()
root.mainloop()
