import customtkinter as ctk
from tkinter import Widget
from backend import login
from assignment import Assignment
from constants import DEFAULT_FONT


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("asSISt")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        self.window_title = ctk.CTkLabel(
            self,
            text="Calculate the impact of an new individual assginment on your\n\
                grade based on its weight and score".replace(
                    "               ",
                    ""
                ),
            font=DEFAULT_FONT
        )
        self.window_title.pack(pady=20)

        # bigheader = ctk.CTkLabel(
        #     self,
        #     text="Let's calculate your",
        #     font=("Oswald", 20),
        # )
        # bigheader.pack(
        #     side="left",  # packing
        #     anchor="nw",
        #     padx=30
        # )

        username, passwd, domain = self.auth()
        self.mainloop()
        username, passwd, domain = (
            x.get()
            for x in (username, passwd, domain)
        )
        # clean screen
        self.clear_screen([self.window_title])

        self.account = login(
            username,
            passwd,
            domain if domain else "sisstudent.fcps.edu/SVUE"
        )
        self.choose_classes()
        self.mainloop()
        self.assignment_gui()
        self.mainloop()

    def clear_screen(self, whitelist: list[Widget] = []):
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
        text_kwargs = {"font": DEFAULT_FONT} | text_kwargs

        if label:
            ctk.CTkLabel(self, text=text, **text_kwargs).pack(**kwargs)
        entry = ctk.CTkEntry(
            self,
            placeholder_text=placeholder_text,
            **text_kwargs
        )
        entry.get()
        entry.pack(**kwargs)
        return entry

    def auth(self):
        outputs = (
            self.get_entry(
                "Enter StudentVUE Information:",
                "Username",
                text_kwargs={"width": 500}
            ),
            self.get_entry(
                placeholder_text="Password",
                label=False,
                text_kwargs={"width": 500, "show": "*"}
            ),
            self.get_entry(
                placeholder_text="Domain (ex: sisstudent.fcps.edu/SVUE)",
                label=False,
                text_kwargs={"width": 500}
            )
        )
        ctk.CTkButton(
            self,
            text="Authenticate",
            command=self.quit
        ).pack(pady=20)
        return outputs

    def choose_classes(self) -> None:
        self.subject = self.account.subjects[0]
        for subject in self.account.subjects:
            def quit(sub=subject):
                self.subject = sub
                self.quit()

            name = subject.name
            ctk.CTkButton(
                self,
                text=name[:name.index("(")],
                command=quit,
                font=DEFAULT_FONT
            ).pack(pady=20)

    def assignment_gui(self) -> None:
        self.clear_screen()
        Assignment(self, self.subject)
        self.mainloop() 


def main():
    ctk.set_appearance_mode("dark")
    App()


if __name__ == "__main__":
    main()
