#!/usr/bin/python3
import os
import webbrowser
import socket
try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    os.system("python -m pip install tk-tools")
link = []
class ipfounder(object):
    def __init__(self):
        super(ipfounder,self).__init__()
        self.root = Tk()
        self.root.title("Ip Founder")
        photo = PhotoImage(file = 'ipfounder_logo.png')
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='developer',command=self.developer)
        menu.add_cascade(label='Dev',menu=filemenu)
        userrecon_label = Label(self.root,text='Ip Founder',foreground='green',background='black',font=("None"))
        userrecon_label.pack()
        userrecon_label.place(x=100,y=10)

        global host,scan
        host = Entry(self.root,width=15)
        host.pack()
        host.place(x=100,y=50)
        host.insert(0,"Host")

        scan = Button(self.root,text='Scan',command=self.scan_ip,width=9,height=3,foreground='green',background='black')
        scan.pack()
        scan.place(x=110,y=80)

        exit = Button(self.root,text='Exit',command=self.ext,width=9,height=3,foreground='green',background='black')
        exit.pack()
        exit.place(x=110,y=140)
        self.root.iconphoto(False,photo)
        # self.root.iconbitmap(default=photo)
        self.root.geometry("300x300")
        self.root.resizable(0,0)
        self.root.configure(background='black')
        self.root.mainloop()

    def scan_ip(self):
        ip = socket.gethostbyname(host.get())
        messagebox.showinfo('Ip',f'Ip: {ip}')
        scan.configure(text='Try')
    def ext(self):
        self.root.destroy()
        exit()

    def developer(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')

    @staticmethod
    def title():
        if os.name == 'nt':
          os.system("title Ip Founder")
        else:
            os.system("printf '\033]2;Ip Founder\a'")


if __name__ == '__main__':
    ipfounder.title()
    window = ipfounder()