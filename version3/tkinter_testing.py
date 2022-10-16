'''
A testing file for tkinter
'''

import tkinter as tk



rootwindow =  tk.Tk()

frm_mainframe = tk.Frame(master=rootwindow, bg="blue")
frm_mainframe.grid(row=1, column=1)

lbl_text = tk.Label(master=frm_mainframe, text="text", width=10, height=2)
lbl_text.grid(row=1, column=1)
lbl_text = tk.Label(master=frm_mainframe, text="text", width=10, height=2)
lbl_text.grid(row=1, column=2)
lbl_text = tk.Label(master=frm_mainframe, text="text", width=10, height=2)
lbl_text.grid(row=1, column=3)
rootwindow.mainloop()
