from tkinter import *
from tkinter.ttk import *
import speedtest
m = Tk()
m.geometry("500x250")
st = speedtest.Speedtest()
P = Progressbar(m, orient = HORIZONTAL, length = 200, mode = 'determinate')
def p():
        import time
        P['value'] = 20
        m.update_idletasks()
        time.sleep(1)

        P['value'] = 40
        m.update_idletasks()
        time.sleep(1)

        P['value'] = 50
        m.update_idletasks
        time.sleep(1)

        P['value'] = 60
        m.update_idletasks
        time.sleep(1)

        P['value'] = 80
        m.update_idletasks
        time.sleep(1)

        P['value'] = 100
        m.update_idletasks
        time.sleep(1)
def printD():
       a = round(st.download(),2)
       p()
       a = str(a)
       print(a)
       w = Label(m, text = "Your download speed: "+a)
       w.place(x=75,y=100)
def printU():
        a = round(st.upload(),2)
        p()
        a = str(a)
        print(a)
        w = Label(m, text = "Your upload speed: "+a)
        w.place(x=75,y=100)
def printP():
        servernames = []
        p()
        st.get_servers(servernames)
        a = round(st.results.ping,2)
        a = str(a)
        print(a)
        w = Label(m, text = "Your ping speed: "+a)
        w.place(x=75,y=100)
P.place(x = 40, y = 30)
style = Style()
style.configure('W.TButton',font = ('calibri',10),foreground = 'blue')
w = Label(m, text = "Welcome to Speed Test! Press the respective button for the speed you want to test").place(x=40,y = 10)
b1 = Button(m, text = "Download Speed",style = 'W.TButton', width = 20, command = printD).place(x=30,y=200)
b2 = Button(m, text = "Upload Speed",style = 'W.TButton', width = 20, command = printU).place(x=170,y=200)
b3 = Button(m, text = "Ping Speed",style = 'W.TButton', width = 20, command = printP).place(x=310,y=200)
m.mainloop()
