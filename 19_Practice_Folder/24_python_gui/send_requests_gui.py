import tkinter as tk

master = tk.Tk()

tk.Radiobutton(master, text="POST").grid(row=0)
tk.Radiobutton(master, text="GET").grid(row=1)
tk.Radiobutton(master, text="OPTIONS").grid(row=2)
tk.Radiobutton(master, text="PATCH").grid(row=3)

#tk.Label(master, text="First Name").grid(row=0)
#tk.Label(master, text="Last Name").grid(row=1)

#e1 = tk.Entry(master)
#e2 = tk.Entry(master)


#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)


tk.Button(master,
          text='Submit',
          command=master.quit).grid(row=4,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)

master.mainloop()

