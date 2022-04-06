from tkinter import *
import json, requests
from tkinter.messagebox import *

def convert():
    global url
    global curl
    global var1, var2

    if amount1.get().isdecimal() and amount1.get() != "":
        if var1.get() != "currency" and var2.get() != "currency":
            if var1.get() == var2.get():
                amount2.insert(0, str(amount1.get()))
            else:
                fromc = var1.get()
                toc = var2.get()
                key = "K3MQO5ISZGAYC6NI"
                url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
                curl = url + "&from_currency=" + fromc + "&to_currency=" + toc + "&apikey=" + key
                req_ob = requests.get(curl)
                result = req_ob.json()
                Exchange_Rate = float(result['Realtime Currency Exchange Rate']['5. Exchange Rate'])
                amount = float(amount1.get())
                new_amount = round(amount * Exchange_Rate, 3)
                amount2.delete(0, END)
                amount2.insert(0, str(new_amount))
        else:
            showerror("Error", "Please choose currencies")
    else:
        showerror("Error", "Please type a number")
def clear():
    amount1.delete(0, END)
    amount2.delete(0, END)
    var1.set("currency")
    var2.set("currency")
window = Tk()
var1 = StringVar(window)
var2 = StringVar(window)
var1.set("currency")
var2.set("currency")
if __name__ == "__main__":
    window.geometry("301x189")
    title = Label(window, text="RealTimeCurrency")
    label1 = Label(window, text="Amount: ")
    label2 = Label(window, text="From: ")
    label3 = Label(window, text="To: ")
    label4 = Label(window, text="Converted: ")
    window.title("RealTimeCurrency")
    title.grid(column=1, row=0)
    label1.grid(column=0, row=1)
    label2.grid(column=0, row=2)
    label3.grid(column=0, row=3)
    label4.grid(column=0, row=5)
    amount1 = Entry(window)
    amount2 = Entry(window)
    amount1.grid(row=1, column=1, ipadx="25")
    amount2.grid(row=5, column=1, ipadx="25")
    curcode = ("USD", "EUR", "ALL", "PKR", "TRY", "IQT", "INR")
    fromcur = OptionMenu(window, var1, *curcode)
    tocur = OptionMenu(window, var2, *curcode)
    fromcur.grid(column=1, row=2)
    tocur.grid(column=1, row=3)
    btn1 = Button(window, text="Convert", command=convert)
    btn2 = Button(window, text="Clear", command=clear)
    btn1.grid(row=4, column=1)
    btn2.grid(row=6, column=1)
    window.mainloop()