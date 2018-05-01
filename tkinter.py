import tkinter as tk

counter = 0 
def counter_label(label):
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
  
  
root = tk.Tk()
root.title("This is my first application.")

label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()

explanation = """At present, only GIF and PPM/PGM formats are supported, but an interface exists to allow additional image file
formats to be added easily."""

whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"

msg = tk.Message(root, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

w2 = tk.Label(root, 
              justify=tk.LEFT,
		 fg = "red",
                 bg = "dark green",		 
		 font = "Times",
              padx = 10, 
              text=explanation).pack(side="left")
root.mainloop()
