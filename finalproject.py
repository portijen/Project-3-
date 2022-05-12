from tkinter import * 
import pandas as pd 


df =pd.read_excel('/Users/jenniferportillo/Desktop/python/com_serv.xlsx')

window = Tk()

window.title("Community Service Finder")

window.geometry('400x250')

window.configure(bg='pink')

promt = Label(window, text="Select a community service option: ")

promt.grid(column=0, row=0)

#creating selection box

choices = ("Food Drive", "Clothes drive", "Blood drive", "Clean up")

choicesvar = StringVar(value=choices)

l = Listbox(window, height = 4, listvariable = choicesvar)

l.grid(column=0, row=1)


#selection

def selected_item(): 

    for i in l.curselection():
        serv_type = (l.get(i))
        print(df.loc[df['Type'] == serv_type])



pd.set_option('display.max_columns', None)

btn = Button(window, text='Print Selected', command=selected_item)

btn.grid(row=2)
l.grid()

window.mainloop()