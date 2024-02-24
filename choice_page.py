import customtkinter as ctk
 


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Assignment Impact Calculator") # Names file 
        self.geometry("640x500") #setup

        title1 = ctk.CTkLabel(self,text="Calculate the impact of an new individual assginment on your grade based on its weight and score")
        title2 = ctk.CTkLabel(self,text="Instructions: Pick whether to enter your grade as number of right points or as a percentage.")
        title1.pack()
        title2.pack()


        point_chosen = False # points btton variable
        percent_chosen = False #percent button variable 

        def points_selected():
            point_chosen = True
        pointsbutton = ctk.CTkButton(master=self, text="Click Here to Enter as Points!", command=points_selected)
        pointsbutton.place(x=100,y=130)

        def percent_selected():
            percent_chosen = True
        percentbutton = ctk.CTkButton(master=self, text="Click Here to Enter as Percent!", command=percent_selected,bd=3)
        percentbutton.place(x=375,y=130)






def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()
