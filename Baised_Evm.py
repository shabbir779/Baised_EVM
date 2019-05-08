from tkinter import *
from tkinter import messagebox

c=0
b=0
o=0
flag=0

tk=Tk()
tk.title("EVM Demo")
tk.geometry("500x500")
header=Label(tk,text='EVM Demo',font=('Times new Roman',20,'bold italic underline'))
header.pack()

def vvpat():
    tk.withdraw()
    top=Toplevel()
    top.title('VVPAT DEMO')
    top.geometry('500x500')
    header=Label(top,text='VVPAT Demo',font=('Times new Roman',20,'bold italic underline'))
    header.pack()
    
    def clear(x):
        global flag,c,b,o
        if(x==1):
            top.destroy()
            tk.deiconify()
        elif(x==0):
            flag = 0
            textbox.delete(0.0,END)
            btnBJP.config(bg='green')
            btnCongress.config(bg='green')
            btnNOTA.config(bg='green')
            messagebox.showinfo('Ballot Issued!','Ballot Issued\nYou can Vote Now.')
        else:
            c=0
            b=0
            o=0
            messagebox.showinfo('Machine Cleared','Machine Cleared!\nAll previous data removed.')
    
    def addVote(x):
        global c,b,o,flag
        if(not flag):
            flag=1
            if(x==1):
                btnCongress.config(bg='red')
                if((c+b+o)<5):
                    c+=1
                else:
                    b+=1
                print('CONGRESS = ',c,'\tTOTAL = ',c+b+o)
                ticket='TICKET GENERATED!\nTicket Number = ',c+b+o,'\nYou voted for Congress!'
                textbox.insert(END,ticket)
                messagebox.showinfo('SUCCESS','You voted for CONGRESS!')
            elif(x==3):
                btnNOTA.config(bg='red')
                if((c+b+o)<5):
                    o+=1
                else:
                    b+=1
                print('OTHER = ',o,'\tTOTAL = ',c+b+o)
                ticket='TICKET GENERATED!\nTicket Number = ',c+b+o,'\nYou voted for Other/NOTA!'
                textbox.insert(END,ticket)
                messagebox.showinfo('SUCCESS','You voted for Other/NOTA!')
            else:
                btnBJP.config(bg='red')
                b+=1
                print('BJP = ',b,'\tTOTAL = ',c+b+o)
                ticket='TICKET GENERATED!\nTicket Number = ',c+b+o,'\nYou voted for BJP!'
                textbox.insert(END,ticket)
                messagebox.showinfo('SUCCESS','You voted for BJP!')
        else:
            messagebox.showerror('Machine LOCKED!','Machine Locked!\nPress BALLOT before Next Vote.\nThank You!')
            
    lblCongress=Label(top,text='Congress',font=('Arial', 14))
    lblCongress.place(x=100,y=60)
    btnCongress=Button(top,text='          ',font=('Arial',14),bg='green',command= lambda :addVote(1))
    btnCongress.place(x=300,y=50)
    
    lblBJP=Label(top,text='BJP',font=('Arial', 14))
    lblBJP.place(x=100,y=110)
    btnBJP=Button(top,text='          ',font=('Arial',14),bg='green',command= lambda :addVote(2))
    btnBJP.place(x=300,y=100)
    
    lblNOTA=Label(top,text='OTHER / NOTA',font=('Arial', 14))
    lblNOTA.place(x=100,y=160)
    btnNOTA=Button(top,text='          ',font=('Arial',14),bg='green',command= lambda :addVote(3))
    btnNOTA.place(x=300,y=150)
    
    textbox=Text(top,height=5,width=33)
    textbox.place(x=100,y=210)
    
    btnClear=Button(top,text='CLEAR',font=('Arial',14),command=lambda :clear(2))
    btnClear.place(x=50,y=300)
    
    btnClear=Button(top,text='BALLOT',font=('Arial',14),command=lambda :clear(0))
    btnClear.place(x=170,y=300)
    btnClose=Button(top,text='CLOSE',font=('Arial',14),command=lambda :clear(1))
    btnClose.place(x=300,y=300)
    

vvpatLaunch=Button(tk,text='Launch VVPAT',font=('Arial',14),command=vvpat,padx=5,pady=5)
vvpatLaunch.place(x=180,y=75)

def result():
    textRb.delete(0.0,END)
    textRc.delete(0.0,END)
    textRo.delete(0.0,END)
    textRb.insert(END,b)
    textRc.insert(END,c)
    textRo.insert(END,o)

dispResult=Button(tk,text='Click to See Final Result!',font=('Arial',14),command=result,padx=5,pady=5)
dispResult.place(x=140,y=150)

lblRc=Label(tk,text='Congress',font=('Arial', 14)).place(x=80,y=250)
textRc=Text(tk,height=2,width=5,font=('Arial', 14,'bold'))
textRc.place(x=90,y=280)

lblRb=Label(tk,text='BJP',font=('Arial', 14)).place(x=220,y=250)
textRb=Text(tk,height=2,width=5,font=('Arial', 14,'bold'))
textRb.place(x=210,y=280)

lblRo=Label(tk,text='Other/NOTA',font=('Arial', 14)).place(x=310,y=250)
textRo=Text(tk,height=2,width=5,font=('Arial', 14,'bold'))
textRo.place(x=320,y=280)

tk.mainloop()