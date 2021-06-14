import tkinter as tk
import random

root = tk.Tk()
root.geometry("400x400")
root.title('Roll Dice')

label = tk.Label(root,font=('Helvetica', 260 , 'bold') , text = '', fg ='green')


def rolldice():
    
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()


button = tk.Button(root, text='roll dice', foreground='green', command=rolldice , bg='lightblue' , fg='red')
button.pack()

root.mainloop()