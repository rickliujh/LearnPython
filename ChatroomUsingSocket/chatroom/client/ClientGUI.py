from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import scrolledtext
import datetime

import socket
from threading import currentThread, Thread


class ChatroomClient(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.sock = None
        self.connectServer("127.0.0.1", 9999)

    def createWidgets(self):
        # self.messageLabel = Text(self)
        # self.messageLabel.pack()
        self.messageLabel = scrolledtext.ScrolledText(self)
        self.messageLabel.config(state=DISABLED)
        self.messageLabel.pack()
        self.Input = Entry(self)
        self.Input.bind("<Return>", self.sendMessage, True)
        # self.grid(row=0, column=0)
        self.Input.pack(side=LEFT,expand=YES,fill=X)
        self.alertButton = Button(self, text='send', command=self.sendMessage)
        # self.alertButton.grid(row=0, column=1)
        self.alertButton.pack()

    def connectServer(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, port)
        string = "connecting to %s:%s" % (server_address, port)
        self.sock.connect(server_address)
        self.writeLine(string)
        t = Thread(target=self.getMessage)
        t.setDaemon(True)
        t.start()

    def sendMessage(self, event=None):
        data = self.Input.get()
        if not data.strip():
            messagebox.showinfo(title='提示', message='不能发送空消息!')
            return
        string = '我: ' + data
        self.sock.sendall(data.encode('utf-8'))
        self.writeLine(string)
        self.Input.delete(0, END)

    def writeLine(self, data):
        nowTime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        string = nowTime + '\n'+data + '\n\n'
        self.messageLabel.config(state=NORMAL)
        self.messageLabel.insert('end', string)
        self.messageLabel.config(state=DISABLED)
        self.messageLabel.see(END)

    def getMessage(self):
        while True:
            data = bytes(self.sock.recv(1024)).decode('utf-8')
            # data = 'test'
            if not data.strip():
                continue
            self.writeLine(data)


app = ChatroomClient()
app.master.title("Chatroom")
app.master.geometry('500x420')
app.mainloop()
