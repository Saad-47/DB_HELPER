from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
TABLE_NAME = ["--Select--","Integer","Text","Real","Blob"]
EXIST_TABLE_NAME = ["--Existing Tables--"]
conn = sqlite3.connect('manuf1.db')
curs=conn.cursor()
curs.execute('select name from sqlite_master where type= "table"')
table = curs.fetchall()
for i in table: 
    EXIST_TABLE_NAME.append(i)
 
def entry_fields(self):
    table_name=Label(self.root4,text=f"\tAttribute Name\t\t  Data type\t\t  Data Length\t\tN/N     PK      FK",font=("times new roman",13,"bold"),fg="black",bg="white")
    table_name.place(x=45,y=170)#.grid(row = 1,column = 0,pady = 10,padx = 10)
    #entry frame
    entry_frame = Frame(self.root4)
    entry_frame.place(x=45,y=200,width = 900, height = 270)
    #main frame
    main_frame = Frame(entry_frame,height = 500,width = 1350)
    main_frame.pack(fill = BOTH, expand = 1)#.grid(sticky = "news")#
    #canvas
    my_canvas = Canvas(main_frame,)
    my_canvas.pack(side = LEFT, fill=BOTH, expand =1)#.grid(row = 2, column = 0, pady = (5,0) ,sticky = "nw")#
    #scrollbar
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill=Y)#.grid(row = 0,column  =1,sticky = "ns")#
    #configure canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    #second frame inside canvas
    second_frame = Frame(my_canvas)
    #add new frame to window in a canvas
    my_canvas.create_window((0,0), window = second_frame, anchor = "nw")

    #Label(second_frame, text = f'0').grid(row = 1,column =0,pady = 10,padx = 10)
    for i in range(1,16):
        Label(second_frame, text = f'{i}').grid(row = i,column =0,pady = 10,padx = 10)

    self.text_attr1_num =Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr1_num.grid(row = 1,column = 1,pady = 10,padx = 10,sticky = "w")#.place(x= 45,y= 50,width=100,height=20)
    self.cmb_table1=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table1['values']= TABLE_NAME
    self.cmb_table1.grid(row = 1,column = 2,pady = 10,padx = 10,sticky = "w")#.place(x= 165,y= 50,width=100,height=20)
    self.cmb_table1.current(0)
    self.text_attr3_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr3_num.grid(row = 1,column =3,pady = 10,padx = 10)#.place(x= 285,y= 50,width=100,height=20)
    self.var1 = StringVar()
    self.cheoick1 = Checkbutton(second_frame,variable = self.var1, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check1.deselect()
    self.check1.grid(row = 1,column =4,pady = 10,padx = 10)#.place(x= 405,y= 50,width=50,height=20)
    self.var2 = StringVar()
    self.check2 = Checkbutton(second_frame,variable = self.var2, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check2.deselect()
    self.check2.grid(row = 1,column =5,pady = 10,padx = 10)#.place(x= 515,y= 50,width=50,height=20)
    self.var3 = StringVar()
    self.check3 = Checkbutton(second_frame,variable = self.var3, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check3.deselect()
    self.check3.grid(row = 1,column =6,pady = 10,padx = 10)#.place(x= 635,y= 50,width=50,height=20)
    self.text_attr4_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr4_num.grid(row = 2,column =1,pady = 10,padx = 10)#.place(x= 45,y= 80,width=100,height=20)
    self.cmb_table2=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table2['values']= TABLE_NAME
    self.cmb_table2.grid(row = 2,column =2,pady = 10,padx = 10)#.place(x= 165,y= 80,width=100,height=20)
    self.cmb_table2.current(0)
    self.text_attr6_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr6_num.grid(row = 2,column =3,pady = 10,padx = 10)#.place(x= 285,y= 80,width=100,height=20)
    self.var4 = StringVar()
    self.check4 = Checkbutton(second_frame,variable = self.var4, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check4.deselect()
    self.check4.grid(row = 2,column =4,pady = 10,padx = 10)#.place(x= 405,y= 80,width=50,height=20)
    self.var5 = StringVar()
    self.check5 = Checkbutton(second_frame,variable = self.var5, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check5.deselect()
    self.check5.grid(row = 2,column =5,pady = 10,padx = 10)#.place(x= 515,y= 80,width=50,height=20)
    self.var6 = StringVar()
    self.check6 = Checkbutton(second_frame,variable = self.var6, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check6.deselect()
    self.check6.grid(row = 2,column =6,pady = 10,padx = 10)#.place(x= 635,y= 80,width=50,height=20)
    self.text_attr7_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr7_num.grid(row = 3,column =1,pady = 10,padx = 10)#.place(x= 45,y= 110,width=100,height=20)
    self.cmb_table3=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table3['values']= TABLE_NAME
    self.cmb_table3.grid(row = 3,column =2,pady = 10,padx = 10)#.place(x= 165,y= 110,width=100,height=20)
    self.cmb_table3.current(0)
    self.text_attr9_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr9_num.grid(row = 3,column =3,pady = 10,padx = 10)#.place(x= 285,y= 110,width=100,height=20)
    self.var7 = StringVar()
    self.check7 = Checkbutton(second_frame,variable = self.var7, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check7.deselect()
    self.check7.grid(row = 3,column =4,pady = 10,padx = 10)#.place(x= 405,y= 110,width=50,height=20)
    self.var8 = StringVar()
    self.check8 = Checkbutton(second_frame,variable = self.var8, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check8.deselect()
    self.check8.grid(row = 3,column =5,pady = 10,padx = 10)#.place(x= 515,y= 110,width=50,height=20)
    self.var9 = StringVar()
    self.check9 = Checkbutton(second_frame,variable = self.var9, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check9.deselect()
    self.check9.grid(row = 3,column =6,pady = 10,padx = 10)#.place(x= 635,y= 110,width=50,height=20)
    self.text_attr10_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr10_num.grid(row = 4,column =1,pady = 10,padx = 10)#.place(x= 45,y= 140,width=100,height=20)
    self.cmb_table4=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table4['values']= TABLE_NAME
    self.cmb_table4.grid(row = 4,column =2,pady = 10,padx = 10)#.place(x= 165,y= 140,width=100,height=20)
    self.cmb_table4.current(0)
    self.text_attr12_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr12_num.grid(row = 4,column =3,pady = 10,padx = 10)#.place(x= 285,y= 140,width=100,height=20)
    self.var10 = StringVar()
    self.check10 = Checkbutton(second_frame,variable = self.var10, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check10.deselect()
    self.check10.grid(row = 4,column =4,pady = 10,padx = 10)#.place(x= 405,y= 140,width=50,height=20)
    self.var11 = StringVar()
    self.check11 = Checkbutton(second_frame,variable = self.var11, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check11.deselect()
    self.check11.grid(row = 4,column =5,pady = 10,padx = 10)#.place(x= 515,y= 140,width=50,height=20)
    self.var12 = StringVar()
    self.check12 = Checkbutton(second_frame,variable = self.var12, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check12.deselect()
    self.check12.grid(row = 4,column =6,pady = 10,padx = 10)#.place(x= 635,y= 140,width=50,height=20)
    self.text_attr13_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr13_num.grid(row = 5,column =1,pady = 10,padx = 10)#.place(x= 45,y= 170,width=100,height=20)
    self.cmb_table5=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table5['values']= TABLE_NAME
    self.cmb_table5.grid(row = 5,column =2,pady = 10,padx = 10)#.place(x= 165,y= 170,width=100,height=20)
    self.cmb_table5.current(0)
    self.text_attr15_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr15_num.grid(row = 5,column =3,pady = 10,padx = 10)#.place(x= 285,y= 170,width=100,height=20)
    self.var13 = StringVar()
    self.check13 = Checkbutton(second_frame,variable = self.var13, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check13.deselect()
    self.check13.grid(row = 5,column =4,pady = 10,padx = 10)#.place(x= 405,y= 170,width=50,height=20)
    self.var14 = StringVar()
    self.check14 = Checkbutton(second_frame,variable = self.var14, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check14.deselect()
    self.check14.grid(row = 5,column =5,pady = 10,padx = 10)#.place(x= 515,y= 170,width=50,height=20)
    self.var15 = StringVar()
    self.check15 = Checkbutton(second_frame,variable = self.var15, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check15.deselect()
    self.check15.grid(row = 5,column =6,pady = 10,padx = 10)#.place(x= 635,y= 170,width=50,height=20)
    self.text_attr16_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr16_num.grid(row = 6,column =1,pady = 10,padx = 10)#.place(x= 45,y= 200,width=100,height=20)
    self.cmb_table6=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table6['values']= TABLE_NAME
    self.cmb_table6.grid(row = 6,column =2,pady = 10,padx = 10)#.place(x= 165,y= 200,width=100,height=20)
    self.cmb_table6.current(0)
    self.text_attr18_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr18_num.grid(row = 6,column =3,pady = 10,padx = 10)#.place(x= 285,y= 200,width=100,height=20)
    self.var16 = StringVar()
    self.check16 = Checkbutton(second_frame,variable = self.var16, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check16.deselect()
    self.check16.grid(row = 6,column =4,pady = 10,padx = 10)#.place(x= 405,y= 200,width=50,height=20)
    self.var17 = StringVar()
    self.check17 = Checkbutton(second_frame,variable = self.var17, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check17.deselect()
    self.check17.grid(row = 6,column =5,pady = 10,padx = 10)#.place(x= 515,y= 200,width=50,height=20)
    self.var18 = StringVar()
    self.check18 = Checkbutton(second_frame,variable = self.var18, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check18.deselect()
    self.check18.grid(row = 6,column =6,pady = 10,padx = 10)#.place(x= 635,y= 200,width=50,height=20)
    self.text_attr19_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr19_num.grid(row = 7,column =1,pady = 10,padx = 10)#.place(x= 45,y= 230,width=100,height=20)
    self.cmb_table7=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table7['values']= TABLE_NAME
    self.cmb_table7.grid(row = 7,column =2,pady = 10,padx = 10)#.place(x= 165,y= 230,width=100,height=20)
    self.cmb_table7.current(0)
    self.text_attr21_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr21_num.grid(row = 7,column =3,pady = 10,padx = 10)#.place(x= 285,y= 230,width=100,height=20)
    self.var19 = StringVar()
    self.check19 = Checkbutton(second_frame,variable = self.var19, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check19.deselect()
    self.check19.grid(row = 7,column =4,pady = 10,padx = 10)#.place(x= 405,y= 230,width=50,height=20)
    self.var20 = StringVar()
    self.check20 = Checkbutton(second_frame,variable = self.var20, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check20.deselect()
    self.check20.grid(row = 7,column =5,pady = 10,padx = 10)#.place(x= 515,y= 230,width=50,height=20)
    self.var21 = StringVar()
    self.check21 = Checkbutton(second_frame,variable = self.var21, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check21.deselect()
    self.check21.grid(row = 7,column =6,pady = 10,padx = 10)#.place(x= 635,y= 230,width=50,height=20)
    self.text_attr22_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr22_num.grid(row = 8,column =1,pady = 10,padx = 10)#.place(x= 45,y= 260,width=100,height=20)
    self.cmb_table8=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table8['values']= TABLE_NAME
    self.cmb_table8.grid(row = 8,column =2,pady = 10,padx = 10)#.place(x= 165,y= 260,width=100,height=20)
    self.cmb_table8.current(0)
    self.text_attr24_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr24_num.grid(row = 8,column =3,pady = 10,padx = 10)#.place(x= 285,y= 260,width=100,height=20)
    self.var22 = StringVar()
    self.check22 = Checkbutton(second_frame,variable = self.var22, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check22.deselect()
    self.check22.grid(row = 8,column =4,pady = 10,padx = 10)#.place(x= 405,y= 260,width=50,height=20)
    self.var23 = StringVar()
    self.check23 = Checkbutton(second_frame,variable = self.var23, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check23.deselect()
    self.check23.grid(row = 8,column =5,pady = 10,padx = 10)#.place(x= 515,y= 260,width=50,height=20)
    self.var24 = StringVar()
    self.check24 = Checkbutton(second_frame,variable = self.var24, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check24.deselect()
    self.check24.grid(row = 8,column =6,pady = 10,padx = 10)#.place(x= 635,y= 260,width=50,height=20)
    self.text_attr25_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr25_num.grid(row = 9,column =1,pady = 10,padx = 10)#.place(x= 45,y= 290,width=100,height=20)
    self.cmb_table9=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table9['values']= TABLE_NAME
    self.cmb_table9.grid(row = 9,column =2,pady = 10,padx = 10)#.place(x= 165,y= 290,width=100,height=20)
    self.cmb_table9.current(0)
    self.text_attr27_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr27_num.grid(row = 9,column =3,pady = 10,padx = 10)#.place(x= 285,y= 290,width=100,height=20)
    self.var25 = StringVar()
    self.check25 = Checkbutton(second_frame,variable = self.var25, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check25.deselect()
    self.check25.grid(row = 9,column =4,pady = 10,padx = 10)#.place(x= 405,y= 290,width=50,height=20)
    self.var26 = StringVar()
    self.check26 = Checkbutton(second_frame,variable = self.var26, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check26.deselect()
    self.check26.grid(row = 9,column =5,pady = 10,padx = 10)#.place(x= 515,y= 290,width=50,height=20)
    self.var27 = StringVar()
    self.check27 = Checkbutton(second_frame,variable = self.var27, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check27.deselect()
    self.check27.grid(row = 9,column =6,pady = 10,padx = 10)#.place(x= 635,y= 290,width=50,height=20)
    self.text_attr28_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr28_num.grid(row = 10,column =1,pady = 10,padx = 10)#.place(x= 45,y= 320,width=100,height=20)
    self.cmb_table10=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table10['values']= TABLE_NAME
    self.cmb_table10.grid(row = 10,column =2,pady = 10,padx = 10)#.place(x= 165,y= 320,width=100,height=20)
    self.cmb_table10.current(0)
    self.text_attr30_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr30_num.grid(row = 10,column =3,pady = 10,padx = 10)#.place(x= 285,y= 320,width=100,height=20)
    self.var28 = StringVar()
    self.check28 = Checkbutton(second_frame,variable = self.var28, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check28.deselect()
    self.check28.grid(row = 10,column =4,pady = 10,padx = 10)#.place(x= 405,y= 320,width=50,height=20)
    self.var29 = StringVar()
    self.check29 = Checkbutton(second_frame,variable = self.var29, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check29.deselect()
    self.check29.grid(row = 10,column =5,pady = 10,padx = 10)#.place(x= 515,y= 320,width=50,height=20)
    self.var30 = StringVar()
    self.check30 = Checkbutton(second_frame,variable = self.var30, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check30.deselect()
    self.check30.grid(row = 10,column =6,pady = 10,padx = 10)#.place(x= 635,y= 320,width=50,height=20)
    self.text_attr31_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr31_num.grid(row = 11,column =1,pady = 10,padx = 10)#.place(x= 45,y= 350,width=100,height=20)
    self.cmb_table11=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table11['values']= TABLE_NAME
    self.cmb_table11.grid(row = 11,column =2,pady = 10,padx = 10)#.place(x= 165,y= 350,width=100,height=20)
    self.cmb_table11.current(0)
    self.text_attr33_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr33_num.grid(row = 11,column =3,pady = 10,padx = 10)#.place(x= 285,y= 350,width=100,height=20)
    self.var31 = StringVar()
    self.check31 = Checkbutton(second_frame,variable = self.var31, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check31.deselect()
    self.check31.grid(row = 11,column =4,pady = 10,padx = 10)#.place(x= 405,y= 350,width=50,height=20)
    self.var32 = StringVar()
    self.check32 = Checkbutton(second_frame,variable = self.var32, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check32.deselect()
    self.check32.grid(row = 11,column =5,pady = 10,padx = 10)#.place(x= 515,y= 350,width=50,height=20)
    self.var33 = StringVar()
    self.check33 = Checkbutton(second_frame,variable = self.var33, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check33.deselect()
    self.check33.grid(row = 11,column =6,pady = 10,padx = 10)#.place(x= 635,y= 350,width=50,height=20)
    self.text_attr34_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr34_num.grid(row = 12,column =1,pady = 10,padx = 10)#.place(x= 45,y= 380,width=100,height=20)
    self.cmb_table12=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table12['values']= TABLE_NAME
    self.cmb_table12.grid(row = 12,column =2,pady = 10,padx = 10)#.place(x= 165,y= 380,width=100,height=20)
    self.cmb_table12.current(0)
    self.text_attr36_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr36_num.grid(row = 12,column =3,pady = 10,padx = 10)#.place(x= 285,y= 380,width=100,height=20)
    self.var34 = StringVar()
    self.check34 = Checkbutton(second_frame,variable = self.var34, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check34.deselect()
    self.check34.grid(row = 12,column =4,pady = 10,padx = 10)#.place(x= 405,y= 380,width=50,height=20)
    self.var35 = StringVar()
    self.check35 = Checkbutton(second_frame,variable = self.var35, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check35.deselect()
    self.check35.grid(row = 12,column =5,pady = 10,padx = 10)#.place(x= 515,y= 380,width=50,height=20)
    self.var36 = StringVar()
    self.check36 = Checkbutton(second_frame,variable = self.var36, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check36.deselect()
    self.check36.grid(row = 12,column =6,pady = 10,padx = 10)#.place(x= 635,y= 380,width=50,height=20)
    self.text_attr37_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr37_num.grid(row = 13,column =1,pady = 10,padx = 10)#.place(x= 45,y= 410,width=100,height=20)
    self.cmb_table13=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table13['values']= TABLE_NAME
    self.cmb_table13.grid(row = 13,column =2,pady = 10,padx = 10)#.place(x= 165,y= 410,width=100,height=20)
    self.cmb_table13.current(0)
    self.text_attr39_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr39_num.grid(row = 13,column =3,pady = 10,padx = 10)#.place(x= 285,y= 410,width=100,height=20)
    self.var37 = StringVar()
    self.check37 = Checkbutton(second_frame,variable = self.var37, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check37.deselect()
    self.check37.grid(row = 13,column =4,pady = 10,padx = 10)#.place(x= 405,y= 410,width=50,height=20)
    self.var38 = StringVar()
    self.check38 = Checkbutton(second_frame,variable = self.var38, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check38.deselect()
    self.check38.grid(row = 13,column =5,pady = 10,padx = 10)#.place(x= 515,y= 410,width=50,height=20)
    self.var39 = StringVar()
    self.check39 = Checkbutton(second_frame,variable = self.var39, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check39.deselect()
    self.check39.grid(row = 13,column =6,pady = 10,padx = 10)#.place(x= 635,y= 410,width=50,height=20)
    self.text_attr40_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr40_num.grid(row = 14,column =1,pady = 10,padx = 10)#.place(x= 45,y= 440,width=100,height=20)
    self.cmb_table14=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table14['values']= TABLE_NAME
    self.cmb_table14.grid(row = 14,column =2,pady = 10,padx = 10)#.place(x= 165,y= 440,width=100,height=20)
    self.cmb_table14.current(0)
    self.text_attr42_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr42_num.grid(row = 14,column =3,pady = 10,padx = 10)#.place(x= 285,y= 440,width=100,height=20)
    self.var40 = StringVar()
    self.check40 = Checkbutton(second_frame,variable = self.var40, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check40.deselect()
    self.check40.grid(row = 14,column =4,pady = 10,padx = 10)#.place(x= 405,y= 440,width=50,height=20)
    self.var41 = StringVar()
    self.check41 = Checkbutton(second_frame,variable = self.var41, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check41.deselect()
    self.check41.grid(row = 14,column =5,pady = 10,padx = 10)#.place(x= 515,y= 440,width=50,height=20)
    self.var42 = StringVar()
    self.check42 = Checkbutton(second_frame,variable = self.var42, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check42.deselect()
    self.check42.grid(row = 14,column =6,pady = 10,padx = 10)#.place(x= 635,y= 440,width=50,height=20)
    self.text_attr43_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr43_num.grid(row = 15,column =1,pady = 10,padx = 10)#.place(x= 45,y= 470,width=100,height=20)
    self.cmb_table15=ttk.Combobox(second_frame,font=("times new roman",13),state='readonly',justify=CENTER)
    self.cmb_table15['values']= TABLE_NAME
    self.cmb_table15.grid(row = 15,column =2,pady = 10,padx = 10)#.place(x= 165,y= 470,width=100,height=20)
    self.cmb_table15.current(0)
    self.text_attr45_num=Entry(second_frame,font=("times new roman",15),bg="white")
    self.text_attr45_num.grid(row = 15,column =3,pady = 10,padx = 10)#.place(x= 285,y= 470,width=100,height=20)
    self.var43 = StringVar()
    self.check43 = Checkbutton(second_frame,variable = self.var43, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check43.deselect()
    self.check43.grid(row = 15,column =4,pady = 10,padx = 10)#.place(x= 405,y= 470,width=50,height=20)
    self.var44 = StringVar()
    self.check44 = Checkbutton(second_frame,variable = self.var44, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check44.deselect()
    self.check44.grid(row = 15,column =5,pady = 10,padx = 10)#.place(x= 515,y= 470,width=50,height=20)
    self.var45 = StringVar()
    self.check45 = Checkbutton(second_frame,variable = self.var45, onvalue = "Yes", offvalue = "No")#box_var[box_num]
    self.check45.deselect()
    self.check45.grid(row = 15,column =6,pady = 10,padx = 10)#.place(x= 635,y= 470,width=50,height=20)

    btn_back= Button(self.root4,text = "BACK",bg="green",fg="white",command = self.back,cursor = "hand2",font=("times new roman",10,"bold")).place(x = 235 ,y= 490)
    btn_cancel= Button(self.root4,text = "CANCEL",bg="green",fg="white",command = self.cancel,cursor = "hand2",font=("times new roman",10,"bold")).place(x=435 ,y= 490)
    btn_Create_Table= Button(self.root4,text = "CREATE TABLE",bg="green",fg="white",command = self.Selector_Save,cursor = "hand2",font=("times new roman",10,"bold")).place(x=635 ,y= 490)

def ALLSave_table(self):
    if (self.text_attr1_num.get() != "" and self.text_attr4_num.get() == ""):
        self.text_attr_num = "1"
        print("ALLSAVE TABLE")
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() == ""):
        self.text_attr_num = "2"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != "" and self.text_attr10_num.get() == ""):
        self.text_attr_num = "3"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != "" and self.text_attr10_num.get() != "" and self.text_attr13_num.get() == ""):
        self.text_attr_num = "4"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() == ""):
        self.text_attr_num = "5"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != "" and self.text_attr19_num.get() == ""):
        self.text_attr_num = "6"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != "" and self.text_attr19_num.get() != "" and self.text_attr22_num.get() == ""):
        self.text_attr_num = "7"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() == ""):
        self.text_attr_num = "8"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() == ""):
        self.text_attr_num = "9"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() != "" and self.text_attr31_num.get() == ""):
        self.text_attr_num = "10"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() != "" and self.text_attr31_num.get() != "" and self.text_attr34_num.get() == ""):
        self.text_attr_num = "11"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() != ""
          and self.text_attr31_num.get() != "" and self.text_attr34_num.get() != "" and self.text_attr37_num.get() == ""):
        self.text_attr_num = "12"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() != ""
          and self.text_attr31_num.get() != "" and self.text_attr34_num.get() != "" and self.text_attr37_num.get() != "" and self.text_attr40_num.get() == ""):
        self.text_attr_num = "13"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() != ""
          and self.text_attr31_num.get() != "" and self.text_attr34_num.get() != "" and self.text_attr37_num.get() != "" and self.text_attr40_num.get() != "" and self.text_attr43_num.get() == ""):
        self.text_attr_num = "14"
        self.Selector_Save
    elif (self.text_attr1_num.get() != "" and self.text_attr4_num.get() != "" and self.text_attr7_num.get() != ""
          and self.text_attr10_num.get() != "" and self.text_attr13_num.get() != "" and self.text_attr16_num.get() != ""
          and self.text_attr19_num.get() != "" and self.text_attr22_num.get() != "" and self.text_attr25_num.get() != "" and self.text_attr28_num.get() != ""
          and self.text_attr31_num.get() != "" and self.text_attr34_num.get() != "" and self.text_attr37_num.get() != "" and self.text_attr40_num.get() != "" and self.text_attr43_num.get() != ""):
        self.text_attr_num = "15"
        self.Selector_Save
        
def Save_table1(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            table_name = self.text_table_name.get()
            column1 = self.text_attr1_num.get()
            print(self.var1.get())
            curs.execute('create table %s(%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)

def Save_table2(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table2.get() == "" or self.text_attr6_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var3.get() == "Yes" and self.var6.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s)not null,%s %s(%s)not null)' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)

def Save_table3(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table2.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)

def Save_table4(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table2.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)


def Save_table5(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table2.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")  
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)

def Save_table6(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")  
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)

def Save_table7(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")  
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)

def Save_table8(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")  
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)

def Save_table9(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")  
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)

def Save_table10(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""
              or self.text_attr28_num.get() == "" or self.cmb_table10.get() == "" or self.text_attr30_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var26.get() == "Yes") or (self.var5.get() == "Yes" and self.var26.get() == "Yes") or (self.var8.get() == "Yes" and self.var26.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var26.get() == "Yes") or (self.var14.get() == "Yes" and self.var26.get() == "Yes")or (self.var17.get() == "Yes" and self.var26.get() == "Yes")or (self.var20.get() == "Yes" and self.var26.get() == "Yes")or (self.var23.get() == "Yes" and self.var26.get() == "Yes")  
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var27.get() == "Yes") or (self.var6.get() == "Yes" and self.var27.get() == "Yes") or (self.var9.get() == "Yes" and self.var27.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var27.get() == "Yes") or (self.var15.get() == "Yes" and self.var27.get() == "Yes") or (self.var18.get() == "Yes" and self.var27.get() == "Yes") or (self.var21.get() == "Yes" and self.var27.get() == "Yes") or (self.var24.get() == "Yes" and self.var27.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get(),self.text_attr28_num.get(),self.cmb_table10.get(),self.text_attr30_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)
            self.text_attr28_num.delete(0,END)
            self.cmb_table10.delete(0,END)
            self.text_attr30_num.delete(0,END)
        

def Save_table11(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""
              or self.text_attr28_num.get() == "" or self.cmb_table10.get() == "" or self.text_attr30_num.get() == ""
              or self.text_attr31_num.get() == "" or self.cmb_table11.get() == "" or self.text_attr33_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var26.get() == "Yes") or (self.var5.get() == "Yes" and self.var26.get() == "Yes") or (self.var8.get() == "Yes" and self.var26.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var26.get() == "Yes") or (self.var14.get() == "Yes" and self.var26.get() == "Yes")or (self.var17.get() == "Yes" and self.var26.get() == "Yes")or (self.var20.get() == "Yes" and self.var26.get() == "Yes")or (self.var23.get() == "Yes" and self.var26.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var29.get() == "Yes") or (self.var5.get() == "Yes" and self.var29.get() == "Yes") or (self.var8.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var29.get() == "Yes") or (self.var14.get() == "Yes" and self.var29.get() == "Yes")or (self.var17.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var29.get() == "Yes")or (self.var23.get() == "Yes" and self.var29.get() == "Yes")or (self.var26.get() == "Yes" and self.var29.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var27.get() == "Yes") or (self.var6.get() == "Yes" and self.var27.get() == "Yes") or (self.var9.get() == "Yes" and self.var27.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var27.get() == "Yes") or (self.var15.get() == "Yes" and self.var27.get() == "Yes") or (self.var18.get() == "Yes" and self.var27.get() == "Yes") or (self.var21.get() == "Yes" and self.var27.get() == "Yes") or (self.var24.get() == "Yes" and self.var27.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var30.get() == "Yes") or (self.var6.get() == "Yes" and self.var30.get() == "Yes") or (self.var9.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var30.get() == "Yes") or (self.var15.get() == "Yes" and self.var30.get() == "Yes") or (self.var18.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var30.get() == "Yes") or (self.var24.get() == "Yes" and self.var30.get() == "Yes") or (self.var27.get() == "Yes" and self.var30.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get(),self.text_attr28_num.get(),self.cmb_table10.get(),self.text_attr30_num.get(),self.text_attr31_num.get(),self.cmb_table11.get(),self.text_attr33_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)
            self.text_attr28_num.delete(0,END)
            self.cmb_table10.delete(0,END)
            self.text_attr30_num.delete(0,END)
            self.text_attr31_num.delete(0,END)
            self.cmb_table11.delete(0,END)
            self.text_attr33_num.delete(0,END)

def Save_table12(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""
              or self.text_attr28_num.get() == "" or self.cmb_table10.get() == "" or self.text_attr30_num.get() == ""
              or self.text_attr31_num.get() == "" or self.cmb_table11.get() == "" or self.text_attr33_num.get() == ""
              or self.text_attr34_num.get() == "" or self.cmb_table12.get() == "" or self.text_attr36_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var26.get() == "Yes") or (self.var5.get() == "Yes" and self.var26.get() == "Yes") or (self.var8.get() == "Yes" and self.var26.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var26.get() == "Yes") or (self.var14.get() == "Yes" and self.var26.get() == "Yes")or (self.var17.get() == "Yes" and self.var26.get() == "Yes")or (self.var20.get() == "Yes" and self.var26.get() == "Yes")or (self.var23.get() == "Yes" and self.var26.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var29.get() == "Yes") or (self.var5.get() == "Yes" and self.var29.get() == "Yes") or (self.var8.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var29.get() == "Yes") or (self.var14.get() == "Yes" and self.var29.get() == "Yes")or (self.var17.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var29.get() == "Yes")or (self.var23.get() == "Yes" and self.var29.get() == "Yes")or (self.var26.get() == "Yes" and self.var29.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var32.get() == "Yes") or (self.var5.get() == "Yes" and self.var32.get() == "Yes") or (self.var8.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var32.get() == "Yes") or (self.var14.get() == "Yes" and self.var32.get() == "Yes")or (self.var17.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var32.get() == "Yes")or (self.var23.get() == "Yes" and self.var32.get() == "Yes")or (self.var26.get() == "Yes" and self.var32.get() == "Yes")or (self.var29.get() == "Yes" and self.var32.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var27.get() == "Yes") or (self.var6.get() == "Yes" and self.var27.get() == "Yes") or (self.var9.get() == "Yes" and self.var27.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var27.get() == "Yes") or (self.var15.get() == "Yes" and self.var27.get() == "Yes") or (self.var18.get() == "Yes" and self.var27.get() == "Yes") or (self.var21.get() == "Yes" and self.var27.get() == "Yes") or (self.var24.get() == "Yes" and self.var27.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var30.get() == "Yes") or (self.var6.get() == "Yes" and self.var30.get() == "Yes") or (self.var9.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var30.get() == "Yes") or (self.var15.get() == "Yes" and self.var30.get() == "Yes") or (self.var18.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var30.get() == "Yes") or (self.var24.get() == "Yes" and self.var30.get() == "Yes") or (self.var27.get() == "Yes" and self.var30.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var33.get() == "Yes") or (self.var6.get() == "Yes" and self.var33.get() == "Yes") or (self.var9.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var33.get() == "Yes") or (self.var15.get() == "Yes" and self.var33.get() == "Yes") or (self.var18.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var33.get() == "Yes") or (self.var24.get() == "Yes" and self.var33.get() == "Yes") or (self.var27.get() == "Yes" and self.var33.get() == "Yes") or (self.var30.get() == "Yes" and self.var33.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get(),self.text_attr28_num.get(),self.cmb_table10.get(),self.text_attr30_num.get(),self.text_attr31_num.get(),self.cmb_table11.get(),self.text_attr33_num.get(),self.text_attr34_num.get(),self.cmb_table12.get(),self.text_attr36_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)
            self.text_attr28_num.delete(0,END)
            self.cmb_table10.delete(0,END)
            self.text_attr30_num.delete(0,END)
            self.text_attr31_num.delete(0,END)
            self.cmb_table11.delete(0,END)
            self.text_attr33_num.delete(0,END)
            self.text_attr34_num.delete(0,END)
            self.cmb_table12.delete(0,END)
            self.text_attr36_num.delete(0,END)

def Save_table13(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""
              or self.text_attr28_num.get() == "" or self.cmb_table10.get() == "" or self.text_attr30_num.get() == ""
              or self.text_attr31_num.get() == "" or self.cmb_table11.get() == "" or self.text_attr33_num.get() == ""
              or self.text_attr34_num.get() == "" or self.cmb_table12.get() == "" or self.text_attr36_num.get() == ""
              or self.text_attr37_num.get() == "" or self.cmb_table13.get() == "" or self.text_attr39_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var26.get() == "Yes") or (self.var5.get() == "Yes" and self.var26.get() == "Yes") or (self.var8.get() == "Yes" and self.var26.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var26.get() == "Yes") or (self.var14.get() == "Yes" and self.var26.get() == "Yes")or (self.var17.get() == "Yes" and self.var26.get() == "Yes")or (self.var20.get() == "Yes" and self.var26.get() == "Yes")or (self.var23.get() == "Yes" and self.var26.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var29.get() == "Yes") or (self.var5.get() == "Yes" and self.var29.get() == "Yes") or (self.var8.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var29.get() == "Yes") or (self.var14.get() == "Yes" and self.var29.get() == "Yes")or (self.var17.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var29.get() == "Yes")or (self.var23.get() == "Yes" and self.var29.get() == "Yes")or (self.var26.get() == "Yes" and self.var29.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var32.get() == "Yes") or (self.var5.get() == "Yes" and self.var32.get() == "Yes") or (self.var8.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var32.get() == "Yes") or (self.var14.get() == "Yes" and self.var32.get() == "Yes")or (self.var17.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var32.get() == "Yes")or (self.var23.get() == "Yes" and self.var32.get() == "Yes")or (self.var26.get() == "Yes" and self.var32.get() == "Yes")or (self.var29.get() == "Yes" and self.var32.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var35.get() == "Yes") or (self.var5.get() == "Yes" and self.var35.get() == "Yes") or (self.var8.get() == "Yes" and self.var35.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var35.get() == "Yes") or (self.var14.get() == "Yes" and self.var35.get() == "Yes")or (self.var17.get() == "Yes" and self.var35.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var35.get() == "Yes")or (self.var23.get() == "Yes" and self.var35.get() == "Yes")or (self.var26.get() == "Yes" and self.var35.get() == "Yes")or (self.var29.get() == "Yes" and self.var35.get() == "Yes")or (self.var32.get() == "Yes" and self.var35.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var27.get() == "Yes") or (self.var6.get() == "Yes" and self.var27.get() == "Yes") or (self.var9.get() == "Yes" and self.var27.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var27.get() == "Yes") or (self.var15.get() == "Yes" and self.var27.get() == "Yes") or (self.var18.get() == "Yes" and self.var27.get() == "Yes") or (self.var21.get() == "Yes" and self.var27.get() == "Yes") or (self.var24.get() == "Yes" and self.var27.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var30.get() == "Yes") or (self.var6.get() == "Yes" and self.var30.get() == "Yes") or (self.var9.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var30.get() == "Yes") or (self.var15.get() == "Yes" and self.var30.get() == "Yes") or (self.var18.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var30.get() == "Yes") or (self.var24.get() == "Yes" and self.var30.get() == "Yes") or (self.var27.get() == "Yes" and self.var30.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var33.get() == "Yes") or (self.var6.get() == "Yes" and self.var33.get() == "Yes") or (self.var9.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var33.get() == "Yes") or (self.var15.get() == "Yes" and self.var33.get() == "Yes") or (self.var18.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var33.get() == "Yes") or (self.var24.get() == "Yes" and self.var33.get() == "Yes") or (self.var27.get() == "Yes" and self.var33.get() == "Yes") or (self.var30.get() == "Yes" and self.var33.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var36.get() == "Yes") or (self.var6.get() == "Yes" and self.var36.get() == "Yes") or (self.var9.get() == "Yes" and self.var36.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var36.get() == "Yes") or (self.var15.get() == "Yes" and self.var36.get() == "Yes") or (self.var18.get() == "Yes" and self.var36.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var36.get() == "Yes") or (self.var24.get() == "Yes" and self.var36.get() == "Yes") or (self.var27.get() == "Yes" and self.var36.get() == "Yes") or (self.var30.get() == "Yes" and self.var36.get() == "Yes") or (self.var33.get() == "Yes" and self.var36.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get(),self.text_attr28_num.get(),self.cmb_table10.get(),self.text_attr30_num.get(),self.text_attr31_num.get(),self.cmb_table11.get(),self.text_attr33_num.get(),self.text_attr34_num.get(),self.cmb_table12.get(),self.text_attr36_num.get(),self.text_attr37_num.get(),self.cmb_table13.get(),self.text_attr39_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)
            self.text_attr28_num.delete(0,END)
            self.cmb_table10.delete(0,END)
            self.text_attr30_num.delete(0,END)
            self.text_attr31_num.delete(0,END)
            self.cmb_table11.delete(0,END)
            self.text_attr33_num.delete(0,END)
            self.text_attr34_num.delete(0,END)
            self.cmb_table12.delete(0,END)
            self.text_attr36_num.delete(0,END)
            self.text_attr37_num.delete(0,END)
            self.cmb_table13.delete(0,END)
            self.text_attr39_num.delete(0,END)


def Save_table14(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""
              or self.text_attr28_num.get() == "" or self.cmb_table10.get() == "" or self.text_attr30_num.get() == ""
              or self.text_attr31_num.get() == "" or self.cmb_table11.get() == "" or self.text_attr33_num.get() == ""
              or self.text_attr34_num.get() == "" or self.cmb_table12.get() == "" or self.text_attr36_num.get() == ""
              or self.text_attr37_num.get() == "" or self.cmb_table13.get() == "" or self.text_attr39_num.get() == ""
              or self.text_attr40_num.get() == "" or self.cmb_table14.get() == "" or self.text_attr42_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var26.get() == "Yes") or (self.var5.get() == "Yes" and self.var26.get() == "Yes") or (self.var8.get() == "Yes" and self.var26.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var26.get() == "Yes") or (self.var14.get() == "Yes" and self.var26.get() == "Yes")or (self.var17.get() == "Yes" and self.var26.get() == "Yes")or (self.var20.get() == "Yes" and self.var26.get() == "Yes")or (self.var23.get() == "Yes" and self.var26.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var29.get() == "Yes") or (self.var5.get() == "Yes" and self.var29.get() == "Yes") or (self.var8.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var29.get() == "Yes") or (self.var14.get() == "Yes" and self.var29.get() == "Yes")or (self.var17.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var29.get() == "Yes")or (self.var23.get() == "Yes" and self.var29.get() == "Yes")or (self.var26.get() == "Yes" and self.var29.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var32.get() == "Yes") or (self.var5.get() == "Yes" and self.var32.get() == "Yes") or (self.var8.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var32.get() == "Yes") or (self.var14.get() == "Yes" and self.var32.get() == "Yes")or (self.var17.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var32.get() == "Yes")or (self.var23.get() == "Yes" and self.var32.get() == "Yes")or (self.var26.get() == "Yes" and self.var32.get() == "Yes")or (self.var29.get() == "Yes" and self.var32.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var35.get() == "Yes") or (self.var5.get() == "Yes" and self.var35.get() == "Yes") or (self.var8.get() == "Yes" and self.var35.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var35.get() == "Yes") or (self.var14.get() == "Yes" and self.var35.get() == "Yes")or (self.var17.get() == "Yes" and self.var35.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var35.get() == "Yes")or (self.var23.get() == "Yes" and self.var35.get() == "Yes")or (self.var26.get() == "Yes" and self.var35.get() == "Yes")or (self.var29.get() == "Yes" and self.var35.get() == "Yes")or (self.var32.get() == "Yes" and self.var35.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var38.get() == "Yes") or (self.var5.get() == "Yes" and self.var38.get() == "Yes") or (self.var8.get() == "Yes" and self.var38.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var38.get() == "Yes") or (self.var14.get() == "Yes" and self.var38.get() == "Yes")or (self.var17.get() == "Yes" and self.var38.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var38.get() == "Yes")or (self.var23.get() == "Yes" and self.var38.get() == "Yes")or (self.var26.get() == "Yes" and self.var38.get() == "Yes")
            or (self.var29.get() == "Yes" and self.var38.get() == "Yes")or (self.var32.get() == "Yes" and self.var38.get() == "Yes")or (self.var35.get() == "Yes" and self.var38.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var27.get() == "Yes") or (self.var6.get() == "Yes" and self.var27.get() == "Yes") or (self.var9.get() == "Yes" and self.var27.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var27.get() == "Yes") or (self.var15.get() == "Yes" and self.var27.get() == "Yes") or (self.var18.get() == "Yes" and self.var27.get() == "Yes") or (self.var21.get() == "Yes" and self.var27.get() == "Yes") or (self.var24.get() == "Yes" and self.var27.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var30.get() == "Yes") or (self.var6.get() == "Yes" and self.var30.get() == "Yes") or (self.var9.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var30.get() == "Yes") or (self.var15.get() == "Yes" and self.var30.get() == "Yes") or (self.var18.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var30.get() == "Yes") or (self.var24.get() == "Yes" and self.var30.get() == "Yes") or (self.var27.get() == "Yes" and self.var30.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var33.get() == "Yes") or (self.var6.get() == "Yes" and self.var33.get() == "Yes") or (self.var9.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var33.get() == "Yes") or (self.var15.get() == "Yes" and self.var33.get() == "Yes") or (self.var18.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var33.get() == "Yes") or (self.var24.get() == "Yes" and self.var33.get() == "Yes") or (self.var27.get() == "Yes" and self.var33.get() == "Yes") or (self.var30.get() == "Yes" and self.var33.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var36.get() == "Yes") or (self.var6.get() == "Yes" and self.var36.get() == "Yes") or (self.var9.get() == "Yes" and self.var36.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var36.get() == "Yes") or (self.var15.get() == "Yes" and self.var36.get() == "Yes") or (self.var18.get() == "Yes" and self.var36.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var36.get() == "Yes") or (self.var24.get() == "Yes" and self.var36.get() == "Yes") or (self.var27.get() == "Yes" and self.var36.get() == "Yes") or (self.var30.get() == "Yes" and self.var36.get() == "Yes") or (self.var33.get() == "Yes" and self.var36.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var39.get() == "Yes") or (self.var6.get() == "Yes" and self.var39.get() == "Yes") or (self.var9.get() == "Yes" and self.var39.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var39.get() == "Yes") or (self.var15.get() == "Yes" and self.var39.get() == "Yes") or (self.var18.get() == "Yes" and self.var39.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var39.get() == "Yes") or (self.var24.get() == "Yes" and self.var39.get() == "Yes") or (self.var27.get() == "Yes" and self.var39.get() == "Yes")
            or (self.var30.get() == "Yes" and self.var39.get() == "Yes") or (self.var33.get() == "Yes" and self.var39.get() == "Yes") or (self.var36.get() == "Yes" and self.var39.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get(),self.text_attr28_num.get(),self.cmb_table10.get(),self.text_attr30_num.get(),self.text_attr31_num.get(),self.cmb_table11.get(),self.text_attr33_num.get(),self.text_attr34_num.get(),self.cmb_table12.get(),self.text_attr36_num.get(),self.text_attr37_num.get(),self.cmb_table13.get(),self.text_attr39_num.get(),self.text_attr40_num.get(),self.cmb_table14.get(),self.text_attr42_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)
            self.text_attr28_num.delete(0,END)
            self.cmb_table10.delete(0,END)
            self.text_attr30_num.delete(0,END)
            self.text_attr31_num.delete(0,END)
            self.cmb_table11.delete(0,END)
            self.text_attr33_num.delete(0,END)
            self.text_attr34_num.delete(0,END)
            self.cmb_table12.delete(0,END)
            self.text_attr36_num.delete(0,END)
            self.text_attr37_num.delete(0,END)
            self.cmb_table13.delete(0,END)
            self.text_attr39_num.delete(0,END)
            self.text_attr40_num.delete(0,END)
            self.cmb_table14.delete(0,END)
            self.text_attr42_num.delete(0,END)


def Save_table15(self):
    if (self.text_table_name.get() == ""):
        messagebox.showerror("Error","Please Enter the table name !!",parent = self.root4)
    elif (self.text_table_name.get() != ""):
        for i in EXIST_TABLE_NAME:
            if (self.text_table_name.get() == i[0]):
                messagebox.showerror("Error","Table already exists !!",parent = self.root4)
        if (self.text_attr1_num.get() == "" or self.cmb_table1.get() == "" or self.text_attr3_num.get() == ""
              or self.text_attr4_num.get() == "" or self.cmb_table.get() == "" or self.text_attr6_num.get() == ""
              or self.text_attr7_num.get() == "" or self.cmb_table3.get() == "" or self.text_attr9_num.get() == ""
              or self.text_attr10_num.get() == "" or self.cmb_table4.get() == "" or self.text_attr12_num.get() == ""
              or self.text_attr13_num.get() == "" or self.cmb_table5.get() == "" or self.text_attr15_num.get() == ""
              or self.text_attr16_num.get() == "" or self.cmb_table6.get() == "" or self.text_attr18_num.get() == ""
              or self.text_attr19_num.get() == "" or self.cmb_table7.get() == "" or self.text_attr21_num.get() == ""
              or self.text_attr22_num.get() == "" or self.cmb_table8.get() == "" or self.text_attr24_num.get() == ""
              or self.text_attr25_num.get() == "" or self.cmb_table9.get() == "" or self.text_attr27_num.get() == ""
              or self.text_attr28_num.get() == "" or self.cmb_table10.get() == "" or self.text_attr30_num.get() == ""
              or self.text_attr31_num.get() == "" or self.cmb_table11.get() == "" or self.text_attr33_num.get() == ""
              or self.text_attr34_num.get() == "" or self.cmb_table12.get() == "" or self.text_attr36_num.get() == ""
              or self.text_attr37_num.get() == "" or self.cmb_table13.get() == "" or self.text_attr39_num.get() == ""
              or self.text_attr40_num.get() == "" or self.cmb_table14.get() == "" or self.text_attr42_num.get() == ""
              or self.text_attr43_num.get() == "" or self.cmb_table15.get() == "" or self.text_attr45_num.get() == ""):
            messagebox.showerror("Error","Attributes, Datatype and Datalength cannot be empty !!",parent = self.root4)
        elif ((self.var2.get() == "Yes" and self.var5.get() == "Yes") or (self.var2.get() == "Yes" and self.var8.get() == "Yes") or (self.var5.get() == "Yes" and self.var8.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var11.get() == "Yes") or (self.var5.get() == "Yes" and self.var11.get() == "Yes") or (self.var8.get() == "Yes" and self.var11.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var14.get() == "Yes") or (self.var5.get() == "Yes" and self.var14.get() == "Yes") or (self.var8.get() == "Yes" and self.var14.get() == "Yes") or (self.var11.get() == "Yes" and self.var14.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var17.get() == "Yes") or (self.var5.get() == "Yes" and self.var17.get() == "Yes") or (self.var8.get() == "Yes" and self.var17.get() == "Yes") or (self.var11.get() == "Yes" and self.var17.get() == "Yes") or (self.var14.get() == "Yes" and self.var17.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var20.get() == "Yes") or (self.var5.get() == "Yes" and self.var20.get() == "Yes") or (self.var8.get() == "Yes" and self.var20.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var20.get() == "Yes") or (self.var14.get() == "Yes" and self.var20.get() == "Yes")or (self.var17.get() == "Yes" and self.var20.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var23.get() == "Yes") or (self.var5.get() == "Yes" and self.var23.get() == "Yes") or (self.var8.get() == "Yes" and self.var23.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var23.get() == "Yes") or (self.var14.get() == "Yes" and self.var23.get() == "Yes")or (self.var17.get() == "Yes" and self.var23.get() == "Yes")or (self.var20.get() == "Yes" and self.var23.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var26.get() == "Yes") or (self.var5.get() == "Yes" and self.var26.get() == "Yes") or (self.var8.get() == "Yes" and self.var26.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var26.get() == "Yes") or (self.var14.get() == "Yes" and self.var26.get() == "Yes")or (self.var17.get() == "Yes" and self.var26.get() == "Yes")or (self.var20.get() == "Yes" and self.var26.get() == "Yes")or (self.var23.get() == "Yes" and self.var26.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var29.get() == "Yes") or (self.var5.get() == "Yes" and self.var29.get() == "Yes") or (self.var8.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var29.get() == "Yes") or (self.var14.get() == "Yes" and self.var29.get() == "Yes")or (self.var17.get() == "Yes" and self.var29.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var29.get() == "Yes")or (self.var23.get() == "Yes" and self.var29.get() == "Yes")or (self.var26.get() == "Yes" and self.var29.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var32.get() == "Yes") or (self.var5.get() == "Yes" and self.var32.get() == "Yes") or (self.var8.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var32.get() == "Yes") or (self.var14.get() == "Yes" and self.var32.get() == "Yes")or (self.var17.get() == "Yes" and self.var32.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var32.get() == "Yes")or (self.var23.get() == "Yes" and self.var32.get() == "Yes")or (self.var26.get() == "Yes" and self.var32.get() == "Yes")or (self.var29.get() == "Yes" and self.var32.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var35.get() == "Yes") or (self.var5.get() == "Yes" and self.var35.get() == "Yes") or (self.var8.get() == "Yes" and self.var35.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var35.get() == "Yes") or (self.var14.get() == "Yes" and self.var35.get() == "Yes")or (self.var17.get() == "Yes" and self.var35.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var35.get() == "Yes")or (self.var23.get() == "Yes" and self.var35.get() == "Yes")or (self.var26.get() == "Yes" and self.var35.get() == "Yes")or (self.var29.get() == "Yes" and self.var35.get() == "Yes")or (self.var32.get() == "Yes" and self.var35.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var38.get() == "Yes") or (self.var5.get() == "Yes" and self.var38.get() == "Yes") or (self.var8.get() == "Yes" and self.var38.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var38.get() == "Yes") or (self.var14.get() == "Yes" and self.var38.get() == "Yes")or (self.var17.get() == "Yes" and self.var38.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var38.get() == "Yes")or (self.var23.get() == "Yes" and self.var38.get() == "Yes")or (self.var26.get() == "Yes" and self.var38.get() == "Yes")
            or (self.var29.get() == "Yes" and self.var38.get() == "Yes")or (self.var32.get() == "Yes" and self.var38.get() == "Yes")or (self.var35.get() == "Yes" and self.var38.get() == "Yes")
            or(self.var2.get() == "Yes" and self.var41.get() == "Yes") or (self.var5.get() == "Yes" and self.var41.get() == "Yes") or (self.var8.get() == "Yes" and self.var41.get() == "Yes")
            or (self.var11.get() == "Yes" and self.var41.get() == "Yes") or (self.var14.get() == "Yes" and self.var41.get() == "Yes")or (self.var17.get() == "Yes" and self.var41.get() == "Yes")
            or (self.var20.get() == "Yes" and self.var41.get() == "Yes")or (self.var23.get() == "Yes" and self.var41.get() == "Yes")or (self.var26.get() == "Yes" and self.var41.get() == "Yes")
            or (self.var29.get() == "Yes" and self.var41.get() == "Yes")or (self.var32.get() == "Yes" and self.var41.get() == "Yes")or (self.var35.get() == "Yes" and self.var41.get() == "Yes")or (self.var38.get() == "Yes" and self.var41.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var6.get() == "Yes") or (self.var3.get() == "Yes" and self.var9.get() == "Yes") or (self.var6.get() == "Yes" and self.var9.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var12.get() == "Yes") or (self.var6.get() == "Yes" and self.var12.get() == "Yes") or (self.var9.get() == "Yes" and self.var12.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var15.get() == "Yes") or (self.var6.get() == "Yes" and self.var15.get() == "Yes") or (self.var9.get() == "Yes" and self.var15.get() == "Yes") or (self.var12.get() == "Yes" and self.var15.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var18.get() == "Yes") or (self.var6.get() == "Yes" and self.var18.get() == "Yes") or (self.var9.get() == "Yes" and self.var18.get() == "Yes") or (self.var12.get() == "Yes" and self.var18.get() == "Yes") or (self.var15.get() == "Yes" and self.var18.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var21.get() == "Yes") or (self.var6.get() == "Yes" and self.var21.get() == "Yes") or (self.var9.get() == "Yes" and self.var21.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var21.get() == "Yes") or (self.var15.get() == "Yes" and self.var21.get() == "Yes") or (self.var18.get() == "Yes" and self.var21.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var24.get() == "Yes") or (self.var6.get() == "Yes" and self.var24.get() == "Yes") or (self.var9.get() == "Yes" and self.var24.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var24.get() == "Yes") or (self.var15.get() == "Yes" and self.var24.get() == "Yes") or (self.var18.get() == "Yes" and self.var24.get() == "Yes") or (self.var21.get() == "Yes" and self.var24.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var27.get() == "Yes") or (self.var6.get() == "Yes" and self.var27.get() == "Yes") or (self.var9.get() == "Yes" and self.var27.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var27.get() == "Yes") or (self.var15.get() == "Yes" and self.var27.get() == "Yes") or (self.var18.get() == "Yes" and self.var27.get() == "Yes") or (self.var21.get() == "Yes" and self.var27.get() == "Yes") or (self.var24.get() == "Yes" and self.var27.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var30.get() == "Yes") or (self.var6.get() == "Yes" and self.var30.get() == "Yes") or (self.var9.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var30.get() == "Yes") or (self.var15.get() == "Yes" and self.var30.get() == "Yes") or (self.var18.get() == "Yes" and self.var30.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var30.get() == "Yes") or (self.var24.get() == "Yes" and self.var30.get() == "Yes") or (self.var27.get() == "Yes" and self.var30.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var33.get() == "Yes") or (self.var6.get() == "Yes" and self.var33.get() == "Yes") or (self.var9.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var33.get() == "Yes") or (self.var15.get() == "Yes" and self.var33.get() == "Yes") or (self.var18.get() == "Yes" and self.var33.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var33.get() == "Yes") or (self.var24.get() == "Yes" and self.var33.get() == "Yes") or (self.var27.get() == "Yes" and self.var33.get() == "Yes") or (self.var30.get() == "Yes" and self.var33.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var36.get() == "Yes") or (self.var6.get() == "Yes" and self.var36.get() == "Yes") or (self.var9.get() == "Yes" and self.var36.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var36.get() == "Yes") or (self.var15.get() == "Yes" and self.var36.get() == "Yes") or (self.var18.get() == "Yes" and self.var36.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var36.get() == "Yes") or (self.var24.get() == "Yes" and self.var36.get() == "Yes") or (self.var27.get() == "Yes" and self.var36.get() == "Yes") or (self.var30.get() == "Yes" and self.var36.get() == "Yes") or (self.var33.get() == "Yes" and self.var36.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var39.get() == "Yes") or (self.var6.get() == "Yes" and self.var39.get() == "Yes") or (self.var9.get() == "Yes" and self.var39.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var39.get() == "Yes") or (self.var15.get() == "Yes" and self.var39.get() == "Yes") or (self.var18.get() == "Yes" and self.var39.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var39.get() == "Yes") or (self.var24.get() == "Yes" and self.var39.get() == "Yes") or (self.var27.get() == "Yes" and self.var39.get() == "Yes")
            or (self.var30.get() == "Yes" and self.var39.get() == "Yes") or (self.var33.get() == "Yes" and self.var39.get() == "Yes") or (self.var36.get() == "Yes" and self.var39.get() == "Yes")
            or(self.var3.get() == "Yes" and self.var42.get() == "Yes") or (self.var6.get() == "Yes" and self.var42.get() == "Yes") or (self.var9.get() == "Yes" and self.var42.get() == "Yes")
            or (self.var12.get() == "Yes" and self.var42.get() == "Yes") or (self.var15.get() == "Yes" and self.var42.get() == "Yes") or (self.var18.get() == "Yes" and self.var42.get() == "Yes")
            or (self.var21.get() == "Yes" and self.var42.get() == "Yes") or (self.var24.get() == "Yes" and self.var42.get() == "Yes") or (self.var27.get() == "Yes" and self.var42.get() == "Yes")
            or (self.var30.get() == "Yes" and self.var42.get() == "Yes") or (self.var33.get() == "Yes" and self.var42.get() == "Yes") or (self.var36.get() == "Yes" and self.var42.get() == "Yes") or (self.var39.get() == "Yes" and self.var42.get() == "Yes")):
            messagebox.showerror("Error","The primary or foreign key cannot be selected twice !!",parent = self.root4)
        else:
            EXIST_TABLE_NAME.clear()
            conn = sqlite3.connect('manuf1.db')
            curs=conn.cursor()
            curs.execute('create table %s(%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s),%s %s(%s))' % (self.text_table_name.get(),self.text_attr1_num.get(),self.cmb_table1.get(),self.text_attr3_num.get(),self.text_attr4_num.get(),self.cmb_table2.get(),self.text_attr6_num.get(),self.text_attr7_num.get(),self.cmb_table3.get(),self.text_attr9_num.get(),self.text_attr10_num.get(),self.cmb_table4.get(),self.text_attr12_num.get(),self.text_attr13_num.get(),self.cmb_table5.get(),self.text_attr15_num.get(),self.text_attr16_num.get(),self.cmb_table6.get(),self.text_attr18_num.get(),self.text_attr19_num.get(),self.cmb_table7.get(),self.text_attr21_num.get(),self.text_attr22_num.get(),self.cmb_table8.get(),self.text_attr24_num.get(),self.text_attr25_num.get(),self.cmb_table9.get(),self.text_attr27_num.get(),self.text_attr28_num.get(),self.cmb_table10.get(),self.text_attr30_num.get(),self.text_attr31_num.get(),self.cmb_table11.get(),self.text_attr33_num.get(),self.text_attr34_num.get(),self.cmb_table12.get(),self.text_attr36_num.get(),self.text_attr37_num.get(),self.cmb_table13.get(),self.text_attr39_num.get(),self.text_attr40_num.get(),self.cmb_table14.get(),self.text_attr42_num.get(),self.text_attr43_num.get(),self.cmb_table15.get(),self.text_attr45_num.get()))
            messagebox.showinfo("Success","Your Table has been created!!",parent=self.root4)
            curs.execute('select name from sqlite_master where type= "table"')
            table = curs.fetchall()
            for i in table:
                EXIST_TABLE_NAME.append(i)
            self.cmb_table=ttk.Combobox(self.root4,font=("times new roman",13),state='readonly',justify=CENTER)
            self.cmb_table.place(x=600,y=100,width=180,height=20)
            EXIST_TABLE_NAME.insert(0,"--Existing Tables--")
            self.cmb_table['values']= EXIST_TABLE_NAME
            self.cmb_table.current(0)
            self.text_table_name.delete(0,END)
            self.text_attr1_num.delete(0,END)
            self.cmb_table1.delete(0,END)
            self.text_attr3_num.delete(0,END)
            self.text_attr4_num.delete(0,END)
            self.cmb_table2.delete(0,END)
            self.text_attr6_num.delete(0,END)
            self.text_attr7_num.delete(0,END)
            self.cmb_table3.delete(0,END)
            self.text_attr9_num.delete(0,END)
            self.text_attr10_num.delete(0,END)
            self.cmb_table4.delete(0,END)
            self.text_attr12_num.delete(0,END)
            self.text_attr13_num.delete(0,END)
            self.cmb_table5.delete(0,END)
            self.text_attr15_num.delete(0,END)
            self.text_attr16_num.delete(0,END)
            self.cmb_table6.delete(0,END)
            self.text_attr18_num.delete(0,END)
            self.text_attr19_num.delete(0,END)
            self.cmb_table7.delete(0,END)
            self.text_attr21_num.delete(0,END)
            self.text_attr22_num.delete(0,END)
            self.cmb_table8.delete(0,END)
            self.text_attr24_num.delete(0,END)
            self.text_attr25_num.delete(0,END)
            self.cmb_table9.delete(0,END)
            self.text_attr27_num.delete(0,END)
            self.text_attr28_num.delete(0,END)
            self.cmb_table10.delete(0,END)
            self.text_attr30_num.delete(0,END)
            self.text_attr31_num.delete(0,END)
            self.cmb_table11.delete(0,END)
            self.text_attr33_num.delete(0,END)
            self.text_attr34_num.delete(0,END)
            self.cmb_table12.delete(0,END)
            self.text_attr36_num.delete(0,END)
            self.text_attr37_num.delete(0,END)
            self.cmb_table13.delete(0,END)
            self.text_attr39_num.delete(0,END)
            self.text_attr40_num.delete(0,END)
            self.cmb_table14.delete(0,END)
            self.text_attr42_num.delete(0,END)
            self.text_attr43_num.delete(0,END)
            self.cmb_table15.delete(0,END)
            self.text_attr45_num.delete(0,END)

