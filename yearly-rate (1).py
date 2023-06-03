import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pandas as pd


window = Tk()
window.title("Monthly Average")

convert = "USD"
to_convert = "EUR"
amount = 1

def list_of_curreny_names():
    currency_list_url = f"https://www.x-rates.com/average/?from={convert}&to={to_convert}&amount={1}&year=2023"
    currency_list = requests.get(currency_list_url).text
    currency_list_page = BeautifulSoup(currency_list,"html.parser")

    currencies = currency_list_page.find_all(class_="currencyList monthlyaverage")
    short_name = []
    currency_name = ""

    for currency in currencies:
        currency_name += currency.text
        curreny_symbols= currency.find_all('a')
        for symbol in curreny_symbols:
            symbol_text = symbol.get("href")
            short_name.append(symbol_text.split("=")[1])
    currency_name_list = currency_name.split("\n")

    full_list = []
    for i, x in zip(short_name, currency_name_list):
        full_list.append(f"{i} - {x}")

    return full_list

short_name = list_of_curreny_names()
short_name.sort()



def generate(amount,n):
    result = am.get(1.0,"end")
    url = f"https://www.x-rates.com/average/?from={var1.get()[:3]}&to={var2.get()[:3]}&amount={int(result)}&year=2020"
    response = requests.get(url)
    html_content = response.content
        
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
        
    # Find the unordered list on the page and extract the data
    ul = soup.find('ul', {'class': 'OutputLinksAvg'})
    lis = ul.find_all('li')

    # Create a string variable to store the data
    output_text = "Month - Average Rate - N° of days \n"
    for li in lis:
        output_text += li.text.strip() + "\n"

    # Show the data in a message box
    messagebox.showinfo(f"Monthly Average of {var1.get()[:3]}/{var2.get()[:3]}", output_text)


        
convert = Label(text="Convert",height=3,width=20)
convert.grid(row=0,column=0)
var1 = StringVar()
OptionMenu(window,var1,*short_name).grid(row=0,column=1)
to_convert = Label(text="Convert to",height=3,width=20).grid(row=1,column=0)
var2 = StringVar()
OptionMenu(window,var2,*short_name).grid(row=1,column=1)
am = Text(window,height=1,width=10)
am.grid(row=2,column=1)
Label(text="Amount").grid(row=2,column=0, pady=15)
Label(text="Year").grid(row=3, column=0, pady=15)
n_entry = Entry(window)
n_entry.grid(row=3, column=1)
b3 = Button(text="Generate", command=lambda: generate(2,2), height=1, width=20)
b3.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

window.mainloop()