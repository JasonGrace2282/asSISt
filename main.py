import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()



        greeting = ctk.CTkLabel(self,text="Hello, Tkinter")
        greeting.pack()





        




def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()
