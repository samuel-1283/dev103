import tkinter as tk
from tkinter import messagebox


# Create main window
root = tk.Tk()
root.title("samtech")
root.geometry("800x600")
root.resizable(width=False, height=False)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)
root.mainloop()