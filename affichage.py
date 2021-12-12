from tkinter import *
from tkinter import ttk
from jeu import Jeu

            
class affichage:

    __dir = ' '

    def __init__(self,x_p,y_p,rows,columns):
        self.__rows = rows
        self.__columns = columns
        self.__jeu = Jeu(self.__rows,self.__columns)
        self.__root = Tk()
        self.__root.bind("<KeyPress-z>",self.zPress)
        self.__root.bind("<KeyPress-s>",self.sPress)
        self.__root.bind("<KeyPress-q>",self.qPress)
        self.__root.bind("<KeyPress-d>",self.dPress)
        self.__root.geometry(str(x_p) + "x" + str(y_p))
        self.__root.update()
        self.__canvas = Canvas(self.__root, width=self.__root.winfo_width(), height=self.__root.winfo_height(), bg="#7698A6")
        self.__canvas.pack(side=RIGHT)
        self.__frame = Frame(self.__root, width=self.__root.winfo_width(), height=self.__root.winfo_height(), bg="#F23E2E")
        self.__frame.pack(side=RIGHT)
        self.update_clock()
        self.__root.mainloop()

    def updateaff(self,plateau_l):
        self.__canvas.delete('all')
        for i in range(len(plateau_l)):
            y = i * (self.__root.winfo_width()/self.__columns)
            for j in range(len(plateau_l)):
                x = j * (self.__root.winfo_height()/self.__rows)
                if plateau_l[i][j] == 's':
                    self.__canvas.create_rectangle(x, y, x+(self.__root.winfo_width()/self.__columns), y+(self.__root.winfo_height()/self.__rows), fill="#E21D22")
                elif plateau_l[i][j] == ' ':
                    self.__canvas.create_rectangle(x, y, x+(self.__root.winfo_width()/self.__columns), y+(self.__root.winfo_height()/self.__rows), fill="#D97E4A")
                elif plateau_l[i][j] == 'b':
                    self.__canvas.create_rectangle(x, y, x+(self.__root.winfo_width()/self.__columns), y+(self.__root.winfo_height()/self.__rows), fill="#16A13B")
    
    def zPress(self,event):
        # print("touche z pressed")
        if self.__dir != "down":
            self.__dir = "up"
        else:
            return

    def sPress(self,event):
        # print("touche s pressed")
        if self.__dir != "up":
            self.__dir = "down"
        else:
            return

    def qPress(self,event):
        # print("touche q pressed")
        if self.__dir != "right":
            self.__dir = "left"
        else:
            return

    def dPress(self,event):
        # print("touche d pressed")
        if self.__dir != "left":
            self.__dir = "right"
        else:
            return

    def update_clock(self):
        # print("foo")
        try:
            self.__jeu.snakeMove(self.__dir)
        except:
            print("C'est perdu")
            return
        self.updateaff(self.__jeu.getPlateau())
        self.__root.after(150, self.update_clock)