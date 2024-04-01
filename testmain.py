import tkinter as tk
from tkinter import ttk
import arrange_algo as arr
import pdf_gen

def arrange(selected_rooms, selected_sections):
    matrices=arr.arrange(arr.get_data(selected_sections), selected_rooms)
    print(matrices)
    print(f"Selected Rooms: {selected_rooms}")
    print(f"Selected Sections: {selected_sections}")
    print("Generating PDF...")
    print("PDF Generated Successfully!")

def submit():
    selected_rooms = [room_var.get() for room_var in room_vars if room_var.get()]
    selected_sections = [section_var.get() for section_var in section_vars if section_var.get()]
    arrange(selected_rooms, selected_sections)


root = tk.Tk()
root.title("EquiSeat")
root.geometry("300x300")
root.iconbitmap('logo.ico')


room_vars = []
section_vars = []


rooms_frame = ttk.LabelFrame(root, text="Rooms")
rooms_frame.pack(fill="both", expand=True)


rooms = ["IT-1", "IT-2", "IT-3", "IT-4"]
for room in rooms:
    var = tk.StringVar()
    chk = ttk.Checkbutton(rooms_frame, text=room, variable=var, onvalue=room, offvalue="")
    chk.pack(anchor='w')
    room_vars.append(var)


sections_frame = ttk.LabelFrame(root, text="Sections")
sections_frame.pack(fill="both", expand=True)

sections = ["IT-3A", "IT-3B"]
for section in sections:
    var = tk.StringVar()
    chk = ttk.Checkbutton(sections_frame, text=section, variable=var, onvalue=section, offvalue="")
    chk.pack(anchor='w')
    section_vars.append(var)


submit_btn = ttk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)


root.mainloop()