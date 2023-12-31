from tkinter import*
from PIL import Image,ImageTk
from record import Record
from hel import rec

window = Tk()
window.title(f"Live Security System")
window.iconphoto(False, PhotoImage(file = 'icon.png'))
window.geometry('1080x600')

#Main frame for video capture
vidBlock = Frame(window, bd = 2)
labelTitle = Label(vidBlock,text="Live Footage",font = ('Helvitica',40,'bold'))
labelTitle.grid(pady=(10,10),column=1)

IconOne = Image.open("24.png")
IconOne = IconOne.resize((70,70),Image.LANCZOS)
IconOne= ImageTk.PhotoImage(IconOne)
lableIconOne = Label(vidBlock,image= IconOne)
lableIconOne.grid(row=0,pady=(5,10),column=0)

IconSpy = Image.open("icon\spa.png")
IconSpy = IconSpy.resize((180,180),Image.LANCZOS)
IconSpy= ImageTk.PhotoImage(IconSpy)
lableIconspy = Label(vidBlock,image= IconSpy)
lableIconspy.grid(row=1,pady=(5,10),column=1)


buttonImage = Image.open("recording.png")
buttonImage = buttonImage.resize((50,50),Image.LANCZOS)
buttonImage= ImageTk.PhotoImage(buttonImage)

btn = Button(vidBlock,text="Record",font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=buttonImage,compound='left',command = rec) 
btn.grid(row=2,pady=(20,10),column=1)

exitBtn = Image.open("icon\exit.png")
exitBtn = exitBtn.resize((50,50),Image.LANCZOS)
exitBtn= ImageTk.PhotoImage(exitBtn)

btn_exit = Button(vidBlock,text="Exit",font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=exitBtn,compound='left',command = window.quit) 
btn_exit.grid(row=3,pady=(20,10),column=1)

vidBlock.pack() 

window.mainloop()