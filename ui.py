import customtkinter as ctk


def auth(root: ctk.CTk):
    usernamehead = ctk.CTkLabel(root, text="Enter username here:")
    username = ctk.CTkEntry(root, width=300)
    usernamehead.pack()
    username.pack()

    passwordhead = ctk.CTkLabel(root, text="Enter password here:")
    password = ctk.CTkEntry(root, width=300, show="*")
    passwordhead.pack()
    password.pack()

    authenticate_button = ctk.CTkButton(root, text="Authenticate")
    authenticate_button.pack()

