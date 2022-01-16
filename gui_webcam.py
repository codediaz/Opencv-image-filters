from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
import cv2
import imutils
from Filters.utils import CFEVideoConf, image_resize
import numpy as np
import matplotlib.pyplot as plt

# Configure VideoCapture class instance for using camera or file input.
bins = 16
var = 0

# Initialize plot.
# Initialize plot.
fig, ax = plt.subplots()
ax.set_title('Histogram Stream Video')
ax.set_xlabel('Bin')
ax.set_ylabel('Frequency')

# Configure VideoCapture
global capure
capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Initialize plot line object(s). Turn on interactive plotting and show plot.
lw = 3
alpha = 0.5
lineR, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', lw=lw, alpha=alpha)
lineG, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', lw=lw, alpha=alpha)
lineB, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', lw=lw, alpha=alpha)
ax.set_xlim(0, bins-1)
ax.set_ylim(0, 1)
plt.ion()
plt.show()



def show():
    global cap 
    if cap is not None:
        ret,frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width = 640)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image =im)
            
            lblVideo.configure(image = img)
            lblVideo.image = img
            lblVideo.after(10,show)
            
        else:
            lblVideo.image = ""
            cap.relase()

        

"""def iniciar():
    # initialize the video stream
    print("[INFO] starting video stream...")    
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    show()"""
    
def iniciar():
        while True:
            (grabbed, frame) = capture.read()

            if not grabbed:
                break
            
            
            # Resize frame to width, if specified.
            numPixels = np.prod(frame.shape[:2]) 
            (b, g, r) = cv2.split(frame)
            histogramR = cv2.calcHist([r], [0], None, [bins], [0, 255]) / numPixels
            histogramG = cv2.calcHist([g], [0], None, [bins], [0, 255]) / numPixels
            histogramB = cv2.calcHist([b], [0], None, [bins], [0, 255]) / numPixels
            lineR.set_ydata(histogramR)
            lineG.set_ydata(histogramG)
            lineB.set_ydata(histogramB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image =im)
            fig.canvas.draw()

            global cap
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
           

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

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
btnIniciar.grid(column=0,row=0,padx=5, pady=40)

btnFinalizar = Button(root,text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1,row=0,padx=5, pady=40)

#Botones para seleccionar los filtros 
btnFiltro1 = Button(root,text="Filtro1", width=25, command=Filtro1)
btnFiltro1.grid(column=0,row=2,padx=5, pady=40)

btnFiltro2 = Button(root,text="Filtro2", width=25, command=Filtro2)
btnFiltro2.grid(column=0,row=3,padx=5, pady=40)

btnFiltro3 = Button(root,text="Filtro3", width=25, command=Filtro3)
btnFiltro3.grid(column=0,row=4,padx=5, pady=40)

#VideoStream de salida
lblVideo = Label(root)
lblVideo.grid(column=1,row=1, rowspan=6)

#Label 
lblInfoFiltros = Label(root, text ="Elija un filtro, por favor", width=25)
lblInfoFiltros.grid(column=0,row=1, padx=5,pady=5)

root.mainloop()
cap.release()
cv2.destroyAllWindows()

