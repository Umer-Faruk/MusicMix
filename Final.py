from tkinter import *
from tkinter import scrolledtext
import pygame
import os


class Final :
     def __init__(self,root):

          
          self.root = root
          self.root.title("Musicmix")
          self.root.geometry('900x600+200+200')
          # self.sl = ["asdas","asdasd","asdads","wqewqe","wqewad","awedad","sdasd","asd","asdasd","sadad","asdasd","asdasd","adsasd","asdas","asdasd","asdads","wqewqe","wqewad","awedad","sdasd","asd","asdasd","sadad","asdasd","asdasd","adsasd"]
          pygame.init()
          pygame.mixer.init()
          self.dpath = os.path.dirname(os.path.realpath(__file__))
          print(self.dpath)
          self.trackname = StringVar()
          self.musicpath = StringVar()
          self.musiclen = 00.0
         

          
          songlist = LabelFrame(self.root,text="songTreack",bd=5,bg="grey")
          songlist.place(x= 700 ,y = 0 , width = 200,height = 400)



          trackinfo = LabelFrame(self.root,text="trackinfo",bd=5)
          trackinfo.place(x=0,y=0,width=700,height=100)
          songname = Label(trackinfo,textvariable = self.trackname ,width =20,font=("times new roman",24,"bold")).grid(row=0,column=0,padx=10,pady=5)

          controls = LabelFrame(self.root,text="controls",bd=5,bg = "grey")
          controls.place(x=0,y=400,width=700,height=100)

          buton = Button(controls,text="play",command=self.play).grid(row=0,column=0,padx=10,pady=5)
          buton = Button(controls,text="stop",command=self.stop).grid(row=0,column=1,padx=10,pady=5)
          buton = Button(controls,text="pause",command=self.pause).grid(row=0,column=2,padx=10,pady=5)
          buton = Button(controls,text="start",command=self.start).grid(row=0,column=3,padx=10,pady=5)

          scrollbar = Scrollbar(songlist)
          scrollbar.pack(side=RIGHT, fill=Y)
          
          self.tracklist = Listbox(songlist)
          self.tracklist.pack(fill = BOTH)
          self.tracklist.place(height=400)
          self.tracklist.config(yscrollcommand=scrollbar.set)
          scrollbar.config(command= self.tracklist.yview)



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
          self.trackname.set(self.tracklist.get(ACTIVE))
          print("working")
          print(self.trackname)
          pygame.mixer.music.load(self.tracklist.get(ACTIVE))
        
          

          pygame.mixer.music.play()
         
          


     def stop(self):
          pygame.mixer.music.stop()
       
     def pause(self):
          pygame.mixer.music.pause()
     def start(self):
          pygame.mixer.music.unpause()

     def setdpath(self):
          print(self.dpathin.get())
          self.dpath= self.dpathin.get()
          self.sl = os.listdir( str(self.dpath))
          for i in self.sl:
               if i.endswith('.mp3') or i.endswith('.wav') or i.endswith('.aif') or i.endswith('.ogg') or i.endswith('.wma') or i.endswith('.acc') or i.endswith('.ra'): 
               
                     self.tracklist.insert(END,i)

     


root = Tk()
Final(root)
root.mainloop()


