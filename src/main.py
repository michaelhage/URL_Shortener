# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:02:41 2020

@author: Michael Hage
"""

import tkinter as tk

    
def print_text(text):
    
    for t in text:
        print(t)
    # url_ent.delete(0,"end")

# initialize window properties
root = tk.Tk()
root.title("my title")
root.geometry('800x600')
# root.configure(background='black')

# Logo frame
logo_lbl = tk.Label(root,
                    height=2,
                    text="URL Shortner")

logo_lbl.pack(fill=tk.X)

# Input frame

# create frame to pack buttons and entries inside

url_lbl = tk.Label(root,
                   text="Input your Url")

url_lbl.pack()

url_ent = tk.Entry(root,
                   width=50)

url_ent.pack()

opt_url_ent = tk.Entry(root,
                   width=50)

opt_url_ent.pack()


url_btn = tk.Button(root,
                    height=1,
                    width=10,
                    text="Enter",
                    command=lambda:print_text(
                    [url_ent.get(), opt_url_ent.get()]
                    ))

url_btn.pack()

root.mainloop()