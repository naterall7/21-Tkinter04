import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 20 and
#   paste it below.
#
#   Now, create a function called print_form() that gets all the values entered
#   in your form and prints them on their own line.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("Form")
window.columnconfigure(0, weight=1, minsize=60)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1, minsize=60)
frame_name = tk.Frame(master=window, bg="#000000")
frame_name.grid(row=0, column=0, sticky="nesw")
label_name = tk.Label(master=frame_name, text = "Name", background = "#000000", foreground = "#64e8c9")
label_name.pack()
entry_name = tk.Entry(master=frame_name, background = "#000000", foreground = "#64e8c9")
entry_name.pack(fill=tk.BOTH)
frame_address1 = tk.Frame(master=window, bg="#000000")
frame_address1.grid(row=1, column=0, sticky="nesw")
label_address1 = tk.Label(master=frame_address1, text = "Address Line 1", background = "#000000", foreground = "#64e8c9")
label_address1.pack()
entry_address1 = tk.Entry(master=frame_address1, background = "#000000", foreground = "#64e8c9")
entry_address1.pack(fill=tk.BOTH)
frame_address2 = tk.Frame(master=window, bg="#000000")
frame_address2.grid(row=2, column=0, sticky="nesw")
label_address2 = tk.Label(master=frame_address2, text = "Address Line 2", background = "#000000", foreground = "#64e8c9")
label_address2.pack()
entry_address2 = tk.Entry(master=frame_address2, background = "#000000", foreground = "#64e8c9")
entry_address2.pack(fill=tk.BOTH)
frame_city = tk.Frame(master=window, bg="#000000")
frame_city.grid(row=3, column=0, sticky="nesw")
label_city = tk.Label(master=frame_city, text = "City", background = "#000000", foreground = "#64e8c9")
label_city.pack()
entry_city = tk.Entry(master=frame_city, background = "#000000", foreground = "#64e8c9")
entry_city.pack(fill=tk.BOTH)
frame_state = tk.Frame(master=window, bg="#000000")
frame_state.grid(row=4, column=0, sticky="nesw")
label_state = tk.Label(master=frame_state, text = "State", background = "#000000", foreground = "#64e8c9")
label_state.pack()
entry_state = tk.Entry(master=frame_state, background = "#000000", foreground = "#64e8c9")
entry_state.pack(fill=tk.BOTH)
frame_zip = tk.Frame(master=window, bg="#000000")
frame_zip.grid(row=5, column=0, sticky="nesw")
label_zip = tk.Label(master=frame_zip, text = "Zip Code", background = "#000000", foreground = "#64e8c9")
label_zip.pack()
entry_zip = tk.Entry(master=frame_zip, background = "#000000", foreground = "#64e8c9")
entry_zip.pack(fill=tk.BOTH)
frame_phone = tk.Frame(master=window, bg="#000000")
frame_phone.grid(row=6, column=0, sticky="nesw")
label_phone = tk.Label(master=frame_phone, text = "Phone Number", background = "#000000", foreground = "#64e8c9")
label_phone.pack()
entry_phone = tk.Entry(master=frame_phone, background = "#000000", foreground = "#64e8c9")
entry_phone.pack(fill=tk.BOTH)
frame_email = tk.Frame(master=window, bg="#000000")
frame_email.grid(row=7, column=0, sticky="nesw")
label_email = tk.Label(master=frame_email, text = "Email Address", background = "#000000", foreground = "#64e8c9")
label_email.pack()
entry_email = tk.Entry(master=frame_email, background = "#000000", foreground = "#64e8c9")
entry_email.pack(fill=tk.BOTH)
frame_button = tk.Frame(master=window, bg="#000000")
frame_button.grid(row=8, column=0, sticky="nesw")
def print_form():
    print(entry_name.get())
    print(entry_address1.get())
    print(entry_address2.get())
    print(entry_city.get())
    print(entry_state.get())
    print(entry_zip.get())
    print(entry_phone.get())
    print(entry_email.get())
button = tk.Button(master=frame_button, text = "Submit", background = "#000000", foreground = "#64e8c9", command=print_form)
button.pack()
window.mainloop()

###############################################################################
# DONE: 2. (1 pt)
#
#   Now, use the command keyword to connect your "Submit" button to your
#   print_form() function.
#
#   Now, when you run your program, you should be able to type information into
#   the form and click "Submit", and it will print all the information that you
#   entered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
