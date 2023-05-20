from tkinter import *
from tkinter import messagebox
import base64
import os
import winsound
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def encrypt():

    password=code.get()
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        winsound.Beep(2000, 1000)
        messagebox.showerror("ENCRYPTION","Enter The Secret Key")
    elif password!="1234":
        winsound.Beep(2000, 1000)
        messagebox.showerror("ENCRYPTION","Invalid Secret Key")

def decrypt():
    password=code.get()
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)

    elif password=="":
        winsound.Beep(2000, 1000)
        messagebox.showerror("ENCRYPTION","Enter The Secret Key")
    elif password!="1234":
        winsound.Beep(2000, 1000)
        messagebox.showerror("ENCRYPTION","Invalid Secret Key")

def main_screen():

    global screen
    global code
    global text1
     
    screen = Tk()
    screen.geometry("375x398")
    screen.iconbitmap("./assets/ico.ico")
    screen.title("TEXT ENCRYPTION APP")

    def reset():
        code.set("")
        text1.delete(1.0,END)
   
    Label(text="Enter The Text For Encryption And Decryption",fg="black",font=("Comic Sans MS",12)).place(x=10,y=10)
    text1 = Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
   
    Label(text="Enter Secret Key For Encryption And Decryption",fg="black",font=("Comic Sans MS",11)).place(x=10,y=170)
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
    
    #buttons
    Button(text="ENCRYPT",height="2",width="23",bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width="50",bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)

    screen.mainloop()

main_screen()
