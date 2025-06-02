import tkinter as tk
from tkinter import ttk

root = tk.Tk()



label1 = tk.Label(root, text="Hier könnte dein Titel stehen!", bg="pink")
label1.pack(side="top", fill="x")

label2 = tk.Label(root, text="Aha, du liest das hier also?", bg="orange")
label2.pack(side="bottom", fill="both", expand=True)

label3 = ttk.Label(root, text="Das hier ist ein TTK-Label")
label3.pack()

root.geometry("400x400")
root.minsize(width=200, height=200)
root.maxsize(width=600, height=600)
root.resizable(width=False, height=True)



root.mainloop()


print("Testausgabe")