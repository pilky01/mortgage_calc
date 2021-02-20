#!/usr/bin/env python3

import tkinter as tk

import mortgage_gui as gui

def main():
    root = tk.Tk()
    mainApplication = gui.Application(root)
    mainApplication.pack()

    root.title('Mortgage Calculator')
#    root.geometry("800x300")
    root.mainloop()

if __name__ == "__main__":
    main()
