import customtkinter as ctk
 


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Hello World")
        self.geometry("500x500")

        title1 = ctk.CTkLabel(self,text="Calculate the impact of an new individual assginment on your grade based on its weight and score")
        title2 = ctk.CTkLabel(self,text="Instructions: Pick whether to enter your grade as number of right points or as a percentage.")

        def choiceselected():
            print("button pressed")

        button = ctk.CTkButton(master=self, text="", command=choiceselected)
        button.pack(padx=20, pady=10)

        number = ctk.CTkLabel(self,text="Current grade value: 50%")

        def slider_event(value):
            value = round(value)
            percent = "Current grade value: " + str(value) + "%"
            number.configure(text=percent)
            



        number.pack()
        slider = ctk.CTkSlider(master=self, from_=0, to=100, command=slider_event)
        slider.place(relx=0.5, rely=0.2, anchor=ctk.N)
        
        





        


def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()
