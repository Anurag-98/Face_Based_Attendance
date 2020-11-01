import cv2
import numpy as np
import sqlite3
import smtplib
import datetime
import time
import Tkinter as tk

root=tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

today=datetime.date.today();
date_td=today.strftime("%d %B, %Y");
date_td.replace(" ","");
 
def create_entry(conn, entry, subject):
 sql = ''' INSERT INTO "{}" (ID,NAME,ATTANDANCE,DATE,TIME)
              VALUES(?,?,?,?,?) '''.format(subject);
 cur = conn.cursor()
 cur.execute(sql, entry)
 return cur.lastrowid

def addit(conn, un, subject):
    cur = conn.cursor()
    cur.execute("SELECT * FROM MASTER WHERE RNO=?", (un,))
 
    rows = cur.fetchall()
    time=str(datetime.datetime.now())
    l=len(time);
    time=time[10:l]
    entry=(int(rows[0][0]), str(rows[0][1]), 'PRESENT',date_td,time);
    create_entry(conn,entry, subject);
    return rows[0][1]

def create_table(conn, subject):
    sql_create = ''' CREATE TABLE IF NOT EXISTS "{}" (
	`ID`	INT NOT NULL,
        `NAME`	TEXT NOT NULL,
	`ATTANDANCE`	TEXT,
	`DATE`   TEXT,
	`TIME`	TEXT) '''.format(subject);
    cur = conn.cursor()
    cur.execute(sql_create)
    return
def face_att(subject):     
 faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
 cam = cv2.VideoCapture(0);
 rec = cv2.createLBPHFaceRecognizer();
 rec.load("recognizer\\trainningData.yml")

 name="none"
 id=0
 #faceCascade = cv2.CascadeClassifier(cascadePath);
 font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4,)
 while (True):
    ret, img =cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetector.detectMultiScale(gray, 1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id, conf = rec.predict(gray[y:y+h,x:x+w])

        conn = sqlite3.connect('test.db')
        create_table(conn, subject);
        conn.execute('''DELETE from "{}" where ID=? AND DATE=?'''.format(subject), (id,date_td))
        #cursor = conn.execute("SELECT id, name, address, attandance,time  from COMPANY")
        name=addit(conn,id, subject);
        cut=len(name);
        name=name[0:cut-1];
        conn.commit()
        conn.close()
           

            
        cv2.cv.PutText(cv2.cv.fromarray(img),str(name), (x,y+h),font, 255);
    cv2.imshow('Face',img); 
    if (cv2.waitKey(1)==ord('q')):
        break;
    
    
 cam.release()
 cv2.destroyAllWindows()

def get_subject():
 #subject=e1.get()
 subject=radbt.get()
 subject=subject+dt
 root.destroy()
 face_att(subject)

radbt=tk.StringVar();
dt=today.strftime("%B, %Y");
dt.replace(" ","");
#e1=tk.Entry(root,text="enter subject")
#canvas1.create_window(200, 140, window=e1)
r1=tk.Radiobutton(root,text="Soft Computing", value="soft_computing",variable=radbt)
canvas1.create_window(200, 20, window=r1)
r1.select()
r2=tk.Radiobutton(root,text="ADHOC and Sensor Networks", value="ASN",variable=radbt)
canvas1.create_window(200, 60, window=r2)
r2.deselect()
r3=tk.Radiobutton(root,text="Human Values and Professional Ethics 2", value="HVPEII",variable=radbt)
canvas1.create_window(200, 100, window=r3)
r3.deselect()
r4=tk.Radiobutton(root,text="Mobile Computing", value="mobile_comp",variable=radbt)
canvas1.create_window(200, 140, window=r4)
r4.deselect()
r5=tk.Radiobutton(root,text="E-commerce/M-Commerce", value="EcomMcom",variable=radbt)
canvas1.create_window(200, 180, window=r5)
r5.deselect()
b1=tk.Button(root,text="ENTER SUBJECT", command=get_subject)
canvas1.create_window(200, 200, window=b1)
b1.pack();
root.mainloop()
