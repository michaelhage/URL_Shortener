# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:15:59 2020

@author: Michael Hage
"""

import tkinter as tk
import string
import random
import validators
import url_shortener as ush
import webbrowser as wb


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        
        master.title("my title")
        master.geometry('800x600')
        
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Make a shortend URL",
                  command=lambda: master.switch_frame(ShortURL)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class ShortURL(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        # master.title("my title")
        # master.geometry('800x600')
        
        
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        
        self.logo_lbl = tk.Label(self,
                    height=2,
                    text="URL Shortner").pack()
        
        self.url_lbl = tk.Label(self,
                   text="Input your URL").pack()

        self.url_ent = tk.Entry(self,
                   width=50)
        
        self.url_ent.pack()
        
        self.opt_lbl = tk.Label(self,
                   text="Input your Short id url. Leave blank if you want it randomized").pack()
        
        self.opt_url_ent = tk.Entry(self,
                   width=50)

        self.opt_url_ent.pack()

        tk.Button(self,
                height=1,
                width=10,
                text="Enter",
                command=lambda: self.url_check(
                self.url_ent.get(), self.opt_url_ent.get()
                )).pack()
        
        
        self.err_lbl = tk.Label(self,
                     text="")

        self.err_lbl.pack()
        
        
        tk.Button(self, text="Return to start page",

                  command=lambda: master.switch_frame(StartPage)).pack()
        
    def url_check(self, url, short_id):
        
        N = 6
        error = 0
        
        
        self.err_lbl.config(text="")
    
        if len(short_id) == 0:
            short_id = "".join( random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N) )
        
        # check if url provided is a valid url
        if len(url) == 0:
            self.err_lbl.config(text="URL input is empty\n")
        elif not(short_id.isalnum()):
            self.err_lbl.config(text="Optional ID should only be alpha numeric only\n")
        elif not(validators.url(url)):
            self.err_lbl.config(text="URL input is not a valid URL\n")
        else:
            error = ush.create_short_id(short_id, url)
        
        if error == 2:
            self.err_lbl.config(text=f"URL was added successfully, code is: {short_id}\n")
        elif error == 1:
            self.err_lbl.config(text="URL ID given is the same as one in the registry\n")
        elif error == 9:
            self.err_lbl.config(text="SOMETHING BAD HAS HAPPEND, AND I DONT KNOW WHAT\n")
            
        self.url_ent.delete(0, tk.END)
        self.opt_url_ent.delete(0, tk.END) 
        
class PageTwo(tk.Frame):
    def __init__(self, master):
        self.url = ""
        
        tk.Frame.__init__(self, master)
        tk.Label(self, text="URL Short ID entry").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Enter the URL Short ID").pack()
        
        self.short_id_ent = tk.Entry(self,
                   width=50)

        self.short_id_ent.pack()
        
        tk.Button(self, text="Enter URL ID",
                  command=lambda: self.get_url(self.short_id_ent.get())).pack()
        
        self.err_lbl = tk.Label(self,
                     text="")

        self.err_lbl.pack()
        
        
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()
        
    def get_url(self, short_id):
        error = 0
        
        self.err_lbl.config(text="")
        
        if not short_id:
            self.err_lbl.config(text="Short ID text box is empty")
        else:
            self.url = ush.retrieve_url(short_id)
        
            if not self.url:
                self.err_lbl.config(text="Invalid ID ")
            else:
                wb.open(self.url[0][0], new=2)
            
        self.short_id_ent.delete(0, tk.END)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()