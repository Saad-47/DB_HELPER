from PIL import Image,ImageTk
from tkinter import *
from tkinter import ttk,messagebox
from captcha.image import ImageCaptcha
import random
import sqlite3
conn = sqlite3.connect('manuf.db')
curs=conn.cursor()
global captcha_string
captcha_string = ''
class Login_window:
    global captcha_string
    captcha_string = ''
    def __init__(self,root):
        self.root = root
        self.root = root
        self.root.title('Login Window')
        self.root.geometry("1350x700+0+0")
        self.bg = ImageTk.PhotoImage(file = "back46.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, width=1750, height=900)
        #Frame
        global frame
        frame = Frame(self.root,bg="white",bd=2)
        frame.place(x=320,y=100,width=800,height=500)
        title = Label(frame,text = "LOGIN HERE",font = ("times new roman",30,"bold"),bg = "white", fg = "black").place(x = 250,y = 50)
        email = Label(frame,text = "E-mail Address",font = ("times new roman",18,"bold"),bg = "white", fg = "#31f400").place(x = 250,y = 150)
        self.text_email = Entry(frame,font = ("times new roman",15),bg = "#f6f5f0")
        self.text_email.place(x = 250,y = 180,width = 350,height = 35)
        password = Label(frame,text = "Password",font = ("times new roman",18,"bold"),bg = "white", fg = "#31f400").place(x = 250,y = 250)
        self.text_password = Entry(frame,show='*',font = ("times new roman",15),bg = "#f6f5f0")
        self.text_password.place(x = 250,y = 280,width = 350,height = 35)
        #captcha
        image = ImageCaptcha()
        data = image.generate('python')
        image.write("python","cap.png")
        self.btn_cap=ImageTk.PhotoImage(file="cap.png")
        btn=Button(frame,image=self.btn_cap,bd=0).place(x=248,y=340)
        self.btn_ref=Button(frame,cursor = "hand2",command = self.captcha ,text= "Refresh",bd=0,bg="white",fg = "#31f400",font=("times new roman",10)).place(x=410,y=340)
        txt = Label(frame,text = "Enter the given text!",font = ("times new roman",15),bg = "white", fg = "#31f400").place(x = 480,y = 350)
        self.text_cap = Entry(frame,font = ("times new roman",15),bg = "white")
        self.text_cap.place(x = 500,y = 375,width = 100,height = 25)
        btn_reg = Button(frame,cursor = "hand2",command = self.register_window,text = "Register new account?",font =("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=410)
        btn_forget = Button(frame,cursor = "hand2",command = self.forget_password,text = "Forget Password?",font =("times new roman",14),bg="white",bd=0,fg="red").place(x=490,y=410)
        btn_login = Button(frame,text = "Login",command = self.login,font =("times new roman",20,"bold"),fg="black",bg="#B00857",cursor = "hand2").place(x=338,y=450,width=180,height=40)

    def captcha(self):
        image = ImageCaptcha()
        number_list = ['0','1','2','3','4','5','6','7','8','9']
        alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        base_char = alphabet_lowercase + alphabet_uppercase + number_list
        captcha_string_list = []
        for i in range(6):

            # Select one character randomly.
            char = random.choice(base_char)
            # Append the character to the list.
            captcha_string_list.append(char)
            global captcha_string
            captcha_string = ''

            # Change the character list to string.    
        for item in captcha_string_list:
            captcha_string += str(item)
        data = image.generate(captcha_string)
        image.write(captcha_string,'cap.png')
        self.btn_cap=ImageTk.PhotoImage(file="cap.png")
        btn=Button(frame,image=self.btn_cap,bd=0).place(x=248,y=340)
       

    def reset(self):
        self.cmb_question.current(0)
        self.text_new_password.delete(0,END)
        self.text_password.delete(0,END)
        self.text_email.delete(0,END)
        self.text_answer.delete(0,END)
        
    def forget_password_elements(self):
        if self.cmb_question.get() == "Select" or self.text_answer.get() == "" or self.text_new_password.get() == "":
            messagebox.showerror("Error","All fields are required!",parent = self.root2)
        else:
            conn = sqlite3.connect('manuf.db')
            curs=conn.cursor()
            curs.execute("Select Email,Question,Answer from newdb where Email=?",(self.text_email.get(),))
            row2 = curs.fetchone()
            if row2[0] != self.text_email.get() or row2[1] != self.cmb_question.get() or row2[2] != self.text_answer.get():
                messagebox.showerror("Error","Please check the question and answer you just entered!",parent=self.root2)
                
            else:
                curs.execute("Update newdb set Password =? where Email=?",(self.text_new_password.get(),self.text_email.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been reset!!",parent=self.root2)
                self.reset()
                self.root2.destroy()
                
                
    def forget_password(self):
        if self.text_email.get() == "":
            messagebox.showerror("Error","Please Enter the Email to reset your password!",parent = self.root)
        else:
            curs.execute("Select * from newdb where Email=?",(self.text_email.get(),))
            row = curs.fetchone()
            if row == None:
                messagebox.showerror("Error","Please Enter the valid Email to reset your password!",parent = self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title=("Forget password")
                self.root2.geometry("360x400+495+150")
                self.root2.config(bg = "white")
                self.root2.focus_force()
                self.root2.grab_set()
                t = Label(self.root2,text = "Forget Password",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
                #elements
                question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=100)
                self.cmb_question=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                self.cmb_question['values']=("Select","Your first pet name","Your place of birth","Your first teacher in school")
                self.cmb_question.place(x=50,y=130,width=250)
                self.cmb_question.current(0)
                answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=180)
                self.text_answer=Entry(self.root2,font=("times new roman",15),bg="white")
                self.text_answer.place(x=50,y=210,width=250)
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=260)
                self.text_new_password=Entry(self.root2,font=("times new roman",15),bg="white")
                self.text_new_password.place(x=50,y=290,width=250)
                btn_change_password= Button(self.root2,text = "Reset Password",bg="green",fg="white",command = self.forget_password_elements,cursor = "hand2",font=("times new roman",15,"bold")).place(x=90,y=340)

    def register_window(self):
        self.root.destroy()
        import registrationgui
        
    def login(self):
        if (self.text_email.get() == "" or self.text_password.get() == ""):
            messagebox.showerror("Error","All fields are required",parent = self.root)
        else:
            curs.execute("Select * from newdb where Email=? and Password=?",(self.text_email.get(),self.text_password.get(),))
            row = curs.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username and password!!",parent=self.root)
            elif self.text_cap.get() == "python":
                messagebox.showinfo("Success","Welcome!!",parent=self.root)
                conn.close()                
            elif self.text_cap.get() != captcha_string:
                print(captcha_string)
                print(self.text_cap.get())
                messagebox.showerror("Error","Captcha does not Match",parent=self.root)
            else:
                messagebox.showinfo("Success","Welcome!!",parent=self.root)
            self.root.destroy()
            import intermenu
            conn.close()
                
root = Tk()
obj = Login_window(root)
root.mainloop()
