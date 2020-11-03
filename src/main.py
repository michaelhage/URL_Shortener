# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 19:02:41 2020

@author: Michael Hage
"""

import tkinter as tk
import url_shortener as ush
import string
import random
  
def print_text(text):
    
    for t in text:
        print(t)
    # url_ent.delete(0,"end")


def url_check(url, short_id):
    
    N = 6
    
    if len(short_id) == 0:
        short_id = "".join( random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N) )

    ush.create_short_id(short_id, url)
    
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
                   text="Input your URL")

url_lbl.pack()

url_ent = tk.Entry(root,
                   width=50)

url_ent.pack()

opt_lbl = tk.Label(root,
                   text="Input your Short id url. Leave blank if you want it randomized")

opt_lbl.pack()

opt_url_ent = tk.Entry(root,
                   width=50)

opt_url_ent.pack()


url_btn = tk.Button(root,
                    height=1,
                    width=10,
                    text="Enter",
                    command=lambda:url_check(
                    url_ent.get(), opt_url_ent.get()
                    ))

url_btn.pack()

root.mainloop()