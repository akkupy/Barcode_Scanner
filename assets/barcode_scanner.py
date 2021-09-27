import cv2
import csv
import sys
from tkinter import *
from pyzbar import pyzbar
from datetime import datetime as dt
from pynput.keyboard import Key, Controller





def row_append(barcode):
    now=dt.now()    
    with open('test.csv', 'a+', newline='') as fd:
        
        datenow= now.strftime("%d-%b-%y")
        timenow = now.strftime("%H:%M:%S")
        csvwriter=csv.writer(fd)   
        csvwriter.writerow([datenow, timenow, barcode])
        print(datenow,timenow,barcode)
   



def read_barcodes(frame,camera):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        barcode_text = barcode.data.decode('utf-8')
        user_choice(barcode_text,x,y,w,h,frame,camera)    
    return frame

def appender(barcode_text,x,y,w,h,window,frame,camera):
    row_append(barcode_text)
    cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2) 
    window.destroy()
    camera.release()
    cv2.destroyAllWindows()
    
    



def deny(window,camera):
    window.destroy()
    camera.release()
    cv2.destroyAllWindows()
    


def user_choice(barcode_text,x,y,w,h,frame,camera):
    window = Tk()
    window.title("Choice")
    window.geometry("400x150")
  
    var = "Is your number "+ barcode_text + "?"
    label = Label(window, text =  
        var, bg = "white", bd = 5, justify = RIGHT, padx = 70, pady = 30)    
    label.pack() 

    btn = Button(window, text = 'yes', bd = '5' ,command= lambda: appender(barcode_text,x,y,w,h,window,frame,camera))
 
    btn.pack(side = 'left')

    btn = Button(window, text = 'no', bd = '5' ,command= lambda:deny(window,camera))
 
    btn.pack(side = 'right')
  
    window.mainloop()


def main():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame,camera)
        cv2.imshow('Barcode reader', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()