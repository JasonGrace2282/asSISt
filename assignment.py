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

        self.rows = []
        self.pluses = []
        self.simulations = []

        self.subject = subject
        self.pack(pady=20)
        self._get_base_stats()

        for i in range(len(subject.weights)):
            self.rows.append(2)
            self.pluses.append(None)
            self.simulations.append(None)
            self.add_button(i)

    def _get_base_stats(self) -> None:
        def get_val(n: float) -> float | int:
            return round(n) if n.is_integer() else n

        self.kwargs = {"padx": 20, "pady": 20}
        title_font = (None, 30)
        for col, weight in enumerate(self.subject.weights, start=1):
            kwargs = {"column": col} | self.kwargs
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
            **self.kwargs
        )
        self.final_grade = ctk.CTkLabel(
            self,
            text=f"{calc_final_grade(self.subject, *self.simulations)*100:.1f}%"
        )
        self.final_grade.grid(
            row=2,
            column=len(self.subject.weights)+2,
            **self.kwargs
        )

    def add_button(self, col: int) -> None:
        self.pluses[col] = ctk.CTkButton(
            self,
            text="+",
            font=(None, 30),
            command=lambda c=col: self.expand(c)
        )
        self.rows[col] += 1
        self.pluses[col].grid(row=self.rows[col], column=col+1)

    def expand(self, col: int) -> None:
        self.pluses[col].destroy()
        self.simulations[col] = ctk.CTkEntry(self, placeholder_text="points / total")
        self.simulations[col].grid(
            column=col+1,
            rows=self.rows[col],
            **self.kwargs
        )
        self.add_button(col)
