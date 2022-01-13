from tkinter import *
from tkinter import filedialog
from PIL import Image
import cv2
import imutils

def iniciar():
    global cap
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    show()

cap = None
root = Tk()

btnIniciar = Button(root,text="Iniciar", width=45, command = iniciar)
btnIniciar.grid(column=0,row=0,padx=5, pady=5)

btnFinalizar = Button(root,text="Finalizar", width=45)
btnFinalizar.grid(column=1,row=0,padx=5, pady=5)


lblVideo = Label(root)
lblVideo.grid(column=0,row=1,columnspan=2)
root.mainloop()

