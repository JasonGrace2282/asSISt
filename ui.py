import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        usernamehead = ctk.CTkLabel(self,text="Enter username here:")
        username = ctk.CTkEntry(self, width=300)
        usernamehead.pack()
        username.pack()

        passwordhead = ctk.CTkLabel(self,text="Enter password here:")
        password = ctk.CTkEntry(self, width=300, show="*")
        passwordhead.pack()
        password.pack()
        
        authenticate_button = ctk.CTkButton(self, text="Authenticate")
        authenticate_button.pack()


def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()

