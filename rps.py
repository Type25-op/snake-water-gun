import os
import random
import customtkinter as ctk
# Coded By Govind Goyal
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}") # snake:0 water:1 gun:2
        self.soln_matrix = [[0,1,2],[2,0,1],[1,2,0]]# 0:draw 1:win 2:lose
        self.ctr_win = 0
        self.ctr_loose = 0
        self.ctr_draw = 0
        self.lts = ['Snake','Water','Gun']
        self.wins  = ctk.CTkLabel(self,text="Wins \n"+str(self.ctr_win))
        self.loose  = ctk.CTkLabel(self,text="Losses \n"+str(self.ctr_loose))
        self.draw  = ctk.CTkLabel(self,text="Draws \n"+str(self.ctr_draw))
        self.snake = ctk.CTkButton(self,text='Snake',command=self.calc0)
        self.water = ctk.CTkButton(self,text='Water',command=self.calc1)
        self.gun = ctk.CTkButton(self,text='Gun',command=self.calc2)
        self.reset_b = ctk.CTkButton(self,text='reset',command=self.reset)

        self.current = ctk.CTkLabel(self,text="You Played :\nComputer Played:")

        # self.test  = ctk.CTkLabel(self,textvariable=self.test_var)
        self.wins.place(relx =0.5,rely = 0.25)
        self.draw.place(relx =0.3,rely = 0.25)
        self.loose.place(relx =0.7,rely = 0.25)
        self.current.place(relx=0.45,rely=0.4)
        self.snake.place(relx =0.45,rely = 0.55)
        self.water.place(relx =0.25,rely = 0.55)
        self.gun.place(relx =0.65,rely = 0.55)
        self.reset_b.place(relx =0.45,rely = 0.75)
        # self.test.place(relx =0.5,rely = 0.5)
    def calc0(self):self.calc(0)
    def calc1(self):self.calc(1)
    def calc2(self):self.calc(2)
    def calc(self,chosen:int):
        # print(f"ran with  {chosen}")
        computer:int = random.randint(0,2)
        scr = f"You Played :{self.lts[chosen]}\nComputer Played:{self.lts[computer]}"
        if self.soln_matrix[chosen][computer] == 0:self.ctr_draw +=1
        elif self.soln_matrix[chosen][computer] == 1:self.ctr_win +=1
        elif self.soln_matrix[chosen][computer] == 2:self.ctr_loose +=1
        else:pass
        self.draw.configure(self,text="Draws \n"+str(self.ctr_draw))
        self.wins.configure(self, text="Win \n" + str(self.ctr_win))
        self.loose.configure(self, text="Loose \n" + str(self.ctr_loose))
        self.current.configure(self, text=scr)
        # print(self.ctr_draw,self.ctr_win,self.ctr_loose)
        return
    def reset(self):
        self.ctr_draw,self.ctr_win,self.ctr_loose = 0,0,0
        self.draw.configure(self, text="Draws \n" + str(self.ctr_draw))
        self.wins.configure(self, text="Win \n" + str(self.ctr_win))
        self.loose.configure(self, text="Loose \n" + str(self.ctr_loose))
        return
if __name__ == "__main__":
    app = App()
    app.mainloop()
