import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()


        username = ctk.CTkEntry(self, width=300)
        username.pack()










def main():
    ctk.set_appearance_mode("dark")
    App().mainloop()


if __name__ == "__main__":
    main()
