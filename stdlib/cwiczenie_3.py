import tkinter

def paliwko():
    try:
        cenaa = float(cena.get())
        dystanss = float(dystans.get())
        spalaniee = float(spalanie.get())
        licz = spalaniee*dystanss/100*cenaa
    except ValueError:
        licz = "Błąd!"
    return liczenie.configure(text=licz)


root = tkinter.Tk()
root.columnconfigure(1)
cena = tkinter.Entry(master=root)
cena.grid(row=0, column=1)
dystans = tkinter.Entry(master=root)
dystans.grid(row=1, column=1)
spalanie = tkinter.Entry(master=root)
spalanie.grid(row=2, column=1)
label1 = tkinter.Label(master=root, text="Cena [zł/l]: ")
label1.grid(row=0, column=0)
label2 = tkinter.Label(master=root, text="Dystans [km]: ")
label2.grid(row=1, column=0)
label3 = tkinter.Label(master=root, text="Spalanie [l/100km]: ")
label3.grid(row=2, column=0)
liczenie = tkinter.Label(master=root, text="<Wynik>")
liczenie.grid(row=3, column=1)
button = tkinter.Button(master=root, text="Licz!", command=paliwko)
button.grid(row=3, column=0)
root.mainloop()

