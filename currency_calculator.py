import tkinter as tk
from tkinter import font
import requests
from string import ascii_letters

not_allowed_symbols = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+' ',', '-', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '\'']

url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json'
response = requests.get(url)

currencies = []
for currency in response.json().keys():
    currencies.append(currency)


def logic():
    from_currency_data = requests.get(f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency.get()}.json')
    initial_amount_data = initial_amount.get()
    if not initial_amount_data:
        error.config(text='ჩაწერე რაოდენობა!')
    elif from_currency.get() == to_currency.get():
        error.config(text='აირჩიე სხვადასხვა ვალუტა!')
    elif any(char.isalpha() or char in not_allowed_symbols for char in initial_amount_data):
        error.config(text='არასწორი ფორმატი!')
    else:
        error.config(text='')
        result = round(from_currency_data.json()[from_currency.get()][to_currency.get()]*float(initial_amount_data), 3)
        converted_amount.config(text=result)


def reset():
    converted_amount.config(text='')
    error.config(text='')
    initial_amount.delete(0, tk.END)
    from_currency.set('აირჩიე')
    to_currency.set('აირჩიე')


root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_offset = (screen_width // 2) - (420 // 2)
y_offset = (screen_height // 2) - (300 // 2)

root.title('ვალუტის კალკულატორი')
root.geometry(f'420x300+{x_offset}+{y_offset}')
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

initial_amount = tk.Entry(root)
initial_amount.grid(row=3, column=1)

converted_amount = tk.Label(root, font=font.Font(size=28))
converted_amount.grid(row=1, column=1)

error = tk.Label(root)
error.grid(row=7, column=1)

from_currency = tk.StringVar()
to_currency = tk.StringVar()
from_currency.set("აირჩიე")
to_currency.set('აირჩიე')

tk.Label(root, text='საიდან', font=font.Font(size=24)).grid(row=0)
tk.Label(root, text='სად', font=font.Font(size=24)).grid(row=0, column=2)
from_currency_drop = tk.OptionMenu(root, from_currency, *currencies)
from_currency_drop.config(width=7)
to_currency_drop = tk.OptionMenu(root, to_currency, *currencies)
to_currency_drop.config(width=7)
from_currency_drop.grid(row=1)
to_currency_drop.grid(row=1, column=2)

tk.Button(root, text='კონვერტაცია', command=logic).grid(row=5, column=1)
tk.Button(root, text='გასუფთავება', command=reset).grid(row=6, column=1)

root.mainloop()
