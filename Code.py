import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
ROOT.withdraw()
USER_INP = simpledialog.askstring(title="Name", prompt="What's your name?")
print("Hello", USER_INP)