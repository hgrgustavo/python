"""
add this to except somehow

    thinking if(!function()):
                messagebox.showerror()
"""

from tkinter import *



def infowindow(output: str) -> tkinter.messagebox.showinfo():
    window = Tk()

    if window:
        return tkinter.messagebox.showinfo(title="", message=output)

    window.mainloop()


def errorwindow(output: str) -> tkinter.messagebox.showerror():
    window = Tk()

    if window:
        return tkinter.messagebox.showerror(title="", message=output)

    window.mainloop()



"""
root = Tk()
display = App(root)
retVal = messagebox.showerror("Error", "Error pop-up")
"""