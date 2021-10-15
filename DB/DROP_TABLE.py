from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
EXIST_TABLE_NAME = ["--Existing Tables--"]

def records(self):
    self.attr_name_var = StringVar()
    Table_frame = Frame(self.root5,bd = 4,relief = RIDGE,bg = "White")
    Table_frame.place(x = 70,y = 100,width = 500,height = 300)
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
    #self.Attributes_table.bind('<ButtonRelease-1>',self.next2)
    fetching(self)
    self.next = "D"
    self.goback = "Y"
    btn_BACK = Button(self.root5,text = "BACK",command = self.back ,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold"))
    btn_BACK.place(x = 70,y = 410)#, width = 50,height = 30
    btn_DROP_TABLE = Button(self.root5,text = "DELETE",command = self.next3 ,bg="green",fg="white",cursor = "hand2",font=("times new roman",10,"bold"))
    btn_DROP_TABLE.place(x = 270,y = 410)#, width = 50,height = 30

def delete_table(self):
    TABLE_NAME = self.cmb_table.get()
    answer = messagebox.askquestion("Delete","Do you really want to Delete this Table!",parent = self.root5)
    if answer == "yes":
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        curs.execute('DROP TABLE '+TABLE_NAME+' ')
        conn.commit()
        conn.close()
        EXIST_TABLE_NAME.clear()
        EXIST_TABLE_NAME.insert(0,"--Existing Table--")
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
        messagebox.showinfo("Success","Table Deleted Successfully!",parent = self.root5)
        EXIST_TABLE_NAME.clear()
        self.root5.destroy()
        self.drop()
            
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


