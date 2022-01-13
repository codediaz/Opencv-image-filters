from tkinter import *
from tkinter import filedialog
from PIL import Image
import cv2
import imutils

root = Tk()

btnIniciar = Button(root,text="Iniciar", width=45)
btnIniciar.grid(column=0,row=0,padx=5, pady=5)

btnFinalizar = Button(root,text="Finalizar", width=45)
btnFinalizar.grid(column=1,row=0,padx=5, pady=5)


lblVideo = Label(root)
lblVideo.grid(column=0,row=1,columnspan=2)
root.mainloop()

