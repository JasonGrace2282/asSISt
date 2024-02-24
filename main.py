import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()


        usernamehead = ctk.CTkLabel(self,Text="Enter User name here")
        username = ctk.CTkEntry(self, width=300)
        usernamehead.pack()
        username.pack()










def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()
