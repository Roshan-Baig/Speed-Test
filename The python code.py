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
       w = Label(m, text = " "+a)
       w.config(text = "")
       w = Label(m, text = "Your download speed: "+a)
       w.place(x=0,y=100)
def printU():
        a = round(st.upload(),2)
        p()
        a = str(a)
        print(a)
        w = Label(m, text = " "+a)
        w.config(text = "")
        w = Label(m, text = "Your upload speed: "+a)
        w.place(x=200,y=100)
def printP():
        servernames = []
        p()
        st.get_servers(servernames)
        a = round(st.results.ping,2)
        a = str(a)
        print(a)
        w = Label(m, text = " "+a)
        w.config(text = "")
        w = Label(m, text = "Your ping speed: "+a)
        w.place(x=380,y=100)
def check():
        printP()
        printU()
        printD()
P.place(x = 40, y = 30)
style = Style()
style.theme_use('alt')
style.configure('TButton', background = 'Black', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('W.TButton', background=[('active', 'Black')])
v = Label(m, text = "Welcome to Speed Test! Press the respective button for the speed you want to test").place(x=40,y = 10)
b3 = Button(m, text = "Check Speed",style = 'W.TButton', width = 20, command = check).place(x=150,y=200)
m.mainloop()
