from tkinter import *
from tkinter import ttk,messagebox
import CREATE_TABLE1
from CREATE_TABLE1 import *
import ALTER_TABLE
from ALTER_TABLE import *
import DROP_TABLE
from DROP_TABLE import *
##import INSERT_TUPLE
##from INSERT_TUPLE import *
import UPDATE_TUPLE
from UPDATE_TUPLE import *
import sqlite3
EXIST_TABLE_NAME = ["--Existing Tables--"]
class MENU:
    
    def __init__(self , root):
        self.root = root
        self.root.title('MAIN MENU')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        menubar = Menu(self.root)
        filemenu = Menu(menubar,tearoff = 0,activeborder = 5,disabledforeground = 'red')
        filemenu.add_command(label = "Change Password",command = self.changepassword)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit",activebackground = "red",command = self.close)
        ddlmenu = Menu(menubar,tearoff = 0,activeborder = 5)
        ddlmenu.add_command(label = "Create Table",command = self.Creation)
        ddlmenu.add_separator()
        ddlmenu.add_command(label = "Alter Table",command = self.Alteration)
        ddlmenu.add_separator()
        ddlmenu.add_command(label = "Drop Table",command = self.drop)
        ddlmenu.add_separator()
        ddlmenu.add_command(label = "View Table Structure")
        dmlmenu = Menu(menubar,tearoff = 0,activeborder = 5)
        dmlmenu.add_command(label = "Insert Tuple",command = self.Insert_Tuple)
        dmlmenu.add_separator()
        dmlmenu.add_command(label = "Alter Tuple",command = self.Update_Tuple)
        dmlmenu.add_separator()
        dmlmenu.add_command(label = "Drop Tuple")
        dmlmenu.add_separator()
        dmlmenu.add_command(label = "View Table Data")
        infomenu = Menu(menubar,tearoff = 0)
        infomenu.add_command(command = self.info)
        menubar.add_cascade(label = "File", menu = filemenu)
        menubar.add_cascade(label = "DDL", menu = ddlmenu)
        menubar.add_cascade(label = "DML", menu = dmlmenu)
        menubar.add_cascade(label = "INFO", menu = infomenu)
        root.config(menu = menubar)
    def close(self):
        answer = messagebox.askquestion("Exit","Do you really want to quit!",parent = self.root)
        if answer == "yes":
            self.root.destroy()
        return None
    def changepassword(self):
        self.root2=Toplevel()
        self.root2.title=("Forget password")
        self.root2.geometry("360x400+495+150")
        self.root2.config(bg = "white")
        self.root2.focus_force()
        self.root2.grab_set()
        t = Label(self.root2,text = "Change Password",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
        #elements
        old_password=Label(self.root2,text="Old Password",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=100)
        self.text_old_password=Entry(self.root2,font=("times new roman",15),bg="white")
        self.text_old_password.place(x=50,y=130,width=250)
        new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=180)
        self.text_new_password=Entry(self.root2,font=("times new roman",15),bg="white")
        self.text_new_password.place(x=50,y=210,width=250)
        c_new_password=Label(self.root2,text="Confirm New Password",font=("times new roman",15,"bold"),fg="black",bg="white").place(x=50,y=260)
        self.text_c_new_password=Entry(self.root2,font=("times new roman",15),bg="white")
        self.text_c_new_password.place(x=50,y=290,width=250)
        btn_change_password= Button(self.root2,text = "Change Password",command = self.change,bg="green",fg="white",cursor = "hand2",font=("times new roman",15,"bold")).place(x=90,y=340)

    def change(self):
        if self.text_old_password.get() == "" or self.text_new_password.get() == "" or self.text_c_new_password.get() == "":
            messagebox.showerror("Error","All fields are required!",parent = self.root2)
        elif self.text_new_password.get() != self.text_c_new_password.get():
            messagebox.showerror("Error","Both password should match!",parent = self.root2)
        else:
            conn = sqlite3.connect('manuf.db')
            curs=conn.cursor()
            curs.execute("Select Password from newdb where Password=?",(self.text_old_password.get(),))
            row2 = curs.fetchone()
            if row2[0] != self.text_old_password.get():
                messagebox.showerror("Error","Please check your old Pasword you just entered!",parent=self.root2)
            else:
                curs.execute("Update newdb set Password =? where Password=?",(self.text_new_password.get(),self.text_old_password.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Your password has been changed!!",parent=self.root2)
                self.reset()
                self.root2.destroy()

    def reset(self):
        self.text_old_password.delete(0,END)
        self.text_new_password.delete(0,END)
        self.text_c_new_password.delete(0,END)

    def info(self):
        self.root3=Toplevel()
        self.root3.title=("Information area")
        self.root3.geometry("660x400+300+150")
        self.root3.config(bg = "white")
        self.root3.focus_force()
        self.root3.grab_set()
        t = Label(self.root3,text = "Developers\nTE CSE 2019-20",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
        info = '''****************************************************************************
                                             This project is done by:-                                                 
                                           1.Muzammil Bagwan-03                                      
                                        2.Usaed Shaikh-48                                         
                                        3.Fayzan Sayed-46                                         
                                         4.Md.Saad Shaikh-47                                       
                                         5.Abdullah Quereshi-44                                    
                                          Programming language used: Python                                   
                  ****************************************************************************'''
        text=Label(self.root3,text=info,font=("times new roman",15,"bold"),fg="black",bg="white")
        text.place(x=50,y=130,width=500)

    
    def Creation(self):
        self.root4=Toplevel()
        self.root4.title=("Crate table")
        self.root4.geometry("1350x700+0+0")
        self.root4.config(bg = "white")
        self.root4.focus_force()
        self.root4.grab_set()
        title = Label(self.root4,text = "NEW TABLE CREATION",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
        table_name=Label(self.root4,text="New Table Name",font=("times new roman",10,"bold"),fg="black",bg="white").place(x=45,y=100)
        self.text_table_name=Entry(self.root4,font=("times new roman",15),bg="white")
        self.text_table_name.place(x=155,y=100,width=120,height=20)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        curs.execute('select name from sqlite_master where type= "table"')
        table = curs.fetchall()
        for i in table:
            EXIST_TABLE_NAME.append(i)
        self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_table.place(x=600,y=100,width=180,height=20)
        self.cmb_table['values']= EXIST_TABLE_NAME
        self.cmb_table.current(0)
        conn.close()
        CREATE_TABLE1.entry_fields(self)
##        attr_num=Label(self.root4,text="Num of Attributes",font=("times new roman",10,"bold"),fg="black",bg="white").place(x=45,y=130)
##        self.text_attr_num=Entry(self.root4,font=("times new roman",15),bg="white")
##        self.text_attr_num.place(x=155,y=130,width=60,height=20)
##        btn_Create_table= Button(self.root4,text = "CREATE COLUMNS",bg="green",fg="white",command = self.Selector,cursor = "hand2",font=("times new roman",10,"bold")).place(x=255,y=130)

        
##    def Selector(self):
##        if self.text_attr_num.get() == "1":
##            CREATE_TABLE.entry_fields1(self)
##        elif self.text_attr_num.get() == "2":
##            CREATE_TABLE.entry_fields2(self)
##        elif self.text_attr_num.get() == "3":
##            CREATE_TABLE.entry_fields3(self)
##        elif self.text_attr_num.get() == "4":
##            CREATE_TABLE.entry_fields4(self)
##        elif self.text_attr_num.get() == "5":
##            CREATE_TABLE.entry_fields5(self)
##        elif self.text_attr_num.get() == "6":
##            CREATE_TABLE.entry_fields6(self)
##        elif self.text_attr_num.get() =="7":
##            CREATE_TABLE.entry_fields7(self)
##        elif self.text_attr_num.get() == "8":
##            CREATE_TABLE.entry_fields8(self)
##        elif self.text_attr_num.get() == "9":
##            CREATE_TABLE.entry_fields9(self)
##        elif self.text_attr_num.get() == "10":
##            CREATE_TABLE.entry_fields10(self)
##        elif self.text_attr_num.get() == "11":
##            CREATE_TABLE.entry_fields11(self)
##        elif self.text_attr_num.get() == "12":
##            CREATE_TABLE.entry_fields12(self)
##        elif self.text_attr_num.get() == "13":
##            CREATE_TABLE.entry_fields13(self)
##        elif self.text_attr_num.get() == "14":
##            CREATE_TABLE.entry_fields14(self)
##        elif self.text_attr_num.get() == "15":
##            CREATE_TABLE.entry_fields15(self)
##        else:
##            messagebox.showerror("Error","Cannot create Attributes more than 15 !!",parent = self.root4)

    def Selector_Save(self):
        CREATE_TABLE1.ALLSave_table(self)
        if self.text_attr_num == "1":
            print("Selector save table")
            CREATE_TABLE1.Save_table1(self)
        elif self.text_attr_num == "2":
            CREATE_TABLE1.Save_table2(self)
        elif self.text_attr_num == "3":
            CREATE_TABLE1.Save_table3(self)
        elif self.text_attr_num == "4":
            CREATE_TABLE1.Save_table4(self)
        elif self.text_attr_num == "5":
            CREATE_TABLE1.Save_table5(self)
        elif self.text_attr_num == "6":
            CREATE_TABLE1.Save_table6(self)
        elif self.text_attr_num == "7":
            CREATE_TABLE1.Save_table7(self)
        elif self.text_attr_num == "8":
            CREATE_TABLE1.Save_table8(self)
        elif self.text_attr_num == "9":
            CREATE_TABLE1.Save_table9(self)
        elif self.text_attr_num == "10":
            CREATE_TABLE1.Save_table10(self)
        elif self.text_attr_num == "11":
            CREATE_TABLE1.Save_table11(self)
        elif self.text_attr_num == "12":
            CREATE_TABLE1.Save_table12(self)
        elif self.text_attr_num == "13":
            CREATE_TABLE1.Save_table13(self)
        elif self.text_attr_num == "14":
            CREATE_TABLE1.Save_table14(self)
        elif self.text_attr_num == "15":
            CREATE_TABLE1.Save_table15(self)

    def Alteration(self):
        self.root4=Toplevel()
        self.root4.title=("Alter table")
        self.root4.geometry("1350x700+0+0")
        self.root4.config(bg = "white")
        self.root4.focus_force()
        self.root4.grab_set()
        title = Label(self.root4,text = "ALTER TABLE ",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
        table_name=Label(self.root4,text="Select Table Name",font=("times new roman",10,"bold"),fg="black",bg="white").place(x=45,y=100)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        #self.cmb_table.clear()
        #self.cmb_table.insert(0,"--Existing Tables--")
        curs.execute('select name from sqlite_master where type= "table"')
        table = curs.fetchall()
        for i in table:
            EXIST_TABLE_NAME.append(i)
        self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_table.place(x=165,y=100,width=180,height=20)
        self.cmb_table['values']= EXIST_TABLE_NAME
        self.cmb_table.current(0)
        conn.close()
        self.counter = 1
        btn_Alter_Table= Button(self.root4,text = "Show Table",bg="green",fg="white",command = self.next1 ,cursor = "hand2",font=("times new roman",10,"bold")).place(x=360 ,y= 100)

    def next1(self):
        if self.counter == 2:
            if (self.txt_attr_name.get() == "" or self.combo_datatype == "--Select--" or self.txt_datalength == ""):
                messagebox.showerror("Error","The attribute Name,Datatype and Datalength are required!",parent = self.root4)
            else:
                ALTER_TABLE.adding(self)
        elif self.counter == 1:
            if self.cmb_table.get() == "--Existing Tables--":
                messagebox.showerror("Error","PLease Select the Table!",parent = self.root4)
            else:
                ALTER_TABLE.altering_data(self)
        
        
    def next2(self):
        if self.number == "m":
            ALTER_TABLE.rename(self)
        elif self.number == "n":
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            TABLE_NAME = self.cmb_table.get()
            curs.execute('ALTER TABLE '+TABLE_NAME+' RENAME TO '+self.txt_newtable_name.get()+' ')
            conn.commit()
            self.cmb_table.set(self.txt_newtable_name.get())
            messagebox.showinfo("Success","Table Renamed Successfully!",parent = self.root5)
            self.root5.destroy()

    def focus(self,ev):
        self.cursor_get = self.Attributes_table.item(self.Attributes_table.selection())
        self.focus = self.cursor_get['values']
        print(self.focus)
        #var = self.focus[0]
        self.attr_name_var.set(self.focus[0])
        self.combo_datatype.set(self.focus[1])
        self.data_length_var.set(self.focus[2])
        print("this is focus")
        print(self.focus[0])
        print("this is var")
        print(self.attr_name_var)

    def next4(self):
        if self.alter == "y":
           ALTER_TABLE.modify(self)
        elif self.back == "b":
           self.root4.destroy() 

    def drop(self):
        self.root5=Toplevel()
        self.root5.title=("Drop Table")
        self.root5.geometry("660x600+335+70")
        self.root5.config(bg = "white")
        self.root5.focus_force()
        self.root5.grab_set()
        EXIST_TABLE_NAME.clear()
        self.lbl_currenttable_name = Label(self.root5,text = "Select Table Name",bg = "white",fg = "green",font = ("times new roman",15,"bold"))
        self.lbl_currenttable_name.grid(row = 0,column = 0,pady = 10,padx = 20,sticky = "w")
        EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        curs.execute('select name from sqlite_master where type= "table"')
        table = curs.fetchall()
        for i in table:
            EXIST_TABLE_NAME.append(i)
        self.cmb_table=ttk.Combobox(self.root5,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_table.grid(row = 1,column = 0,pady = 10,padx = 20,sticky = "w")
        self.cmb_table['values']= EXIST_TABLE_NAME
        self.cmb_table.current(0)
        conn.close()
        self.next = "C"
        btn_CONFORM = Button(self.root5,text = "Confirm",command = self.next3 ,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold"))
        btn_CONFORM.grid(row = 1,column = 1,pady = 10,padx = 20,sticky = "w")
        
    def next3(self):
        if self.next == "C":
            DROP_TABLE.records(self)
        elif self.next == "D":
            DROP_TABLE.delete_table(self)
        
    def back(self):
        if self.goback == "Y":
            print("back")
            self.root5.destroy()
        else:
            self.root4.destroy()
        
    def cancel(self):
        answer = messagebox.askquestion("Cancel","Do you really want to Cancel!",parent = self.root)
        if answer == "yes":
            self.root4.destroy()
        return None

    def Insert_Tuple(self):
        self.root4=Toplevel()
        self.root4.title=("Insert Tuple")
        self.root4.geometry("1350x700+0+0")
        self.root4.config(bg = "white")
        self.root4.focus_force()
        self.root4.grab_set()
        title = Label(self.root4,text = "Insert Tuple",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
        table_name=Label(self.root4,text="Select Table Name",font=("times new roman",10,"bold"),fg="black",bg="white").place(x=45,y=100)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        #self.cmb_table.clear()
        #self.cmb_table.insert(0,"--Existing Tables--")
        curs.execute('select name from sqlite_master where type= "table"')
        table = curs.fetchall()
        for i in table:
            EXIST_TABLE_NAME.append(i)
        self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_table.place(x=165,y=100,width=180,height=20)
        self.cmb_table['values']= EXIST_TABLE_NAME
        self.cmb_table.current(0)
        conn.close()
        self.f = 1
        btn_Alter_Table= Button(self.root4,text = "Show Table",bg="green",fg="white",command = self.forward ,cursor = "hand2",font=("times new roman",10,"bold")).place(x=360 ,y= 100)
        
    def forward(self):
        if self.f == 1:
            INSERT_TUPLE.entry_fields(self)
        elif INSERT_TUPLE.f == 'a':
            INSERT_TUPLE.Checking_length(self)
        if self.f == "u":
            UPDATE_TUPLE.altering_data(self)

    def Update_Tuple(self):
        self.root4=Toplevel()
        self.root4.title=("Update Tuple")
        self.root4.geometry("1350x700+0+0")
        self.root4.config(bg = "white")
        self.root4.focus_force()
        self.root4.grab_set()
        title = Label(self.root4,text = "Update Tuple",font = ("times new roman",20,"bold"),bg = "white",fg = "red",).place(x=0,y=10,relwidth=1)
        table_name=Label(self.root4,text="Select Table Name",font=("times new roman",10,"bold"),fg="black",bg="white").place(x=45,y=100)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        #self.cmb_table.clear()
        #self.cmb_table.insert(0,"--Existing Tables--")
        curs.execute('select name from sqlite_master where type= "table"')
        table = curs.fetchall()
        for i in table:
            EXIST_TABLE_NAME.append(i)
        self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_table.place(x=165,y=100,width=180,height=20)
        self.cmb_table['values']= EXIST_TABLE_NAME
        self.cmb_table.current(0)
        conn.close()
        self.f = "u"
        btn_Show_Table= Button(self.root4,text = "Show Table",bg="green",fg="white",command = self.forward ,cursor = "hand2",font=("times new roman",10,"bold")).place(x=360 ,y= 100)
        
        
root = Tk()
obj = MENU(root)
root.mainloop()
