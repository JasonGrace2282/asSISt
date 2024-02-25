import customtkinter as ctk
from backend.classes import Subject
from backend.calc import calc_final_grade


class Assignment(ctk.CTkScrollableFrame):
    def __init__(self, root: ctk.CTk, subject: Subject) -> None:
        super().__init__(
            root,
            width=root.winfo_width(),
            height=root.winfo_height()
        )
        self.subject = subject
        self.simulations = ()
        self.pack(pady=20)
        self._get_base_stats()
        self.row = 3

    def _get_base_stats(self) -> None:
        def get_val(n: float) -> float | int:
            return round(n) if n.is_integer() else n

        base = {"padx": 20, "pady": 20}
        title_font = (None, 30)
        for col, weight in enumerate(self.subject.weights, start=1):
            kwargs = {"column": col} | base
            ctk.CTkLabel(
                self,
                text=weight.name,
                font=title_font
            ).grid(row=1, **kwargs)
            ctk.CTkLabel(
                self,
                text=f"{get_val(weight.points)} / {get_val(weight.points_possible)}"
            ).grid(row=2, **kwargs)

        ctk.CTkLabel(self, text="Final Grade", font=title_font).grid(
            row=1,
            column=len(self.subject.weights)+2,
            **base
        )
        ctk.CTkLabel(self, text=f"{calc_final_grade(self.subject, *self.simulations)*100}%").grid(
            row=2,
            column=len(self.subject.weights)+2,
            **base
        )

    def add_button(self) -> None:
        plus = ctk.CTkButton(
            self,
            text="+",
            font=(None, 50),
            command=self.expand
        )
        plus.grid()

    def expand(self) -> None:
        pass
