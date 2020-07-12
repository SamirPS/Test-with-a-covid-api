#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: samir
"""
from tkinter import (
    Tk,
    Label,
    Listbox,
)

import requests
import tkinter.scrolledtext as tkscrolled



class CovidTest:
    def __init__(self):

        # Initialise l'application change le titre et la positionne
        self.root = Tk()
        self.root.title("Covid")

       

        self.root.resizable(False, False)
        self.entry_country = tkscrolled.ScrolledText(self.root, width=60, height=10,)

        
    
        self.country = Listbox(
            self.root, selectmode="single", exportselection=0, width=20, height=10
        )
        Label(self.root, text="Country").grid(row=0, column=6)

       
        self.country.grid(row=2, column=6, rowspan=10, padx=10)

        for country in [i["country"] for i in requests.get("https://corona.lmao.ninja/v2/countries?yesterday=false&sort=").json()]:
            self.country.insert("end", country)

        
        
        
        self.entry_country.grid(row=2, column=20, rowspan=10)

        self.country.bind("<<ListboxSelect>>", self.display)
        

        
        self.root.mainloop()

    def display(self,*inutile):
        r=requests.get("https://corona.lmao.ninja/v2/countries?yesterday=false&sort=")
        country=[i["country"] for i in r.json()]
        try :
            country=self.country.get(self.country.curselection()[0])
        except:
            country="None"
        

        

        self.entry_country.configure(state="normal")
        self.entry_country.delete(0.7, "end")

        for i in r.json():
            if i["country"]==country:
                self.entry_country.insert(0.7,f"""Here the number of case :{i["cases"]} case,{i["deaths"]} death,{i["recovered"]} recovered 
                                       \nToday we have : {i["todayCases"]} case,{i["todayDeaths"]} deaths,{i["todayRecovered"]} recovered""")
                break

       

        self.entry_country.configure(state="disabled")


if __name__ == "__main__":
    CovidTest()
