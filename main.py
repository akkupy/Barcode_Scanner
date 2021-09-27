from tkinter import *
from assets import *
  
window = Tk()
window.title("BarCode Scanner")
window.geometry("400x150")
  
var = "BARCODE ID SCANNER"  
label = Label(window, text =  
    var, bg = "white", bd = 5, justify = RIGHT, padx = 70, pady = 30)    
label.pack() 

btn = Button(window, text = 'Scan!', bd = '5' ,command= main)
 
btn.pack(side = 'top')
  
window.mainloop()