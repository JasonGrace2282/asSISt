import customtkinter as ctk
from tkinter import Widget
from backend import login


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("StudentVUE Grade Helpers")
        self.geometry("500x500")

        label = ctk.CTkLabel(
            self,
            text="Calculate the impact of an new individual assginment on your\
                grade based on its weight and score".replace(
                    "               ",
                    ""
                )
        )
        label.pack(pady=20)

        username, passwd, domain = self.auth()
        self.mainloop()
        # clean screen
        self.clear_screen([label])
        

        self.account = login(
            username.get(),
            passwd.get(),
            domain.get() if domain.get() else "sisstudent.fcps.edu/SVUE"
        )
        self.choose_classes()
        self.mainloop()

    def clear_screen(self, whitelist: list[Widget]):
        for widget in self.winfo_children():
            if widget not in whitelist:
                widget.destroy()


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
                "Enter StudenVUE Information:",
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

    def choose_classes(self) -> None:
        for subject in self.account.subjects:
            ctk.CTkButton(self, text=subject.name, command=self.quit).pack(pady=20)


def main():
    ctk.set_appearance_mode("dark")
    App()


if __name__ == "__main__":
    main()
