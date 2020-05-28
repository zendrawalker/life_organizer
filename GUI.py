import tkinter as tk
from tkinter import filedialog, Text
import os, sys

screen = tk.Tk()
apps= []

def add_app():
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfile(initialdir='/', title='select file',
                                      filetypes=(("textfile", '*.rtf'), ("documents", "*.pdf")))
    apps.append(filename)
    print(filename)
    #we only want the name of the file
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def run_app():
    for app in apps:
        os.system(app)



canvas = tk.Canvas(screen, height=500, width=500)
canvas.pack()


frame = tk.Frame(screen, bg='lightblue')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

open_file = tk.Button(screen, text="Open File", padx=10, pady=5, fg='black', command=add_app)
run_apps = tk.Button(screen, text="run apps", padx=10, pady=10, fg='black', command = run_app)


run_apps.pack()
open_file.pack()


screen.mainloop()
