#Importar libreria
from tkinter import *
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image

pygame.init()#Este metodo inicia la libreria pygame

def openSong():
    song = filedialog.askopenfilename()
    print(song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def playSong():
    pygame.mixer.music.play()

def stopSong():
    pygame.mixer.music.stop()

def resumeSong():
    pygame.mixer.music.unpause()

def pauseSong():
    pygame.mixer.music.pause()
    
def VolumUpper():
    nivelVolumen= pygame.mixer.music.get_volume()+0.3
    pygame.mixer.music.set_volume(nivelVolumen)
    
def VolumLower():
    nivelVolumen=pygame.mixer.music.get_volume()-0.3
    pygame.mixer.music.set_volume(nivelVolumen)



raiz = Tk()
raiz.title("Reproductor Mp3 - GUI")
#raiz.iconbitmap("disk-jockey.ico")
raiz.geometry("600x400")
raiz.resizable(1,1)


#frame o marco
framePrincipal = Frame(raiz, bg ="#4d4d4d", width=600, height=400)
framePrincipal.pack(fill="both", expand=1)

imagenChida= Image.open("tesla.jpg")
imagenReproductor= imagenChida.resize((300,200))
img = ImageTk.PhotoImage(imagenReproductor)

#Titulo imagen
tituloImagen= Label(framePrincipal, image=img)
tituloImagen.pack()

#titulo reproductor
tituloreproductor = Label(framePrincipal, text="Reproductor GUI", bg="#4d4d4d", fg="#f4f4f4", font=("Roboto", 14))
tituloreproductor.place(relx=0.4, rely=0.55)

#botonopenfile
botonopenfile = Button(framePrincipal, text = "Open File" , font=("Roboto", 14, "bold"), bg="#5dc460", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, command=openSong)
botonopenfile.place(relx=0.0, rely=0.7 )

#botonplaysong
botonplaysong = Button(framePrincipal, text = "Play Song" , font=("Roboto", 14, "bold"), bg="#5dc460", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, command=playSong)
botonplaysong.place(relx=0.2, rely=0.7 )

#botonstop
botonstop = Button(framePrincipal, text = "Stop" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, command=stopSong)
botonstop.place(relx=0.4, rely=0.7 )

#botonresume
botonresume = Button(framePrincipal, text = "Resume" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, command=resumeSong)
botonresume.place(relx=0.6, rely=0.7 )

#botonpause
botonpause = Button(framePrincipal, text = "Pause" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, command=pauseSong)
botonpause.place(relx=0.8, rely=0.7 )

#BotonVolumenUpper
BotonVUP=Button(framePrincipal,text="Vupper +",font=("Roboto",20, "bold"),bg="#334eaf" ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=VolumUpper)
BotonVUP.place(relx=0.8,rely=0.8)

#Boton VolumenLower
BotonVL=Button(framePrincipal,text="Vlower -",font=("Roboto",20, "bold"),bg="#4f5f6f" ,fg="#f4f4f4",width=8,height=1,bd=0,highlightthickness=0,command=VolumLower)
BotonVL.place(relx=0.6,rely=0.8)



raiz.mainloop()