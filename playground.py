# # # import tkinter as tk
# # # # from tkinter import ttk
# # # import ttkbootstrap as ttk
# # #
# # # def on_click():
# # #     # get and set the content of entry
# # #     entry_data = entry.get()
# # #     print(entry_data)
# # #     data_output.set(entry_data)
# # #
# # #     # update label
# # #     label.configure(text=entry_data)
# # #     # label["text"] = "Label was changed again"
# # #     # print(label.configure()) # information
# # #
# # #     entry.configure(state="disable")
# # #
# # # def reset():
# # #     entry.configure(state="enable")
# # #     label.configure(text="some text")
# # #     data_output.set("")
# # #
# # # # window
# # # app = ttk.Window(themename="darkly")
# # # app.title("widgets")
# # # app.geometry("300x200")
# # #
# # # # variables
# # # data_output = tk.StringVar()
# # #
# # # # label
# # # label = ttk.Label(master=app, text="Label")
# # # label.pack()
# # # # label.config(text="New text")
# # # # label["text"] = "Another new"
# # #
# # # # entry
# # # entry = ttk.Entry(master=app)
# # # entry.pack(pady=5)
# # #
# # # frame = ttk.Frame(master=app)
# # # frame.pack(pady=5)
# # #
# # # # button
# # # button = ttk.Button(master=frame, text="submit", command= on_click)
# # # button.pack(side="left", padx=5, pady=5)
# # #
# # # button_2 = ttk.Button(master=frame, text="reset", command= reset)
# # # button_2.pack(side="left")
# # #
# # # # output label
# # # label_2 = ttk.Label(master=app, textvariable=data_output)
# # # label_2.pack()
# # #
# # # # runner
# # # app.mainloop()
# # #
# #
# # import tkinter as tk
# # from tkinter import ttk
# #
# # def on_click():
# #     data_input.set("updated")
# #
# # # window
# # app = tk.Tk()
# # app.title("mimic")
# # app.geometry("300x200")
# #
# # data_input = tk.StringVar(value= "test")
# # # data_input.set("text ")
# #
# # # label
# # label = ttk.Label(master=app, text= "some text", textvariable=data_input)
# # label.pack()
# #
# # # entry
# # entry = ttk.Entry(master=app, textvariable=data_input)
# # entry.pack(pady=5)
# #
# # entry_2 = ttk.Entry(master=app, textvariable=data_input)
# # entry_2.pack(pady=5)
# #
# # # button
# # button = ttk.Button(master=app, text="button", command= on_click)
# # button.pack(pady=5)
# #
# # label_2 = ttk.Label(master=app, textvariable= data_input)
# #
# # # exercise
# # # create 2 entry filed and 1 label, they should be connected via stringvar
# # # set a strat value of 'test'
# #
# # # runner
# # app.mainloop()
# # #
# # 1:06:20
# #
# # import tkinter as tk
# # from tkinter import ttk
# #
# # # setup
# # app = tk.Tk()
# # app.title("Buttons")
# # app.geometry("600x400")
# #
# # # button
# # def button_func():
# #     print("a button was pressed")
# #     print(radio_var.get())
# #
# # button_string = tk.StringVar(value="button")
# # button = ttk.Button(
# #     master=app,
# #     text="button",
# #     textvariable=button_string,
# #     command= button_func
# # )
# # button.pack()
# #
# # # check button
# # check_var = tk.IntVar(value=10)
# # check1 = ttk.Checkbutton(
# #     master=app,
# #     text = "checkbox 1",
# #     variable=check_var,
# #     command= lambda: print(check_var.get()),
# #     onvalue=10,
# #     offvalue=5
# # )
# # check1.pack()
# #
# # check2 = ttk.Checkbutton(
# #     master=app,
# #     text= "checkbox 2",
# #     command = lambda: check_var.set(5)
# # )
# # check2.pack()
# #
# # # radio button
# # radio_var = tk.StringVar()
# # radio1 = ttk.Radiobutton(
# #     master=app, text= "Radiobutton 1",
# #     value="radio 1",
# #     variable=radio_var,
# #     command= lambda: print(radio_var.get())
# # )
# # radio1.pack()
# # radio2 = ttk.Radiobutton(
# #     master=app, text= "Radiobutton 2",
# #     value= 4,
# #     variable=radio_var,
# #     command= lambda: print(radio_var.get())
# # )
# # radio2.pack()
# #
# # # run
# # app.mainloop()
# import tkinter as tk
# from tkinter import ttk
#
# # window
# app = tk.Tk()
# app.title("1:25:42")
# app.geometry("400x400")
#
# def radio_func():
#     print(exersice_var.get())
#     exersice_var.set(False)
#
# exersice_var = tk.BooleanVar()
# radio_var = tk.StringVar()
#
# radio1 = ttk.Radiobutton(
#     master=app,
#     text="Radiobutton 1",
#     value = "A",
#     variable= radio_var,
#     command= radio_func
# )
# radio2 = ttk.Radiobutton(
#     master=app,
#     text="Radiobutton 2",
#     value= "B",
#     variable= radio_var,
#     command= radio_func
# )
# radio1.pack()
# radio2.pack()
#
# checkbox = ttk.Checkbutton(
#     master=app,
#     text="Checkbox",
#     variable= exersice_var,
#     command= lambda: print(radio_var.get()),
#     onvalue= True,
#     offvalue= False
# )
# checkbox.pack()
#
#
# # run
# app.mainloop()
# 1:41:30
