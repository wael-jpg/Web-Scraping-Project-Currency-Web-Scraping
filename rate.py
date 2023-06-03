import requests
from bs4 import BeautifulSoup
from tkinter import *
import requests
import pandas as pd

window = Tk()
window.title("Rate_Table")

convert = "USD"
to_convert = "EUR"
amount = 1

def list_of_curreny_names():
    currency_list_url = f"https://www.x-rates.com/table/?from={convert}&amount={1}"
    currency_list = requests.get(currency_list_url).text
    currency_list_page = BeautifulSoup(currency_list,"html.parser")

    currencies = currency_list_page.find_all(class_="currencyList ratestable")
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

def generate1(amount):
        result = am.get(1.0,"end")
        url = f"https://www.x-rates.com/table/?from={var1.get()[:3]}&amount={int(result)}"
        response = requests.get(url)
        html_content = response.content
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table on the page and extract the data
        table = soup.find("table", class_="tablesorter ratesTable")
        table_rows = table.find_all("tr")

        data = []
        for row in table_rows:
            cells = row.find_all("td")
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            if row_data:
                data.append(row_data)

        # Convert the data to a pandas DataFrame
        headers = ["Currency", "Rate", "Change"]
        df = pd.DataFrame(data, columns=headers)

        # Print the DataFrame
        print(df)

        # Save the DataFrame to an Excel file
        df.to_excel("Total_rates_table.xlsx", index=False)

        # Print a success message
        print("Rates table saved to rates_table.xlsx!")
        

def generate2(amount):
        result = am.get(1.0,"end")
        url = f"https://www.x-rates.com/table/?from={var1.get()[:3]}&amount={int(result)}"
        response = requests.get(url)
        html_content = response.content
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the table on the page and extract the data
        table = soup.find("table", class_="ratesTable")
        table_rows = table.find_all("tr")

        data = []
        for row in table_rows:
            cells = row.find_all("td")
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            if row_data:
                data.append(row_data)

        # Convert the data to a pandas DataFrame
        headers = ["Currency", "Rate", "Change"]
        df = pd.DataFrame(data, columns=headers)

        # Print the DataFrame
        print(df)

        # Save the DataFrame to an Excel file
        df.to_excel("Top10_rates_table.xlsx", index=False)

        # Print a success message
        print("Rates table saved to rates_table.xlsx!")


convert = Label(text="Convert",height=3,width=20)
convert.grid(row=0,column=0)

var1 = StringVar()
OptionMenu(window,var1,*short_name).grid(row=0,column=1)

am = Text(window,height=1,width=10)
am.grid(row=2,column=1)

Label(text="Amount").grid(row=2,column=0, pady=15)

b3 = Button(text="Generate All Table", command=lambda: generate1(2), height=1, width=20)
b3.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

b4 = Button(text="Generate Top 10", command=lambda: generate2(2), height=1, width=20)
b4.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

window.mainloop()