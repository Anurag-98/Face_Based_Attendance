import Tkinter as tk
import sys
import os
import tkMessageBox

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
username="supervisor"
password="bpit@123"
def capture_img():
 os.system('01_face_dataset.py')

def train_img():
 os.system('02_face_training.py')

def face_att():
 os.system('AT.py')

def login():
 user=e1.get()
 pw=e2.get()
 if(user!=username or pw!=password):
   l=tk.Label(root, text="Wrong Credentials")
   canvas1.create_window(200,100,window=l)
 elif(user==username and pw==password):
   root.destroy()
   mains()
l1=tk.Label(root,text="Enter Username")
l2=tk.Label(root,text="Enter Password")
e1=tk.Entry(root,text="Enter Username")
e2=tk.Entry(root,text="Enter Password",show="*")
canvas1.create_window(200,20,window=l1)
canvas1.create_window(200,60,window=l2)
canvas1.create_window(200,40,window=e1)
canvas1.create_window(200,80,window=e2)
bb=tk.Button(root, text="LOGIN",command=login)
canvas1.create_window(200,200,window=bb)
bb.pack()
def mains():
 node=tk.Tk();
 canvas2 = tk.Canvas(node, width = 400, height = 300)
 canvas2.pack()
 b1=tk.Button(node,text="ADD FACE TO DATABASE",command=capture_img)
 canvas2.create_window(200,40,window=b1)
 b2=tk.Button(node,text="TRAIN IMAGES",command=train_img)
 canvas2.create_window(200,60,window=b2)
 b3=tk.Button(node,text="START WEBCAM FOR ATTENDANCE",command=face_att)
 canvas2.create_window(200,80,window=b3)
 b1.pack()
 b2.pack()
 b3.pack()
 node.mainloop()
 
root.mainloop()
