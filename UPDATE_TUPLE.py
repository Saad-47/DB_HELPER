from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
import CREATE_TABLE1
from CREATE_TABLE1 import *

def altering_data(self):
    self.attr_name_var = StringVar()
    self.data_length_var = StringVar()
    Table_frame = Frame(self.root4,bd = 4,relief = RIDGE,bg = "White")
    Table_frame.place(x = 600,y = 140,width = 500,height = 300)
    #scrollx_bar = Scrollbar(Table_frame, orient = HORIZONTAL)
    scrolly_bar = Scrollbar(Table_frame, orient = VERTICAL)
    self.Attributes_table = ttk.Treeview(Table_frame, columns = ("Attribute name","Datatype","Data Length","NOT NULL"),yscrollcommand = scrolly_bar.set)#,xscrollcommand = scrollx_bar.set
    #scrollx_bar.pack(side = BOTTOM, fill = X)
    scrolly_bar.pack(side = RIGHT, fill = Y)
    #scrollx_bar.config(command = self.Attributes_table.xview)
    scrolly_bar.config(command = self.Attributes_table.yview)
    self.Attributes_table.heading("Attribute name", text = "Attribute Name")
    self.Attributes_table.heading("Datatype", text = "Data Type")
    self.Attributes_table.heading("Data Length", text = "Data Length")
    self.Attributes_table['show'] = 'headings'
    self.Attributes_table.column("Attribute name",width = 150)
    self.Attributes_table.column("Datatype",width = 150)
    self.Attributes_table.column("Data Length",width = 150)
    self.Attributes_table.pack(fill = BOTH, expand = 1)
    self.Attributes_table.bind('<ButtonRelease-1>',self.focus)
    fetching(self)
    Manage_frame = Frame(self.root4,bd = 4,relief = RIDGE,bg = "green")
    Manage_frame.place(x = 20,y = 140,width = 540,height = 500)
    self.lbl_attr_name = Label(Manage_frame,text = "Attribute Name",bg = "green",fg = "white",font = ("times new roman",15,"bold"))
    self.lbl_attr_name.grid(row = 1,column = 0,pady = 10,padx = 20,sticky = "w")
    self.txt_attr_name = Entry(Manage_frame,textvariable = self.attr_name_var,font = ("times new roman",10,"bold"),bd = 5,relief = GROOVE)
    self.txt_attr_name.grid(row = 1,column = 1,pady = 10,padx = 20,sticky = "w")
    self.lbl_datatype = Label(Manage_frame,text = "Data Type",bg = "green",fg = "white",font = ("times new roman",15,"bold"))
    self.lbl_datatype.grid(row = 2,column = 0,pady = 10,padx = 20,sticky = "w")
    self.combo_datatype = ttk.Combobox(Manage_frame,font = ("times new roman",10,"bold"),state = "readonly")
    self.combo_datatype['values'] = ("--Select--","Integer","Text","Real","Blob")
    self.combo_datatype.grid(row = 2,column = 1,pady = 10,padx = 20,sticky = "w")
    self.combo_datatype.current(0)
    self.lbl_datalength = Label(Manage_frame,text = "Data Length",bg = "green",fg = "white",font = ("times new roman",15,"bold"))
    self.lbl_datalength.grid(row = 3,column = 0,pady = 10,padx = 20,sticky = "w")
    self.txt_datalength = Entry(Manage_frame,textvariable = self.data_length_var,font = ("times new roman",10,"bold"),bd = 5,relief = GROOVE)
    self.txt_datalength.grid(row = 3,column = 1,pady = 10,padx = 20,sticky = "w")

    self.lbl_NOTNULL = Label(Manage_frame,text = "NOT NULL",bg = "green",fg = "white",font = ("times new roman",15,"bold"))
    self.lbl_NOTNULL.grid(row = 4,column = 0,pady = 10,padx = 20,sticky = "w")
    self.combo_NULLKEY = ttk.Combobox(Manage_frame,font = ("times new roman",10,"bold"),state = "readonly")
    self.combo_NULLKEY['values'] = ("--Select--","Yes","No")
    self.combo_NULLKEY.grid(row = 4,column = 1,pady = 10,padx = 20,sticky = "w")
    self.combo_NULLKEY.current(0)
    self.lbl_PRIMARYKEY = Label(Manage_frame,text = "PRIMARY KEY",bg = "green",fg = "white",font = ("times new roman",15,"bold"))
    self.lbl_PRIMARYKEY.grid(row = 5,column = 0,pady = 10,padx = 20,sticky = "w")
    self.combo_PRIMARYKEY = ttk.Combobox(Manage_frame,font = ("times new roman",10,"bold"),state = "readonly")
    self.combo_PRIMARYKEY['values'] = ("--Select--","Yes","No")
    self.combo_PRIMARYKEY.grid(row = 5,column = 1,pady = 10,padx = 20,sticky = "w")
    self.combo_PRIMARYKEY.current(0)
    self.lbl_FOREIGNKEY = Label(Manage_frame,text = "FOREIGN KEY",bg = "green",fg = "white",font = ("times new roman",15,"bold"))
    self.lbl_FOREIGNKEY.grid(row = 6,column = 0,pady = 10,padx = 20,sticky = "w")
    self.combo_FOREIGNKEY = ttk.Combobox(Manage_frame,font = ("times new roman",10,"bold"),state = "readonly")
    self.combo_FOREIGNKEY['values'] = ("--Select--","Yes","No")
    self.combo_FOREIGNKEY.grid(row = 6,column = 1,pady = 10,padx = 20,sticky = "w")
    self.combo_FOREIGNKEY.current(0)
    self.counter = 2
    self.number = "m"
    self.alter = "y"
    self.goback = "n"
    btn_Back = Button(self.root4,text = "BACK",command = self.back,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold")).place(x = 75 ,y= 660)
    btn_RENAME_TABLE = Button(self.root4,text = "RENAME TABLE",command = self.next2,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold")).place(x = 275 ,y= 660)    
    btn_ADD = Button(self.root4,text = "ADD",command = self.next1,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold")).place(x = 475 ,y= 660)
    btn_cancel = Button(self.root4,text = "CANCEL",bg="green",fg="white",command = self.cancel,cursor = "hand2",font=("times new roman",10,"bold")).place(x=675 ,y= 660)
    #btn_modify = Button(self.root4,text = "MODIFY",bg="green",fg="white",command = self.next4,cursor = "hand2",font=("times new roman",10,"bold")).place(x=875 ,y= 660)
    
def fetching(self):
    conn = sqlite3.connect('manuf1.db')
    curs=conn.cursor()
    TABLE_NAME = self.cmb_table.get()
    curs.execute("PRAGMA table_info(%s)" % (self.cmb_table.get()))
    print(self.cmb_table.get())
    self.rows = curs.fetchall()
    print(len(self.rows))
    if len(self.rows) != 0:
        self.Attributes_table.delete(*self.Attributes_table.get_children())
        for row in self.rows:
            if (row[2][0:2] == "In"):
                print("integer")
                self.Attributes_table.insert("",END,values = (row[1],row[2][0:7],row[2][8:-1]))
            elif row[2][0:2] == "Te":
                self.Attributes_table.insert("",END,values = (row[1],row[2][0:4],row[2][5:-1]))
            elif row[2][0:2] == "Re":
                self.Attributes_table.insert("",END,values = (row[1],row[2][0:4],row[2][5:-1]))
            elif row[2][0:2] == "Bl":
                self.Attributes_table.insert("",END,values = (row[1],row[2][0:4],row[2][5:-1]))
            print(row[1],row[2][0:7],row[2][8:-1])
            print(row[1],row[2][0:4],row[2][5:-1])
            conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error","No Data Availabe!",parent = self.root5)

def adding(self):  
    conn = sqlite3.connect('manuf1.db')
    curs=conn.cursor()
    TABLE_NAME = self.cmb_table.get()
    column_name = self.rows[0][1]
    new_column_name = self.txt_attr_name.get()
    curs.execute("ALTER TABLE %s ADD COLUMN %s %s(%s)" % (TABLE_NAME,self.txt_attr_name.get(),self.combo_datatype.get(),self.txt_datalength.get() ))
    conn.commit()
    messagebox.showinfo("Success","Column Added Successfully!",parent = self.root4)
    conn.close()
    fetching(self)
    clear(self)
##    
##def modify(self):
##    MODIFY_TABLE = []
##    conn = sqlite3.connect('manuf1.db')
##    curs=conn.cursor()
##    TABLE_NAME = self.cmb_table.get()
##    column_name = self.rows[0][1]
##    new_column_name = self.txt_attr_name.get()
##    curs.execute("PRAGMA table_info ("+TABLE_NAME+") ")
##    self.rows = curs.fetchall()
##    for row in self.rows:
##        MODIFY_TABLE.append(row[1])
##    print(MODIFY_TABLE)
##    MODIFY_TABLE.remove(self.focus[0])
##    print("After removing",MODIFY_TABLE)
##    print("The column for edit")
##    print(self.focus[0])
##    print(self.combo_datatype.get())
##    print(self.txt_datalength.get())
##    curs.execute('create table if not exists temp(%s %s(%s))' % (self.txt_attr_name.get(),self.combo_datatype.get(),self.txt_datalength.get()))
##    print(MODIFY_TABLE)
##    for i in MODIFY_TABLE:
##        print("this is row[1]: column to add from original to temp")
##        print(row[1])
##        name = row[1]
##        print("table from which the data is copying",TABLE_NAME)
##        #print("remaining column and table name",column,TABLE_NAME)
##        curs.execute('insert into temp(%s) select %s from %s ' % (i,i,TABLE_NAME))
##        conn.commit()
##
##    print("BEfore drop",TABLE_NAME)
##    curs.execute('drop table %s ' % (TABLE_NAME))
##    conn.commit()
##    print("after drop",TABLE_NAME)
##    curs.execute('alter table temp rename to %s' % (TABLE_NAME))
##    conn.commit()
##    print("after rename",TABLE_NAME)
##    messagebox.showinfo("Success","Column Modified Successfully!",parent = self.root4)
##    fetching(self)
##    clear(self)

def rename(self):
    self.root5=Toplevel()
    self.root5.title=("Rename Table")
    self.root5.geometry("360x400+495+150")
    self.root5.config(bg = "white")
    self.root5.focus_force()
    self.root5.grab_set()
    self.attr_tablename_var = StringVar()
    TABLE_NAME = self.cmb_table.get()
    self.attr_tablename_var.set(TABLE_NAME)
    self.lbl_currenttable_name = Label(self.root5,text = "Current Table Name",bg = "white",fg = "green",font = ("times new roman",15,"bold"))
    self.lbl_currenttable_name.grid(row = 0,column = 0,pady = 10,padx = 20,sticky = "w")
    self.txt_currenttable_name = Entry(self.root5,textvariable = self.attr_tablename_var,font = ("times new roman",10,"bold"),bd = 5,relief = GROOVE)
    self.txt_currenttable_name.grid(row = 1,column = 0,pady = 10,padx = 20,sticky = "w")
    self.lbl_newtable_name = Label(self.root5,text = "New Table Name",bg = "white",fg = "green",font = ("times new roman",15,"bold"))
    self.lbl_newtable_name.grid(row = 2,column = 0,pady = 10,padx = 20,sticky = "w")
    self.txt_newtable_name = Entry(self.root5,font = ("times new roman",10,"bold"),bd = 5,relief = GROOVE)
    self.txt_newtable_name.grid(row = 3,column = 0,pady = 10,padx = 20,sticky = "w")
    self.number = "n"
    btn_RENAME_TABLE = Button(self.root5,text = "CHANGE",command = self.next2,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold"))
    btn_RENAME_TABLE.grid(row = 4,column = 0,pady = 10,padx = 20,sticky = "w")


    

def clear(self):
    self.txt_attr_name.delete(0,END)
    self.txt_datalength.delete(0,END)
    self.combo_datatype.current(0)
    self.combo_NULLKEY.current(0)
    self.combo_PRIMARYKEY.current(0)
    self.combo_FOREIGNKEY.current(0)
    
