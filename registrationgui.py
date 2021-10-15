from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk,messagebox
#import pymysql
import sqlite3
conn = sqlite3.connect('manuf.db')
curs=conn.cursor()
class Register:
    def __init__(self , root):
        self.root = root
        self.root.title('Registration Window')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # bg image
        self.bg = ImageTk.PhotoImage(file = "back46.png")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        self.left = ImageTk.PhotoImage(file = "back45.png")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        #title
        title=Label(frame1,text="Register Here",font=("times new roman",20,"bold"),bg="white",fg="#31f400").place(x=50,y=30)
        #1st line
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=50,y=100)
        self.text_fname=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_fname.place(x=50,y=130,width=250)
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=370,y=100)
        self.text_lname=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_lname.place(x=370,y=130,width=250)
        #2nd line
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=50,y=170)
        self.text_contact=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_contact.place(x=50,y=200,width=250)
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=370,y=170)
        self.text_email=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_email.place(x=370,y=200,width=250)
        #3rd line
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select","Your first pet name","Your place of birth","Your first teacher in school")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=370,y=240)
        self.text_answer=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_answer.place(x=370,y=270,width=250)
        #4th line
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=50,y=310)
        self.text_password=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_password.place(x=50,y=340,width=250)
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="#31f400").place(x=370,y=310)
        self.text_cpassword=Entry(frame1,font=("times new roman",15),bg="#f6f5f0")
        self.text_cpassword.place(x=370,y=340,width=250)
        #terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        self.btn_img=ImageTk.PhotoImage(file="back49.png")
        btn=Button(self.root,image=self.btn_img,bd=0,command = self.register_data,cursor="hand2").place(x=525,y=530,height=40,width=280)
        self.btn_limg=ImageTk.PhotoImage(file="back48.png")
        btn_login=Button(frame1,image=self.btn_limg,bd=0,cursor="hand2",command=self.login_window).place(x=360,y=430,height=40,width=280)

    def login_window(self):
        self.root.destroy()
        import login
        
    def clear(self):
        self.text_fname.delete(0,END)
        self.text_lname.delete(0,END)
        self.text_contact.delete(0,END)
        self.text_email.delete(0,END)
        self.text_answer.delete(0,END)
        self.text_password.delete(0,END)
        self.text_cpassword.delete(0,END)
        self.cmb_question.current(0)
        
    def register_data(self):
        if self.text_fname.get()=="" or self.text_email.get()=="" or self.cmb_question.get()=="Select" or self.text_answer.get()=="" or self.text_password.get()=="" or self.text_cpassword.get()=="" or self.text_contact.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        elif self.text_password.get() != self.text_cpassword.get():
            messagebox.showerror("Error","Both password should match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Accept the terms and condition",parent=self.root)
        else:
            #conn.execute('create table newdb(First_Name,Last_Name,Contact,Email,Question,Answer,Password)')
            First_Name = self.text_fname.get()
            Last_Name = self.text_lname.get()
            Contact = self.text_contact.get()
            Email = self.text_email.get()
            Question = self.cmb_question.get()
            Answer = self.text_answer.get()
            Password  = self.text_password.get()
            curs.execute("Select * from newdb where Email=?",(self.text_email.get(),))
            row = curs.fetchone()
            if row != None:
                messagebox.showerror("Error","This User already exists!!",parent=self.root)
            else:
                curs.execute('INSERT INTO newdb(First_Name,Last_Name,Contact,Email,Question,Answer,Password) VALUES (:First_Name,:Last_Name,:Contact,:Email,:Question,:Answer,:Password)',{'First_Name':First_Name,'Last_Name':Last_Name,'Contact':Contact,'Email':Email,'Question':Question,'Answer':Answer,'Password':Password})
                conn.commit()
                info2=curs.execute('Select First_Name,Last_Name,Contact,Email,Question,Answer,Password from newdb')
                print("First_Name\tLast_Name\t  Contact\t\t  Email\t\t\tQuestion\t  Answer\t  Password\n")
                for row in info2:  
                    print(row[0]," "*(20),row[1],""*(20),row[2],""*(20),row[3],""*(30),row[4],""*(40),row[5],""*(30),row[6],"\n")
       
                messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                conn.commit
                self.clear()
root = Tk()
obj = Register(root)
root.mainloop()
