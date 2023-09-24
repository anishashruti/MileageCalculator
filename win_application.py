import mileage_logic
import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.geometry("600x475")
root.configure(bg="#060D20")
root.title("Mileage calculator")

style = ttk.Style()
style.configure("Custom.TFrame", background="#060D20")
style.configure("Rounded.TEntry", borderwidth=5, relief="ridge", bordercolor="black", padding=(10, 10),background="#E7EA4B")
style.configure("Custom.TButton", borderwidth=5, relief="flat", bordercolor="black", padding=(10, 10),background="#E7EA4B")
style.configure("CustomR.TFrame", background="#E7EA4B")
font_style_title = ("Verdana", 20, "bold")
font_style_txt = ("Verdana", 14, "bold")


def on_entry_click_start(event):
    if textbox_start.get() == "km in Start of trip":
        textbox_start.delete(0, "end")
        textbox_start.config(foreground="black")


def on_entry_click_end(event):
    if textbox_end.get() == "km in End of trip":
        textbox_end.delete(0, "end")
        textbox_end.config(foreground="black")


def on_entry_click_fuel(event):
    if textbox_fuel.get() == "Fuel Consumption":
        textbox_fuel.delete(0, "end")
        textbox_fuel.config(foreground="black")

def calculate():
    print("Started calculation")
    fuel = float(textbox_fuel.get())
    end = int(textbox_end.get())
    start = int(textbox_start.get())
    try:
        if isinstance(fuel, float) and isinstance(end, int) and isinstance(start, int):
            mileage = str(round(float((end-start) / fuel),2))
            print(mileage)
            label_mileage.config(text=f" {mileage}")

    except ValueError:
        label_mileage.config(text=f"0")
        print(ValueError)



title_label = ttk.Label(root, text="Mileage Calculator", font=font_style_title, foreground="#E7EA4B",
                        background="#060D20")
title_label.pack(pady=25)

left_panel = ttk.Frame(root, style="Custom.TFrame")
left_panel.pack(side=tk.LEFT, padx=20)
right_panel = ttk.Frame(root, style="CustomR.TFrame")
right_panel.pack(side=tk.RIGHT, padx=30)

textbox_start = ttk.Entry(left_panel, font=font_style_txt, foreground="grey", style="Rounded.TEntry")
textbox_start.insert(0, "km in Start of trip")
textbox_start.bind('<FocusIn>', on_entry_click_start)
textbox_start.grid(row=0, column=1, padx=10, pady=10)

textbox_end = ttk.Entry(left_panel, font=font_style_txt, foreground="grey", style="Rounded.TEntry")
textbox_end.insert(0, "km in End of trip")
textbox_end.bind('<FocusIn>', on_entry_click_end)
textbox_end.grid(row=1, column=1, padx=10, pady=10)

textbox_fuel = ttk.Entry(left_panel, font=font_style_txt, foreground="grey", style="Rounded.TEntry")
textbox_fuel.insert(0, "Fuel Consumption")
textbox_fuel.bind('<FocusIn>', on_entry_click_fuel)
textbox_fuel.grid(row=2, column=1, padx=10, pady=10)

calculate_Btn =ttk.Button(left_panel,text="Go",command=calculate,style="Custom.TButton")
calculate_Btn.grid(row=3, column=1, padx=10, pady=10)

label_mileage = ttk.Label(right_panel, text="00.00", font=font_style_txt, foreground="black", background="#E7EA4B")
label_mileage.pack(padx=50, pady=50)

root.mainloop()
