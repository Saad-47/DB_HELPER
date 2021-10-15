from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

EXIST_TABLE_NAME = ["--Existing Tables--"]
conn = sqlite3.connect('manuf1.db')
curs=conn.cursor()
curs.execute('select name from sqlite_master where type= "table"')
table = curs.fetchall()
for i in table:
    EXIST_TABLE_NAME.append(i)
global my_entries
my_entries = []
global TABLE_NAME
TABLE_NAME = ''
def entry_fields(self):
    print("In the entry fields fun")
    fetching(self)
    #entry frame
    entry_frame = Frame(self.root4)
    entry_frame.place(x=35,y=200,width = 900, height = 270)
    #main frame
    main_frame = Frame(entry_frame,height = 500,width = 1350)
    main_frame.pack(fill = BOTH, expand = 1)#.grid(sticky = "news")#
    #canvas
    my_canvas = Canvas(main_frame,)
    my_canvas.pack(side = LEFT, fill=BOTH, expand =1)#.grid(row = 2, column = 0, pady = (5,0) ,sticky = "nw")#
    #scrollbar
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill=Y)#.grid(row = 0,column  =1,sticky = "ns")#
    my_xscrollbar = Scrollbar(main_frame, orient=HORIZONTAL, command = my_canvas.xview)
    my_xscrollbar.pack(side = BOTTOM, fill=X)
    #configure canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    my_canvas.configure(xscrollcommand = my_xscrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    
    #second frame inside canvas
    global second_frame
    second_frame = Frame(my_canvas)
    #add new frame to window in a canvas
    my_canvas.create_window((0,0), window = second_frame, anchor = "nw")

    #Label(second_frame, text = f'0').grid(row = 1,column =0,pady = 10,padx = 10)
    for i in range(1,11):
        Label(second_frame, text = f'{i}').grid(row = i,column =0,pady = 10,padx = 10)
    
    
    for i in range(1,11):
        for j in range(len(self.rows)):
            my_entry = Entry(second_frame,font=("times new roman",15),bg="white")
            my_entry.grid(row = i,column = j,pady = 1,padx = 1,sticky = "w")#.place(x= 45,y= 50,width=100,height=20)
            my_entries.append(my_entry)
            
    btn_back= Button(self.root4,text = "BACK",bg="green",fg="white",command = self.back,cursor = "hand2",font=("times new roman",10,"bold")).place(x = 235 ,y= 490)
    btn_cancel= Button(self.root4,text = "CANCEL",bg="green",fg="white",command = self.cancel,cursor = "hand2",font=("times new roman",10,"bold")).place(x=435 ,y= 490)
    btn_Create_Table= Button(self.root4,text = "INSERT TUPLE",bg="green",fg="white",command = printing,cursor = "hand2",font=("times new roman",10,"bold")).place(x=635 ,y= 490)

def fetching(self):
    conn = sqlite3.connect('manuf1.db')
    curs=conn.cursor()
    curs.execute("PRAGMA table_info('%s')" % (self.cmb_table.get()))
    print(self.cmb_table.get())
    self.rows = curs.fetchall()
    print(len(self.rows))
    global col
    col = []
    global TABLE_NAME
    TABLE_NAME = self.cmb_table.get()
    print("Table name at top",TABLE_NAME)
    print(self.rows)
    if len(self.rows) != 0:
        for i in range(len(self.rows)):
            columns = self.rows[i][1]
            table_name=Label(self.root4,text=columns,font=("times new roman",13,"bold"),fg="black",bg="white")
            table_name.place(x=135+(i*200),y=170)
            col.append(columns)       
     
        print(columns)
        global length
        length = len(self.rows)
        print("the length ",length)
        print("the self.rows  ",len(self.rows))
    else:
        messagebox.showerror("Error","No Data Availabe!",parent = self.root4)

def printing():
    entry_list = ''
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
    print("the entry list\n",my_entries[0].get(),my_entries[2].get(),my_entries[1].get(),my_entries[5].get())
    f = 'a'
    Checking_length()
    

def Checking_length():
    
    print(length)
    if length == 1:
        Checking_fields1()
    elif length == 2:
        Checking_fields2()
    elif length == 3:
        Checking_fields3()
    elif length == 4:
        Checking_fields4()
    elif length == 5:
        Checking_fields5()
    elif length == 6:
        Checking_fields6()
    elif length == 7:
        Checking_fields7()
    elif length == 8:
        Checking_fields8()
    elif length == 9:
        Checking_fields9()
    elif length == 10:
        Checking_fields10()
    elif length == 11:
        Checking_fields11()
    elif length == 12:
        Checking_fields12()
    elif length == 13:
        Checking_fields13()
    elif length == 14:
        Checking_fields14()
    elif length == 15:
        Checking_fields15()
    else:
        print("Not went there")
    

def Checking_fields1():
    print("field 1")
    print(my_entries[0].get())
    if my_entries[0].get() != '' and my_entries[1].get() == '':
        print("only one data is present inside")
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[0].get()+"')")
            conn.commit()
        print("data inserted ")
        info2=conn.execute("SELECT %s FROM %s" % (*col,TABLE_NAME))
        for row in info2:  
            print("data:", row[0])#,"Model:", row[1])
        print("data displayed!")
        conn.close()        

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() == ''):
        print("two data is present inside")
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(2):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()        
    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() == ''):
        print("three data is present inside")
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(3):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()          

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() == ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(4):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() == ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(5):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != ''
      and my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() == ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(6):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != ''
      and my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() == ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(7):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != ''
      and my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() == ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(8):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()


    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != ''
      and my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != ''
      and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() == ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(9):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()

    elif (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != ''
      and my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != ''
      and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != ''):
        print("Table name is ",TABLE_NAME)
        conn = sqlite3.connect('manuf1.db')
        curs=conn.cursor()
        print("In the database")
        print("THe column list ", *col)
        for i in col:
            for j in range(10):
                curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+i+"') VALUES ('"+my_entries[j].get()+"')")
            
            conn.commit()
        print("data inserted ")
        info2 = conn.execute("SELECT * FROM %s" % (TABLE_NAME))
        for row in info2:
            print(row)
            #print("data1:", row[0])#,"data2:", row[1])
        print("data displayed!")
        conn.close()

def Checking_fields2():
    print("field 2")
    print(my_entries[0].get())
    if my_entries[0].get() != '' and my_entries[2].get() == '':
        if my_entries[0].get() != '' and my_entries[1].get() != '':
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() == '':
        if my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '':
            print("two data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)
    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() != '' and my_entries[10].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
           my_entries[8].get() != '' and my_entries[9].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() != '' and my_entries[10].get() != '' and my_entries[12].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
           my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() != '' and my_entries[10].get() != '' and my_entries[12].get() != '' and my_entries[14].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
           my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)
        
    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() != '' and my_entries[10].get() != '' and my_entries[12].get() != '' and my_entries[14].get() != '' and
         my_entries[16].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
           my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() != '' and my_entries[10].get() != '' and my_entries[12].get() != '' and my_entries[14].get() != '' and
         my_entries[16].get() != '' and my_entries[18].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
           my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
           my_entries[16].get() != '' and my_entries[17].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[2].get() != '' and my_entries[4].get() != '' and my_entries[6].get() != '' and
         my_entries[8].get() != '' and my_entries[10].get() != '' and my_entries[12].get() != '' and my_entries[14].get() != '' and
         my_entries[16].get() != '' and my_entries[18].get() != ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
           my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
           my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != ''):
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"') VALUES ('"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()        
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)


def Checking_fields3():
    print("field 3")
    print(my_entries[0].get())
    if my_entries[0].get() != '' and my_entries[3].get() == '':
        if my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '':
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() == '':
        if my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '':
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() != '' and my_entries[15].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() != '' and my_entries[15].get() != '' and
         my_entries[18].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() != '' and my_entries[15].get() != '' and
         my_entries[18].get() != '' and my_entries[21].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and
           my_entries[18].get() != '' and my_entries[19].get() != '' and my_entries[20].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[18].get()+"','"+my_entries[19].get()+"','"+my_entries[20].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() != '' and my_entries[15].get() != '' and
         my_entries[18].get() != '' and my_entries[21].get() != '' and my_entries[24].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and
           my_entries[18].get() != '' and my_entries[19].get() != '' and my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[18].get()+"','"+my_entries[19].get()+"','"+my_entries[20].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() != '' and my_entries[15].get() != '' and
         my_entries[18].get() != '' and my_entries[21].get() != '' and my_entries[24].get() != '' and my_entries[27].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and
           my_entries[18].get() != '' and my_entries[19].get() != '' and my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
           my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[18].get()+"','"+my_entries[19].get()+"','"+my_entries[20].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[3].get() != '' and my_entries[6].get() != '' and my_entries[9].get() != '' and my_entries[12].get() != '' and my_entries[15].get() != '' and
         my_entries[18].get() != '' and my_entries[21].get() != '' and my_entries[24].get() != '' and my_entries[27].get() != '' and my_entries[30].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and my_entries[5].get() != '' and
           my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
           my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and
           my_entries[18].get() != '' and my_entries[19].get() != '' and my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
           my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and my_entries[28].get() != '' and my_entries[29].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[3].get()+"','"+my_entries[4].get()+"','"+my_entries[5].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[18].get()+"','"+my_entries[19].get()+"','"+my_entries[20].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"') VALUES ('"+my_entries[27].get()+"','"+my_entries[28].get()+"','"+my_entries[29].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)


def Checking_fields4():
    print("field 4")
    print(my_entries[0].get())
    if my_entries[0].get() != '' and my_entries[4].get() == '':
        if my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '':
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
           my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() != '' and my_entries[24].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() != '' and my_entries[24].get() != '' and my_entries[28].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
            my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() != '' and my_entries[24].get() != '' and my_entries[28].get() != '' and
          my_entries[32].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
            my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and
            my_entries[28].get() != '' and my_entries[29].get() != '' and my_entries[30].get() != '' and my_entries[31].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[28].get()+"','"+my_entries[29].get()+"','"+my_entries[30].get()+"','"+my_entries[31].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() != '' and my_entries[24].get() != '' and my_entries[28].get() != '' and
          my_entries[32].get() != '' and my_entries[36].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
            my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and
            my_entries[28].get() != '' and my_entries[29].get() != '' and my_entries[30].get() != '' and my_entries[31].get() != '' and
            my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != '' and my_entries[35].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[28].get()+"','"+my_entries[29].get()+"','"+my_entries[30].get()+"','"+my_entries[31].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"','"+my_entries[35].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() != '' and my_entries[24].get() != '' and my_entries[28].get() != '' and
          my_entries[32].get() != '' and my_entries[36].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
            my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and
            my_entries[28].get() != '' and my_entries[29].get() != '' and my_entries[30].get() != '' and my_entries[31].get() != '' and
            my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != '' and my_entries[35].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[28].get()+"','"+my_entries[29].get()+"','"+my_entries[30].get()+"','"+my_entries[31].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"','"+my_entries[35].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[4].get() != '' and my_entries[8].get() != '' and my_entries[12].get() == '' and
          my_entries[16].get() != '' and my_entries[20].get() != '' and my_entries[24].get() != '' and my_entries[28].get() != '' and
          my_entries[32].get() != '' and my_entries[36].get() != ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and
            my_entries[4].get() != '' and my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and
            my_entries[8].get() != '' and my_entries[9].get() != '' and my_entries[10].get() != '' and my_entries[11].get() != '' and
            my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and my_entries[15].get() != '' and
            my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and
            my_entries[24].get() != '' and my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and
            my_entries[28].get() != '' and my_entries[29].get() != '' and my_entries[30].get() != '' and my_entries[31].get() != '' and
            my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != '' and my_entries[35].get() != '' and
            my_entries[36].get() != '' and my_entries[37].get() != '' and my_entries[38].get() != '' and my_entries[39].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[4].get()+"','"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[8].get()+"','"+my_entries[9].get()+"','"+my_entries[10].get()+"','"+my_entries[11].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"','"+my_entries[15].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[24].get()+"','"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[28].get()+"','"+my_entries[29].get()+"','"+my_entries[30].get()+"','"+my_entries[31].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"','"+my_entries[35].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"') VALUES ('"+my_entries[36].get()+"','"+my_entries[37].get()+"','"+my_entries[38].get()+"','"+my_entries[39].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

def Checking_fields5():
    print("field 5")
    print(my_entries[0].get())
    if my_entries[0].get() != '' and my_entries[5].get() == '':
        if my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '':
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != ''
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() == '':
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() != '' and
          my_entries[25].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and my_entries[24].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"','"+my_entries[24].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() != '' and
          my_entries[25].get() != '' and my_entries[30].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and my_entries[24].get() != '' and
            my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and my_entries[28].get() != '' and my_entries[29].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"','"+my_entries[24].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"','"+my_entries[28].get()+"','"+my_entries[29].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() != '' and
          my_entries[25].get() != '' and my_entries[30].get() != '' and my_entries[35].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and my_entries[24].get() != '' and
            my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and my_entries[28].get() != '' and my_entries[29].get() != ''
            my_entries[30].get() != '' and my_entries[31].get() != '' and my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"','"+my_entries[24].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"','"+my_entries[28].get()+"','"+my_entries[29].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[30].get()+"','"+my_entries[31].get()+"','"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() != '' and
          my_entries[25].get() != '' and my_entries[30].get() != '' and my_entries[35].get() != '' and my_entries[40].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and my_entries[24].get() != '' and
            my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and my_entries[28].get() != '' and my_entries[29].get() != '' and
            my_entries[30].get() != '' and my_entries[31].get() != '' and my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != '' and
            my_entries[35].get() != '' and my_entries[36].get() != '' and my_entries[37].get() != '' and my_entries[38].get() != '' and my_entries[39].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"','"+my_entries[24].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"','"+my_entries[28].get()+"','"+my_entries[29].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[30].get()+"','"+my_entries[31].get()+"','"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[35].get()+"','"+my_entries[36].get()+"','"+my_entries[37].get()+"','"+my_entries[38].get()+"','"+my_entries[39].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() != '' and
          my_entries[25].get() != '' and my_entries[30].get() != '' and my_entries[35].get() != '' and my_entries[40].get() != '' and my_entries[45].get() == ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and my_entries[24].get() != '' and
            my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and my_entries[28].get() != '' and my_entries[29].get() != '' and
            my_entries[30].get() != '' and my_entries[31].get() != '' and my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != '' and
            my_entries[35].get() != '' and my_entries[36].get() != '' and my_entries[37].get() != '' and my_entries[38].get() != '' and my_entries[39].get() != '' and
            my_entries[40].get() != '' and my_entries[41].get() != '' and my_entries[42].get() != '' and my_entries[43].get() != '' and my_entries[44].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"','"+my_entries[24].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"','"+my_entries[28].get()+"','"+my_entries[29].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[30].get()+"','"+my_entries[31].get()+"','"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[35].get()+"','"+my_entries[36].get()+"','"+my_entries[37].get()+"','"+my_entries[38].get()+"','"+my_entries[39].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[40].get()+"','"+my_entries[41].get()+"','"+my_entries[42].get()+"','"+my_entries[43].get()+"','"+my_entries[44].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)

    elif (my_entries[0].get() != '' and my_entries[5].get() != '' and my_entries[10].get() != '' and my_entries[15].get() != '' and my_entries[20].get() != '' and
          my_entries[25].get() != '' and my_entries[30].get() != '' and my_entries[35].get() != '' and my_entries[40].get() != '' and my_entries[45].get() != ''):
        if (my_entries[0].get() != '' and my_entries[1].get() != '' and my_entries[2].get() != '' and my_entries[3].get() != '' and my_entries[4].get() != '' and
            my_entries[5].get() != '' and my_entries[6].get() != '' and my_entries[7].get() != '' and my_entries[8].get() != '' and my_entries[9].get() != '' and
            my_entries[10].get() != '' and my_entries[11].get() != '' and my_entries[12].get() != '' and my_entries[13].get() != '' and my_entries[14].get() != '' and
            my_entries[15].get() != '' and my_entries[16].get() != '' and my_entries[17].get() != '' and my_entries[18].get() != '' and my_entries[19].get() != '' and
            my_entries[20].get() != '' and my_entries[21].get() != '' and my_entries[22].get() != '' and my_entries[23].get() != '' and my_entries[24].get() != '' and
            my_entries[25].get() != '' and my_entries[26].get() != '' and my_entries[27].get() != '' and my_entries[28].get() != '' and my_entries[29].get() != '' and
            my_entries[30].get() != '' and my_entries[31].get() != '' and my_entries[32].get() != '' and my_entries[33].get() != '' and my_entries[34].get() != '' and
            my_entries[35].get() != '' and my_entries[36].get() != '' and my_entries[37].get() != '' and my_entries[38].get() != '' and my_entries[39].get() != '' and
            my_entries[40].get() != '' and my_entries[41].get() != '' and my_entries[42].get() != '' and my_entries[43].get() != '' and my_entries[44].get() != '' and
            my_entries[45].get() != '' and my_entries[46].get() != '' and my_entries[47].get() != '' and my_entries[48].get() != '' and my_entries[49].get() != ''):
            print("working")
            print("only one data is present inside")
            print("Table name is ",TABLE_NAME)
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            print("In the database")
            print("THe column list ", *col)
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[0].get()+"','"+my_entries[1].get()+"','"+my_entries[2].get()+"','"+my_entries[3].get()+"','"+my_entries[4].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[5].get()+"','"+my_entries[6].get()+"','"+my_entries[7].get()+"','"+my_entries[8].get()+"','"+my_entries[9].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[10].get()+"','"+my_entries[11].get()+"','"+my_entries[12].get()+"','"+my_entries[13].get()+"','"+my_entries[14].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[15].get()+"','"+my_entries[16].get()+"','"+my_entries[17].get()+"','"+my_entries[18].get()+"','"+my_entries[19].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[20].get()+"','"+my_entries[21].get()+"','"+my_entries[22].get()+"','"+my_entries[23].get()+"','"+my_entries[24].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[25].get()+"','"+my_entries[26].get()+"','"+my_entries[27].get()+"','"+my_entries[28].get()+"','"+my_entries[29].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[30].get()+"','"+my_entries[31].get()+"','"+my_entries[32].get()+"','"+my_entries[33].get()+"','"+my_entries[34].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[35].get()+"','"+my_entries[36].get()+"','"+my_entries[37].get()+"','"+my_entries[38].get()+"','"+my_entries[39].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[40].get()+"','"+my_entries[41].get()+"','"+my_entries[42].get()+"','"+my_entries[43].get()+"','"+my_entries[44].get()+"')")
            conn.commit()
            curs.execute("INSERT INTO '"+TABLE_NAME+"'('"+col[0]+"','"+col[1]+"','"+col[2]+"','"+col[3]+"','"+col[4]+"') VALUES ('"+my_entries[45].get()+"','"+my_entries[46].get()+"','"+my_entries[47].get()+"','"+my_entries[48].get()+"','"+my_entries[49].get()+"')")
            conn.commit()
            print("data inserted ")
            info2=conn.execute("SELECT * FROM %s" % (TABLE_NAME))
            for row in info2:  
                print(row)
            print("data displayed!")
            conn.close()
        else:
            messagebox.showerror("Error","Please Enter all the fields!",parent = second_frame)
