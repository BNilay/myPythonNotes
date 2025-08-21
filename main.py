import tkinter

window = tkinter.Tk()
window.title("TK python")
window.minsize(width=800,height=800)

#label
label =  tkinter.Label(text="my label")
label.config(bg="light blue")
label.config(padx=10,pady=10)
label.pack()


#button
def button_clicked():
    print(text.get("1.0",tkinter.END))

button = tkinter.Button(text="button", command=button_clicked)
button.config(padx=10,pady=10)
button.pack()


#entry
entry = tkinter.Entry(width=20)
entry.pack()
entry.pack()


#text
text = tkinter.Text(width=30)
text.pack()
text.focus()


#scale
def scale_selected(value):
    print(value)
scale = tkinter.Scale(from_=0,to=50,command=scale_selected)
scale.pack()


#spinbox
def spinbox_selected():
    print(spinbox.get())
spinbox  = tkinter.Spinbox(from_=0,to=50,command=spinbox_selected)
spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())
check_state= tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
checkbutton.pack()


#radiobutton
def radio_selected():
    print(radio_checked_state.get())
radio_checked_state = tkinter.IntVar()
radio_button = tkinter.Radiobutton(text="1. option",value=10,variable=radio_checked_state,command=radio_selected)
radio_button2 = tkinter.Radiobutton(text="2. option",value=20,variable=radio_checked_state,command=radio_selected)
radio_button.pack()
radio_button2.pack()



#listbox
def listbox_selected(event):
    print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox()
name_list = ["A","B","C","D"]
for i in range(len(name_list)):
    listbox.insert(i,name_list[i])
listbox.bind('<<ListboxSelect>>',listbox_selected)
listbox.pack()










































window.mainloop()