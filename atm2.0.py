# Two pins pin no.s "4598" and "7865"

from tkinter import*
from PIL import ImageTk, Image
import PIL.Image
from tkinter import *
import sqlite3
con=sqlite3.connect("king1.db") 
k=20000
pin="4598"
cpin="7865"
b=0
d=0
f=""
r3=0
t3=0
stn=""
Actype=""
last_depo=""
nme=""
h6=""
st=""
ws=Tk()
c=StringVar()
upin=StringVar()
# functions
def show(n):
    global f
    f=f+n
    upin.set(f)
def clr():
    global f
    f=""  
    upin.set("")
def singleclr():
    ws.destroy()

def enter():
    if pin==f:
        w.destroy()
        rat()
    elif cpin==f:
        w.destroy()
        bat()
    else:
        h1.after(1000,h1.destroy())
        l1=Label(w,text="***INVALID PIN NO.***\n""----try again-------",bg="#50A8B0",fg="white",font=("arial",12,""),width=30)
        l1.place(x=230,y=20)
        w.update()
ws.title("ATM")
ws.geometry("830x500")
ws.resizable(10,10)
ws.config(bg="grey")
w=Frame(ws,width=800,height=500,bg="light blue")
w.pack()
h0=Label(w,text="City Bank",bg="#50A8B0",fg="white",font=("arial",16,""))
h0.place(x=0,y=0)
h1=Label(w,text="Welcome to the ATM",bg="#50A8B0",fg="white",font=("arial",16,""))
h1.place(x=260,y=20)
h2=Label(w,text="Please enter your ATM Pin",bg="#50A8B0",fg="white",font=("arial",16,""))
h2.place(x=230,y=70)
e=Entry(w,text=upin,width=40,font=50,justify=LEFT).place(x=185,y=110)

image=PIL.Image.open("at.png")
photo=ImageTk.PhotoImage(image)
resized_image= image.resize((350,250))
new_image= ImageTk.PhotoImage(resized_image)
l=Label(w,image=new_image)
l.place(x=180,y=150)
image1=PIL.Image.open("at1.png")
photo=ImageTk.PhotoImage(image1)
resized_image1= image1.resize((60,40))
new_image1= ImageTk.PhotoImage(resized_image1)
bt1=Button(w,image=new_image1,command=lambda: show("1"))
bt1.place(x=208,y=178)
image2=PIL.Image.open("at2.png")
photo=ImageTk.PhotoImage(image2)
resized_image2= image2.resize((60,40))
new_image2= ImageTk.PhotoImage(resized_image2)
bt2=Button(w,image=new_image2,command=lambda: show("2"))
bt2.place(x=278,y=178)
image3=PIL.Image.open("at3.png")
photo=ImageTk.PhotoImage(image3)
resized_image3= image3.resize((60,40))
new_image3= ImageTk.PhotoImage(resized_image3)
bt3=Button(w,image=new_image3,command=lambda: show("3"))
bt3.place(x=348,y=178)
image4=PIL.Image.open("at4.png")
photo=ImageTk.PhotoImage(image4)
resized_image4= image4.resize((60,40))
new_image4= ImageTk.PhotoImage(resized_image4)
bt4=Button(w,image=new_image4,command=lambda: show("4"))
bt4.place(x=208,y=230)
image5=PIL.Image.open("at5.png")
photo=ImageTk.PhotoImage(image5)
resized_image5= image5.resize((60,40))
new_image5= ImageTk.PhotoImage(resized_image5)
bt5=Button(w,image=new_image5,command=lambda: show("5"))
bt5.place(x=278,y=230)
image6=PIL.Image.open("at6.png")
photo=ImageTk.PhotoImage(image6)
resized_image6= image6.resize((60,40))
new_image6= ImageTk.PhotoImage(resized_image6)
bt6=Button(w,image=new_image6,command=lambda: show("6"))
bt6.place(x=348,y=230)
image7=PIL.Image.open("at7.png")
photo=ImageTk.PhotoImage(image7)
resized_image7= image7.resize((60,40))
new_image7= ImageTk.PhotoImage(resized_image7)
bt7=Button(w,image=new_image7,command=lambda: show("7"))
bt7.place(x=208,y=282)
image8=PIL.Image.open("at8.png")
photo=ImageTk.PhotoImage(image8)
resized_image8= image8.resize((60,40))
new_image8= ImageTk.PhotoImage(resized_image8)
bt8=Button(w,image=new_image8,command=lambda: show("8"))
bt8.place(x=278,y=282)
image9=PIL.Image.open("at9.png")
photo=ImageTk.PhotoImage(image9)
resized_image9= image9.resize((60,40))
new_image9= ImageTk.PhotoImage(resized_image9)
bt9=Button(w,image=new_image9,command=lambda: show("9"))
bt9.place(x=348,y=282)
image0=PIL.Image.open("at0.png")
photo=ImageTk.PhotoImage(image0)
resized_image0= image0.resize((60,40))
new_image0= ImageTk.PhotoImage(resized_image0)
bt0=Button(w,image=new_image0,command=lambda: show("0"))
bt0.place(x=278,y=335)
imagecan=PIL.Image.open("atcan.png")
photo=ImageTk.PhotoImage(imagecan)
resized_imagecan= imagecan.resize((65,45))
new_imagecan= ImageTk.PhotoImage(resized_imagecan)
btc=Button(w,image=new_imagecan,command=singleclr)
btc.place(x=438,y=176)
imageclr=PIL.Image.open("atclr.png")
photo=ImageTk.PhotoImage(imageclr)
resized_imageclr= imageclr.resize((65,45))
new_imageclr= ImageTk.PhotoImage(resized_imageclr)
btcl=Button(w,image=new_imageclr,command=clr)
btcl.place(x=438,y=228)
imageent=PIL.Image.open("atent.png")
photo=ImageTk.PhotoImage(imageent)
resized_imageent= imageent.resize((65,45))
new_imageent= ImageTk.PhotoImage(resized_imageent)
bt=Button(w,image=new_imageent,command=enter)
bt.place(x=438,y=280)
def rat():
    global Actype,accno,bal,withdraw,deposit,nme
    bq=con.execute("SELECT Name from atm where AccountNo=10")
    for row in bq:
        nme=(row[0])
        print(nme)
    b8=con.execute("SELECT Acctype from atm where AccountNo=10")
    for row in b8:
        Actype=(row[0])
        print(Actype)
    m0=con.execute("select AccountNo from atm where AccountNo=10")
    for row in m0:
        st=(row[0])
    accno=int(st)
    print(accno)
    m=con.execute("SELECT Bal from atm where AccountNo=10")
    for row in m:
        stn=(row[0])
    bal=int(stn)
    print(bal)
    m=con.execute("SELECT lastwith from atm where AccountNo=10")
    for row in m:
        stn1=(row[0])
    withdraw=int(stn1)
    print(withdraw)
    b8=con.execute("SELECT lastdepo from atm where AccountNo=10")
    for row in b8:
        last_depo=(row[0])
    deposit=int(last_depo)
    print(deposit)
    # con.close()
    f2=Frame(ws,height=100,width=150,bg="blue",highlightbackground="red",bd=5)
    f2.pack()
    l=Label(f2,text="City Bank",bg="blue",fg="white",font=("arial",40,"bold"),width=15)
    l.pack()
    bt=Button(ws,text="Cash Withdrawal",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: sh())
    bt.place(x=0,y=250)
    bt=Button(ws,text="Check Balance",bg="#88cffa",font=("arial",14,""),width=15,command=chkbal)
    bt.place(x=656,y=200)
    bt=Button(ws,text="  Cash Deposit ",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: sh1())
    bt.place(x=656,y=150)
    bt=Button(ws,text="   Fast Cash     ",bg="#88cffa",font=("arial",14,""),width=15,command=fast)
    bt.place(x=0,y=150)
    bt=Button(ws,text="  Mini Statement  ",bg="#88cffa",font=("arial",14,""),width=15,command=ministate)
    bt.place(x=0,y=200)
    bt=Button(ws,text="   Back   ",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: back())
    bt.place(x=656,y=250)
    bt=Button(ws,text="   Exit   ",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: ws.destroy())
    bt.place(x=656,y=300)
    bt=Button(ws,text="Account info",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: sh3())
    bt.place(x=0,y=300)

def bat():
    global Actype,accno,bal,withdraw,deposit,nme
    bw=con.execute("SELECT Name from atm where AccountNo=28")
    for row in bw:
        nme=(row[0])
        print(nme)
    b8=con.execute("SELECT Acctype from atm where AccountNo=28")
    for row in b8:
        Actype=(row[0])
        print(Actype)
    m0=con.execute("select AccountNo from atm where AccountNo=28")
    for row in m0:
        st=(row[0])
    accno=int(st)
    print(accno)
    m=con.execute("SELECT Bal from atm where AccountNo=28")
    for row in m:
        stn=(row[0])
    bal=int(stn)
    print(bal)
    m=con.execute("SELECT lastwith from atm where AccountNo=28")
    for row in m:
        stn1=(row[0])
    withdraw=int(stn1)
    print(withdraw)
    b8=con.execute("SELECT lastdepo from atm where AccountNo=28")
    for row in b8:
        last_depo=(row[0])
    deposit=int(last_depo)
    print(deposit)
    # con.close()
    f2=Frame(ws,height=100,width=150,bg="blue",highlightbackground="red",bd=5)
    f2.pack()
    l=Label(f2,text="City Bank",bg="blue",fg="white",font=("arial",40,"bold"),width=15)
    l.pack()
    bt=Button(ws,text="Cash Withdrawal",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: sh())
    bt.place(x=0,y=250)
    bt=Button(ws,text="Check Balance",bg="#88cffa",font=("arial",14,""),width=15,command=chkbal)
    bt.place(x=656,y=200)
    bt=Button(ws,text="  Cash Deposit ",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: sh1())
    bt.place(x=656,y=150)
    bt=Button(ws,text="   Fast Cash     ",bg="#88cffa",font=("arial",14,""),width=15,command=fast)
    bt.place(x=0,y=150)
    bt=Button(ws,text="  Mini Statement  ",bg="#88cffa",font=("arial",14,""),width=15,command=ministate)
    bt.place(x=0,y=200)
    bt=Button(ws,text="   Back   ",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: back())
    bt.place(x=656,y=250)
    bt=Button(ws,text="   Exit   ",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: ws.destroy())
    bt.place(x=656,y=300)
    bt=Button(ws,text="Account info",bg="#88cffa",font=("arial",14,""),width=15,command=lambda: sh3())
    bt.place(x=0,y=300)
def calw():
    try:
        global bal
        global r3
        e=c.get()
        r3=int(e)
        if bal>=r3:
            if pin==f:
                con.execute("update atm set Bal=Bal-? where AccountNo=10",[c.get()])
                con.execute("update atm set lastwith=? where AccountNo=10",[r3])
                con.commit()
            elif cpin==f:
                con.execute("update atm set Bal=Bal-? where AccountNo=28",[c.get()])
                con.execute("update atm set lastwith=? where AccountNo=28",[r3])
                con.commit()
            cls()
            bal=bal-r3
            x5=Label(ws,text="Your money is successfully Withdraw",bg="#88cffa",font=("arial",14,""))
            x5.place(x=260,y=328)
            x5.after(1000, lambda :x5.destroy())
            w.after(1000, lambda :w.destroy())
        else:
            x5=Label(ws,text="***Insufficent Balance***",bg="#88cffa",font=("arial",14,""))
            x5.place(x=310,y=280)
            x5.after(1000, lambda :x5.destroy())
    except ValueError :
        # ws.destroy()
        print("fhfhj")
        pass
def cald():
    global t3,bal
    t2=d.get()
    t3=int(t2)
    try:
        if pin==f:
            con.execute("update atm set Bal=bal+? where AccountNo=10",[d.get()])
            con.execute("update atm set lastdepo=? where AccountNo=10",[d.get()])
            con.commit()
        elif cpin==f:
            con.execute("update atm set Bal=bal+? where AccountNo=28",[d.get()])
            con.execute("update atm set lastdepo=? where AccountNo=28",[d.get()])
            con.commit()
        cls()
        bal=bal+t3
        x4=Label(ws,text="Your money is successfully deposited",bg="#88cffa",font=("arial",14,""))
        x4.place(x=260,y=328)
        x4.after(1000, lambda :x4.destroy())
        w.after(1000, lambda :w.destroy())
    except ValueError :
        # ws.destroy()
        pass
def fast():
    global r3,bal
    r3=1000
    if bal>=r3:
        if pin==f:
            con.execute("update atm set Bal=Bal-? where AccountNo=10",[r3])
            con.execute("update atm set lastwith=? where AccountNo=10",[r3])
            con.commit()
            bal=bal-r3
        elif cpin==f:
            con.execute("update atm set Bal=Bal-? where AccountNo=28",[r3])
            con.execute("update atm set lastwith=? where AccountNo=28",[r3])
            con.commit()
            bal=bal-r3
        cls()
        x5=Label(ws,text="Your money is successfully Withdraw",bg="#88cffa",font=("arial",14,""))
        x5.place(x=260,y=200)
        x5.after(1000, lambda :x5.destroy())
    else:
        x5=Label(ws,text="***Insufficent Balance***",bg="#88cffa",font=("arial",14,""))
        x5.place(x=310,y=280)
        x5.after(1000, lambda :x5.destroy())
def chkbal():
    x2=Label(ws,text=f"Your balance is {bal}",bg="#88cffa",font=("arial",14,""))
    x2.place(x=316,y=200)
    x2.after(2000, lambda :x2.destroy())
def ministate():
    if t3 and r3!=0:
        x3=Label(ws,text=f"Your balance is {bal}\n Last deposit is {t3}\n Last withdrawal is {r3} ",bg="#88cffa",font=("arial",14,""))
        x3.place(x=316,y=200)
        x3.after(2000, lambda :x3.destroy())
    elif t3!=0 and r3==0:
        x3=Label(ws,text=f"Your balance is {bal}\n Last deposit is {t3}\n Last withdrawal is {withdraw} ",bg="#88cffa",font=("arial",14,""))
        x3.place(x=316,y=200)
        x3.after(2000, lambda :x3.destroy())
    elif t3==0 and r3!=0:
        x3=Label(ws,text=f"Your balance is {bal}\n Last deposit is {deposit}\n Last withdrawal is {r3} ",bg="#88cffa",font=("arial",14,""))
        x3.place(x=316,y=200)
        x3.after(2000, lambda :x3.destroy())
    else:
        x3=Label(ws,text=f"Your balance is {bal}\n Last deposit is {deposit}\n Last withdrawal is {withdraw} ",bg="#88cffa",font=("arial",14,""))
        x3.place(x=316,y=200)
        x3.after(2000, lambda :x3.destroy())
def cls():
    c1=con.execute("SELECT Bal from atm")
    for row in c1:
        print("BAL=",row[0])
def sh():
    global c,w
    global x2
    w=Frame(ws,width=415,height=250,bg="grey")
    w.pack()
    c=Entry(w,font=80)
    c.pack(padx=100,pady=140)
    btc=Label(w,text="Enter the Amount ",bg="#88cffa",font=("arial",14,""))
    btc.place(x=115,y=70)
    x2=Button(w,text="Submit",bg="#88cffa",font=("arial",12,""),command=lambda: calw())
    x2.place(x=155,y=200)
def sh1():
    global d,w
    global x0,btp
    w=Frame(ws,width=415,height=250,bg="grey")
    w.pack()
    d=Entry(w,font=80)
    d.pack(padx=100,pady=140)
    btp=Label(w,text="Enter the Amount ",bg="#88cffa",font=("arial",14,""))
    btp.place(x=115,y=70)
    x0=Button(w,text="Submit",bg="#88cffa",font=("arial",12,""),command=lambda: cald())
    x0.place(x=155,y=200)
    # x2.after(1000, lambda :x2.destroy())
def sh3():
    xn=Label(ws,text=f"Name = {nme}\n Account type is {Actype}\n Account no. = {accno}",bg="#88cffa",font=("arial",16,""))
    xn.place(x=316,y=200)
    xn.after(2000, lambda :xn.destroy())
def back():
    w.after(100, lambda :w.destroy())
ws.mainloop()


