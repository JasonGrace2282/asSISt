import customtkinter as ctk 
from PIL import Image


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.geometry("500x500")
        
        plus_state = True
        while plus_state == True:
            name_header = ctk.CTkLabel(master=self,
                                    text="Assignment Name",
                                    justify="center",
                                    text_color="white",
                                    font=("Comic Sans",25))
            name_header.pack()
            name_entry = ctk.CTkEntry(master=self,
                                    placeholder_text="Assignment Name",
                                    placeholder_text_color = "grey",
                                    width = 300,
                                    justify="center")
                                    
            name_entry.pack()
            
            #points
            points_header = ctk.CTkLabel(master=self,
                                    text="Points Correct",
                                    justify="left",
                                    text_color="white",
                                    font=("Comic Sans",18),
                                    padx=0.7)
            points_header.pack()
            points_entry = ctk.CTkEntry(master=self,
                                    placeholder_text="Points Correct",
                                    placeholder_text_color = "grey",
                                    width = 200,
                                    justify="center")
            points_entry.pack()



            #POINTS POSSIBLE
            pointspossiblehead = ctk.CTkLabel(master=self,
                                    text="Total Points",
                                    justify="left",
                                    text_color="white",
                                    font=("Comic Sans",18),
                                    padx=0.7)
            pointspossiblehead.pack()
            pointspossibleentry = ctk.CTkEntry(master=self,
                                    placeholder_text="Total Points",
                                    placeholder_text_color = "grey",
                                    width = 200,
                                    justify="center")
            pointspossibleentry.pack()

            #Weight 
            weight_header = ctk.CTkLabel(master=self,
                                    text="Weighting Category",
                                    justify="left",
                                    text_color="white",
                                    font=("Comic Sans",18),
                                    padx=0.7)
            weight_header.pack()
            weight_entry = ctk.CTkEntry(master=self,
                                    placeholder_text="Category Name",
                                    placeholder_text_color = "grey",
                                    width = 200,
                                    justify="center")
            weight_entry.pack()

            number = ctk.CTkLabel(self,
                                text="Current grade value: 50%",
                                font=("Arial",18))
            def slider_event(value):
                value = round(value)
                percent = "Current grade value: " + str(value) + "%"
                number.configure(text=percent)
                    
            number.pack()
            #Grade Slider
            slider = ctk.CTkSlider(master=self, 
                                from_=0, to=100, 
                                command=slider_event,
                                fg_color = "black",
                                width=250,
                                height=30)

            slider.place(relx=0.5, rely=0.51, anchor=ctk.N)

            plus_state = False
            def plus():
                plus_state = True
        
            plus_button = ctk.CTkButton(master=self, 
                                        text="+",
                                        font=("Arial",50),
                                        fg_color="black",
                                        hover_color="grey",
                                        height=80,
                                        width=80,
                                        command=plus)
            plus_button.pack(pady=50)

            #Needs .get() 












        self.mainloop()

        



def main():
    ctk.set_appearance_mode("dark")
    App()


if __name__ == "__main__":
    main()
