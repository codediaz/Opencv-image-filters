from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import cv2
import imutils

def show():
    global cap 
    if cap is not None:
        ret,frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width = 640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image =im)
            
            lblVideo.configure(image = img)
            lblVideo.image = img
            lblVideo.after(10,show)
            
        else:
            lblVideo.image = ""
            cap.relase()
        

def iniciar():
    # initialize the video stream
    print("[INFO] starting video stream...")    
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    show()

def finalizar():
    # initialize the video stream
    print("[INFO] end video stream...")  
    global cap
    cap.release()
    
def Filtro1():
    print("[INFO] starting filter 1 in video stream...") 
    global cap 
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    if cap is not None:
        ret,frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width = 640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image =im)
            
            lblVideo.configure(image = img)
            lblVideo.image = img
            lblVideo.after(10,show)
            
        else:
            lblVideo.image = ""
            cap.relase()
    
def Filtro2():
    print("[INFO] starting filter 2 in video stream...") 
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    if cap is not None:
        ret,frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width = 640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image =im)
            
            lblVideo.configure(image = img)
            lblVideo.image = img
            lblVideo.after(10,show)
            
        else:
            lblVideo.image = ""
            cap.relase()
      

def Filtro3():
    print("[INFO] starting filter 3 in video stream...") 
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    if cap is not None:
        ret,frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width = 640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image =im)
            
            lblVideo.configure(image = img)
            lblVideo.image = img
            lblVideo.after(10,show)
            
        else:
            lblVideo.image = ""
            cap.relase()

    
cap = None

root = Tk()

btnIniciar = Button(root,text="Iniciar", width=45, command = iniciar)
btnIniciar.grid(column=0,row=0,padx=5, pady=5)

btnFinalizar = Button(root,text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1,row=0,padx=5, pady=5)


btnFiltro1 = Button(root,text="Filtro1", width=25, command=Filtro1)
btnFiltro1.grid(column=0,row=2,padx=5, pady=5)

btnFiltro2 = Button(root,text="Filtro2", width=25, command=Filtro2)
btnFiltro2.grid(column=1,row=2,padx=5, pady=5)

btnFiltro3 = Button(root,text="Filtro3", width=25, command=Filtro3)
btnFiltro3.grid(column=2,row=2,padx=5, pady=5)

lblVideo = Label(root)
lblVideo.grid(column=0,row=1,columnspan=3)
root.mainloop()

