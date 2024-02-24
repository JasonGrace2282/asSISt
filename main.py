import customtkinter as ctk
from backend import login


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Hello World")
        self.geometry("500x500")

        ctk.CTkLabel(
            self,
            text="Calculate the impact of an new individual assginment on your\
                grade based on its weight and score".replace(
                    "               ",
                    ""
                )
        ).pack(pady=20)

        username, passwd, domain = self. ()
        self.mainloop()
        while not username.get() or not passwd.get() or not domain.get():
            username, passwd, domain = self.auth()
            self.mainloop()
        account = login(username.get(), passwd.get(), domain.get())
        print(account)

    def get_entry(
        self,
        text: str = "",
        placeholder_text: str = "",
        label: bool = True,
        text_kwargs: dict = {},
        **kwargs
    ) -> ctk.CTkEntry:
        kwargs = {"pady": 20} | kwargs
        if label:
            ctk.CTkLabel(self, text=text, **text_kwargs).pack(**kwargs)
        entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder_text,
            **text_kwargs
        )
        entry.pack(**kwargs)
        return entry

    def auth(self):
        outputs = (
            self.get_entry(
                "Enter StudentVUE Information:",
                "Username",
                text_kwargs={"width": 300}
            ),
            self.get_entry(
                placeholder_text="Password",
                label=False,
                text_kwargs={"width": 300, "show": "*"}
            ),
            self.get_entry(
                placeholder_text="Domain (ex: sisstudent.fcps.edu/SVUE)",
                label=False,
                text_kwargs={"width": 300}
            )
        )
        ctk.CTkButton(
            self,
            text="Authenticate",
            command=self.quit
        ).pack(pady=20)

        return outputs


def main():
    ctk.set_appearance_mode("dark")
    App()


if __name__ == "__main__":
    main()
