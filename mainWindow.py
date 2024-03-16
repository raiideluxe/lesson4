import tkinter as tk


class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)

        self.principal = tk.DoubleVar()
        self.rate = tk.DoubleVar()
        self.years = tk.IntVar()
        self.amount = tk.StringVar()

        principal_label = tk.Label(self, text="Principal $:", underline=0, anchor=tk.W)
        principal_label.grid(row=0, column=0)
        self.principal_scale = tk.Scale(self, from_=1000, to=10000, resolution=1, orient=tk.HORIZONTAL,
                                        variable=self.principal, command=self.updateUi)
        self.principal_scale.grid(row=0, column=1)

        rate_label = tk.Label(self, text="Rate:", underline=0, anchor=tk.W)
        rate_label.grid(row=1, column=0)
        self.rate_scale = tk.Scale(self, from_=0, to=100, resolution=0.01, orient=tk.HORIZONTAL, variable=self.rate,
                                   command=self.updateUi)
        self.rate_scale.grid(row=1, column=1)

        years_label = tk.Label(self, text="Years:", underline=0, anchor=tk.W)
        years_label.grid(row=2, column=0)
        self.years_scale = tk.Scale(self, from_=0, to=30, resolution=1, orient=tk.HORIZONTAL, variable=self.years,
                                    command=self.updateUi)
        self.years_scale.grid(row=2, column=1)

        self.actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)
        self.actualAmountLabel.grid(row=3, column=0, columnspan=2)

        self.updateUi()

    def updateUi(self, *ignore):
        principal = self.principal.get()
        rate = self.rate.get()
        years = self.years.get()

        amount = principal * (1 + rate / 100) ** years
        self.amount.set(f"{amount:.2f}")

    def quit(self, event=None):
        self.parent.destroy()
