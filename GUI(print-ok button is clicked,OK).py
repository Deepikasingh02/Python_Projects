
#   on clicking the button OK, print: "ok button is clicked"
import tkinter as tk

class ButtonEventHandler:
    def __init__(self):
        root = tk.Tk()
        self.b1=tk.Button(root, text="ok", command=self.functionOk)
        self.b1.pack()
        root.mainloop()

    def functionOk(self):
        print("ok button is clicked")
if __name__ =="__main__":
    ButtonEventHandler()

#                 OR

import tkinter as tk
def ok():
    print("ok button is clicked")
root =tk.Tk()
b1 = tk.Button(root, text ="ok",
          command = ok)
b1.pack()
root.mainloop()
