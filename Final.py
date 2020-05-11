from tkinter import *
from tkinter import scrolledtext
import pygame
import os
import mutagen.mp3
try:
    import pkg_resources.py2_warn
except ImportError:
    pass

class Final :
     def __init__(self,root):

          
          self.root = root
          self.root.title("Musicmix")
          self.root.geometry('900x600+200+200')
          # self.sl = ["asdas","asdasd","asdads","wqewqe","wqewad","awedad","sdasd","asd","asdasd","sadad","asdasd","asdasd","adsasd","asdas","asdasd","asdads","wqewqe","wqewad","awedad","sdasd","asd","asdasd","sadad","asdasd","asdasd","adsasd"]
          pygame.init()
          # pygame.mixer.init()
          self.dpath = os.path.dirname(os.path.realpath(__file__))
          print(self.dpath)
          self.trackname = StringVar()
          self.musicpath = StringVar()
          self.musiclen = 00.0
          
          
         

          
          songlist = LabelFrame(self.root,text="songTreack",bd=5,bg="grey")
          songlist.place(x= 700 ,y = 0 , width = 200,height = 400)



          trackinfo = LabelFrame(self.root,text="trackinfo",bd=5)
          trackinfo.place(x=0,y=0,width=700,height=100)
          songname = Label(trackinfo,textvariable = self.trackname,width =20,font=("times new roman",24,"bold")).grid(row=0,column=0,padx=10,pady=5)

     #control panel 

          self.controls = LabelFrame(self.root,text="controls",bd=5,bg = "grey")
          self.controls.place(x=0,y=400,width=700,height=100)

          self.pbuton = Button(self.controls,text="play",command=self.play)
          self.pbuton.grid(row=0,column=0,padx=10,pady=5)
          self.pbuton.configure(bg="green") 

          

          self.sbuton = Button(self.controls,text="stop",command=self.stop)
          self.sbuton.grid(row=0,column=1,padx=10,pady=5)
          self.sbuton.configure(bg="red") 


          self.pubuton = Button(self.controls,text="pause",command=self.pause)
          self.pubuton.grid(row=0,column=2,padx=10,pady=5)
          self.pubuton.configure(bg="yellow") 

          

          self.stbuton = Button(self.controls,text="start",command=self.start)
          self.stbuton.grid(row=0,column=3,padx=10,pady=5)
          self.stbuton.configure(bg="green")

          scrollbary = Scrollbar(songlist)
          scrollbarx = Scrollbar(songlist, orient=HORIZONTAL)
          scrollbary.pack(side=RIGHT, fill=Y)
          
          self.tracklist = Listbox(songlist)
          # self.tracklist.pack(fill = BOTH)
          self.tracklist.place(height=400)
          self.tracklist.config(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
          scrollbary.config(command= self.tracklist.yview)
          scrollbarx.config(command=self.tracklist.xview)
          # self.tracklist.pack(fill = BOTH)
          scrollbarx.pack(side=BOTTOM, fill=X)
          self.tracklist.pack(side=LEFT, fill=BOTH)
          scrollbary.pack(side=RIGHT, fill=Y)
          



          self.dpathin = Entry(self.root,bg="white",fg="red")
          dpathl = Label(self.root,text="set the Directory path \n load songs",)
          dpathl.place(x=700,y=400,width = 200,height=40)
         
         
          self.dpathin.place(x=700,y=450,width=200,height=20)
          botn = Button(self.root,text="OK",command=self.setdpath)
          botn.place(x=750,y=470)

      
         
         


     
          # /home/umer/Desktop
          # os.listdir(self.dpath)

          self.sl = os.listdir( str(self.dpath))

          for i in self.sl:
               if i.endswith('.mp3') or i.endswith('.wav') or i.endswith('.aif') or i.endswith('.ogg') or i.endswith('.wma') or i.endswith('.acc') or i.endswith('.ra'): 
                    self.tracklist.insert(END,i)

          if self.tracklist.size() == 0 :
               print("no audio file s are found")
               self.trackname.set("no audio  file found ")
          else:
               print("aoudio file found!!")

     def play(self):
               
               # self.pbuton.configure(bg="green") 
               self.controls.configure(bg="#1feb00") 
               mp3 = mutagen.mp3.MP3(self.tracklist.get(ACTIVE))
               print(mp3)
               pygame.mixer.init(frequency=mp3.info.sample_rate)
        
               self.trackname.set(self.tracklist.get(ACTIVE))
             
               pygame.mixer.music.load(self.tracklist.get(ACTIVE))
             
               pygame.mixer.music.play()
          

         
          


     def stop(self):
          # self.sbuton.configure(bg="red") 
          self.controls.configure(bg="#ff5524") 
          pygame.mixer.music.stop()
       
     def pause(self):
          # self.pubuton.configure(bg="yellow") 
          self.controls.configure(bg="yellow") 
          pygame.mixer.music.pause()
     def start(self):
          # self.stbuton.configure(bg="green")
          self.controls.configure(bg="lightgreen")  
          pygame.mixer.music.unpause()

     def setdpath(self):
          print(self.dpathin.get())

          self.dpath= self.dpathin.get()
          
          self.sl = os.listdir( str(self.dpath))
          for i in self.sl:
               if i.endswith('.mp3') or i.endswith('.wav') or i.endswith('.aif') or i.endswith('.ogg') or i.endswith('.wma') or i.endswith('.acc') or i.endswith('.ra'): 
               
                     self.tracklist.insert(END,os.path.join(self.dpath,i))

     


root = Tk()
Final(root)
root.mainloop()


