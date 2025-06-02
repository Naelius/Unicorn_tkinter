import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()

# Bild zuerst laden
image = Image.open("wood-background.jpg").resize((600, 400))
photo = ImageTk.PhotoImage(image)

image2 = Image.open("dragon.jpg").resize((600, 400))
photo2 = ImageTk.PhotoImage(image2)

# Dann das Label mit dem Bild erstellen
label1 = ttk.Label(root, image=photo, text="Roar! I'm a mighty Dragon!", compound="top")
label1.pack(side="top", fill="x")

# Überschreibt das Bild von image
label1["image"] = photo2

root.mainloop()

print("Testausgabe")
