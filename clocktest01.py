

# Digital Clock GUI @tapgo416

#importing libraries 

from tkinter import Label, Tk
import time

# defining the size of the application window

app_window = Tk()
app_window.title("Clock @tapgo416")
app_window.geometry("386x164")
app_window.resizable(0,0)

# defining the look / font, and colors

text_font= ("Boulder", 68, 'bold')
background = "#000000"
foreground= "white"
border_width = 41

# combine elements to define label # Label is used to specify the container box where we can place the text or images.

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# define the main function # set the text of the label as the real time

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()