# Importing Module
from tkinter import *

# Window Properties
window = Tk()
window.geometry('400x450')
window.iconbitmap('Stopwatch_Icon.ico')
window.title('Stopwatch')
window.resizable(0,0)

counter = 0
running = False
def counter_label(label):
    def count():
        if running:
            global counter
            if counter==0:             
                display="0"
            else:
                display=str(counter)

            label['text']=display   
            
            label.after(1000, count)    
            counter += 1
            if counter<=10:
                label.place(x=180,y=170)
            elif counter>=11:
                label.place(x=160,y=170)
            elif counter>=101:
                label.place(x=140,y=170)
    count()     

def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=1
    if running==True:
        Stop()
        reset['state']='disabled'
        label['text']='00'
        label.place(x=180,y=170)
    if running==False:      
        reset['state']='disabled'
        label['text']='0'
        label.place(x=180,y=170)

bg = PhotoImage(file='Stopwatch_BG.png')
img = Label(window, image=bg, bg='#960096')
img.place(x=0,y=0)

label = Label(window,text="0",font=("Source Sans Pro",60,"bold"),fg="black",bg='#960096')
label.place(x=180,y=170)

labelmsg = Label(window,text="Seconds",font=("Source Sans Pro",16),fg="black",bg='#960096')
labelmsg.place(x=162,y=250)

start = Button(window,font="bold",text='Start',width=8,height=1,command=lambda:Start(label),bg="dark cyan")
stop = Button(window,font="bold",text='Stop',width=8,state='disabled',command=Stop,bg="dark cyan")
reset = Button(window,font="bold",text='Reset',width=8,state='disabled',command=lambda:Reset(label),bg="dark cyan")

start.place(x=30, y=390)
stop.place(x=150, y=390)
reset.place(x=270, y=390)

window.mainloop()