import customtkinter as ctk
 


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Hello World")
        self.geometry("500x500")

        


        number = ctk.CTkLabel(self,text="100")

        def slider_event(value):
            value = round(value)
            percent = "Current grade value: " + str(value) + "%"
            number.configure(text=percent)
            



        number.pack()
        slider = ctk.CTkSlider(master=self, from_=0, to=100, command=slider_event)
        slider.place(relx=0.5, rely=0.5, anchor=ctk.N)
        
        








def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()
