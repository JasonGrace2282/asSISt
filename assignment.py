import customtkinter as ctk
from backend.classes import Subject


class Assignment(ctk.CTkScrollableFrame):
    def __init__(self, root: ctk.CTk, subject: Subject) -> None:
        super().__init__(
            root,
            width=root.winfo_width(),
            height=root.winfo_height()-100
        )
        self.subject = subject
        self.pack(pady=20)
        self._get_base_stats()

    def _get_base_stats(self) -> None:
        def get_val(n: float) -> float | int:
            return round(n) if n.is_integer() else n

        for col, weight in enumerate(self.subject.weights, start=1):
            kwargs = {"column": col, "padx": 20, "pady": 20}
            ctk.CTkLabel(
                self,
                text=weight.name
            ).grid(row=1, **kwargs)
            ctk.CTkLabel(
                self,
                text=f"{get_val(weight.points)} / {get_val(weight.points_possible)}"
            ).grid(row=2, **kwargs)
