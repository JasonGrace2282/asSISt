import customtkinter as ctk
from backend.classes import Subject, SimulatedAssignment
from backend.calc import calc_final_grade, finals_grade_recalc
from constants import DEFAULT_FONT


class Assignment(ctk.CTkScrollableFrame):
    def __init__(self, root: ctk.CTk, subject: Subject) -> None:
        super().__init__(
            root,
            width=root.winfo_width(),
            height=root.winfo_height()
        )

        def resize(event, root=root):
            self.configure(
                width=root.winfo_width(),
                height=root.winfo_height()
            )

        root.bind("<Configure>", resize)

        self.sims = []

        self.subject = subject
        self.pack(pady=20)
        self._get_base_stats()

        for col, sub in enumerate(self.subject.weights, start=1):
            for row in range(3, 6):
                self.sims.append(SimulatedAssignment(
                    ctk.CTkEntry(
                        self,
                        placeholder_text="grade / total"
                    ),
                    name=sub.name
                ))
                self.sims[-1].expr.grid(row=row, column=col, **self.kwargs)
        ctk.CTkButton(
            self,
            text="Recalculate",
            command=self.update_grade
        ).grid(
            row=3,
            column=len(self.subject.weights)+3,
            **self.kwargs
        )

        def back():
            root.quit()
            root.clear_screen()  # type: ignore
            root.choose_classes()  # type: ignore
            root.mainloop()
            root.clear_screen()  # type: ignore
            root.assignment_gui()  # type: ignore

        ctk.CTkButton(
            self,
            text="Back",
            command=back
        ).grid(
            row=4,
            column=len(self.subject.weights)+3,
            **self.kwargs
        )

    def update_grade(self) -> None:
        fg = calc_final_grade(self.subject, *self.sims)
        if (
            self.weighting.get().isnumeric()
            and self.final_exam_points.get().isnumeric()
        ):
            w = int(self.weighting.get())/100
            print(w, self.final_exam_points.get())
            fg = finals_grade_recalc(
                fg,
                int(self.final_exam_points.get())/100,
                (1-w, w)
            )
        self.final_grade.configure(
            text=f"{fg*100:.1f}%",
            require_redraw=True
        )

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
                text=f"{get_val(weight.points)} / {get_val(weight.points_possible)}",
                font=DEFAULT_FONT
            ).grid(row=2, **kwargs)

        # final stuff
        ctk.CTkLabel(
            self,
            text="Final Exam",
            font=title_font
        ).grid(
            row=1,
            column=len(self.subject.weights)+2,
            **self.kwargs
        )

        self.weighting = ctk.CTkEntry(
            self,
            placeholder_text="Weightage of your grade (e.g. 20)",
        )
        self.weighting.grid(
            row=2,
            column=len(self.subject.weights)+2,
            **self.kwargs
        )

        self.final_exam_points = ctk.CTkEntry(
            self,
            placeholder_text="Estimated percent score (ex: 67)"
        )
        self.final_exam_points.grid(
            row=3,
            column=len(self.subject.weights)+2,
            **self.kwargs
        )

        ctk.CTkLabel(self, text="Final Grade", font=title_font).grid(
            row=1,
            column=len(self.subject.weights)+3,
            **self.kwargs
        )

        self.final_grade = ctk.CTkLabel(
            self,
            text=f"{calc_final_grade(self.subject, *self.sims)*100:.1f}%",
            font=DEFAULT_FONT
        )
        self.final_grade.grid(
            row=2,
            column=len(self.subject.weights)+3,
            **self.kwargs
        )
