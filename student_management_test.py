from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import sqlite3
import requests
import bs4
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 

#Widget Main structure
root =Tk()
root.title("Student Management System ")
root.geometry("800x650+300+25")
root.config(bg="lightblue")
root.focus_set()

def f1():
	root.withdraw()
	add_st.deiconify()
def f2():
	add_st.withdraw()
	root.deiconify()
def f3():
	root.withdraw()
	view_st.deiconify()
	view_st_data.delete(1.0,END)
	con=None
	try:
		con=connect("management.db")
		print("Connected for View")
		sql="select * from student"
		cursor= con.cursor()
		cursor.execute(sql)
		data=cursor.fetchall()
		info= ""
		for d in data:
			info=info + "Rno:" + str(d[0])+ "\n" +"Name:" + str(d[1])+ "\n" + "Marks:" + str(d[2])+ "\n"+ "--------------------------------------------"
		view_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Issue occured while Viewing",str(e))
	finally :
		if con is not None:
			con.close()
			print("Disconnected for View")
def f4():
	view_st.withdraw()
	root.deiconify()

def f5():
    con = None
    try:
        con = connect('management.db')
        print ('Connected for Insertion')

        cursor = con.cursor()
        cursor.execute('CREATE TABLE if not exists student (rno integer PRIMARY KEY , name text , marks real)'
                       )
        sql = "insert into student values('%d', '%s', '%d')"
        cursor = con.cursor()

        rno = int(add_st_entrno.get())
        name = add_st_entname.get()
        marks = int(add_st_entmarks.get())

        cursor.execute(sql % (rno, name, marks))
        if rno <= 0 or len(str(rno)) == 0:
            showerror("Mistake!", "Invalid Roll no")
        elif len(name) < 2 or False == name.isalpha() or len(name) == 0:
            showerror("Mistake", "Invalid name")
        elif marks < 0 or marks > 100:
            showerror("Mistake", "Invalid marks")
        else:

            con.commit()
            showinfo("Success", "Record added")

        add_st_entrno.delete(0, END)
        add_st_entname.delete(0, END)
        add_st_entmarks.delete(0, END)
    except Exception as e:
        #showinfo("Avoid any blank Inputs \nRoll Nos must be positive integers \nName should only contain alphabets \nMarks should range from 0-10")
        showerror("Insert Error","Avoid any blank Inputs \nRoll Nos must be positive integers \nName should only contain alphabets \nMarks should range from 0-10")
        con.rollback()
    finally:
        if con is not None:
            con.close()
            print ('Disconnected for Insertion')

def up1():
	root.withdraw()
	update_stu.deiconify()
def up2():
	update_stu.withdraw()
	root.deiconify()
def up3():
    con = None
    try:
        con = connect('management.db')
        print ('Connected for update')

        sql = "Update student set name = '%s' , marks = '%d' where rno = '%d' "
        cursor = con.cursor()

        rno = int(update_stu_entrno.get())
        name = update_stu_entname.get()
        marks = int(update_stu_entmarks.get())
        args=(name,marks,rno)
        cursor.execute(sql % args )
    

        if len(name) < 2 or (False == name.isalpha()) or (len(name) == 0):
            showerror('Mistake', 'Invalid name !')
        elif (rno < 0 ):
            showerror('Mistake', 'Invalid Roll No !')
        elif (marks < 0 or marks > 100):
            showerror('Mistake', 'Invalid marks !')
        elif cursor.rowcount >= 1:
            con.commit()
            showinfo('Success !', 'Record Updated Successfully!')
        else:
            showerror('Update Issue!', 'Record doesnt exists!')

        update_stu_entrno.delete(0, END)
        update_stu_entname.delete(0, END)
        update_stu_entmarks.delete(0, END)
    except Exception as e:
        showerror('Update issues',"Avoid any blank Inputs \nInsert Only existing & positve numbers \nName should only contain alphabets \nMarks should range from 0-100")
        con.rollback()
    finally:
        if con is not None:
            con.close()
            print("Disconnected for Update")

def del1():
    delete_stu.withdraw()
    root.deiconify()
    
def del2():
    con = None
    try:
        con = connect('management.db')
        print ('Connected for delete')        

        rno = int(delete_stu_entrno.get())
        args=(rno)
        cursor=con.cursor()
        sql="delete from student where rno ='%d'"
        cursor.execute(sql % args )
    

        if cursor.rowcount >=1:
            con.commit()
            showinfo('Success','Record Deleted')
        else:
            showerror('Delete Error', 'Record doesnt exists!')

        delete_stu_entrno.delete(0, END)
    except Exception as e:
        showerror('Issue while Deleting','Insert only positive and existing values')
        con.rollback()
    finally:
        if con is not None:
            con.close()
            print("Disconnected for Delete")

def del3():
    delete_stu.deiconify()
    root.withdraw()

def quote():
        try:
                web_add="https://www.brainyquote.com/quote_of_the_day"
                res=requests.get(web_add)
	

                data=bs4.BeautifulSoup(res.text,"html.parser")
	
                info=data.find('img',{"class":"p-qotd"})
	

                quote=info['alt']
                #print(quote)
                output=quote
                w = Label(root, text="Quote Of the Day",font=('Times',18,'italic','bold'),bg="lightblue")
                w.place(relx=20,rely=450, anchor='s')
                w.pack()
                x = Label(root, text = output,font=('Times',18,'italic','bold'))
                x.config(bg='lightblue')
                x.place(x=20,y=500)
                x.pack()

        

        except Exception as e:
                print("Issues",str(e))
              
                       
def temp_loc():
        try:
            web_address = 'https://ipinfo.io/'
            res = requests.get(web_address)
    #print(res)

            data = res.json()
    #print(data)

            city_name = data['city']
    #print ('city name= ', city_name)
            a1 = 'http://api.openweathermap.org/data/2.5/weather?units=metric'
            a2 = '&q=' + city_name
            a3 = '&appid=c6e315d09197cec231495138183954bd'
            web_address = a1 + a2 + a3
            res = requests.get(web_address)
    #print(res)
            data = res.json()
    #print(data)

            m=data['main']
            t=m['temp']
    #print("Temp: ",t)

            Location = Label(root, text = "Location",font=('Arial',18,'bold'),bg="lightblue").place(x = 280,y = 530)  
            place_city = Label(root, text = city_name,font=('Arial',18,'bold'),bg="lightblue").place(x = 405,y = 530) 
            Temperature= Label(root, text = "Temp",font=('Arial',18,'bold'),bg="lightblue").place(x = 280, y = 600)
            temp=Label(root, text = t,font=('Arial',18,'bold'),bg="lightblue").place(x = 405, y =600)  
    
        except Exception as e:

            print ('Issues', str(e))
        
def charts():
    plot=array()
    plot.show()
    	
	
def export():
    
    plot=array()
    current_dt = datetime.strftime(datetime.now(), "%d%m%y%H%M%S")
   
    plot.savefig(f'C:\PHYTON\chart_{current_dt}.pdf')

    plot.show()
        
    charts()

def array():
    con=None
    try:
                con=connect("management.db")
                print("Connected fot charts")
                cursor = con.cursor()
                sql= "Select * from student order by marks desc limit 5"
                cursor.execute(sql)
                data = cursor.fetchall()
                names=[]
                marks=[]
                for row in data:
                    names.append(row[1])
                    marks.append(row[2])
                
                plt.bar(names,marks,color='lightblue',label='student performance ')
               
                plt.xlabel("Names")
                plt.ylabel("Marks")
                plt.title("Class Performance of DIV A")
                plt.legend(shadow=True)
                plt.grid()
                
                return plt
            
    except Exception as e:
	    showerror("Issue Plot",str(e))
		
    finally:
	    if con is not None:
		    con.close()
		    print("Disconnected for charts")
 		

quote()
temp_loc()


#buttons
btnAdd=Button(root, text="Add", width=10,font=('arial',18,'bold'),activebackground="lightblue", command=f1)
btnView=Button(root, text="View", width=10,font=('arial',18,'bold'),activebackground="lightblue", command=f3)
btnUpdate=Button(root, text="Update", width=10,font=('arial',18,'bold'),activebackground="lightblue",command=up1)
btnDelete=Button(root, text="Delete", width=10,font=('arial',18,'bold'),activebackground="lightblue",command=del3)
btnCharts=Button(root, text="Charts", width=10,font=('arial',18,'bold'),activebackground="lightblue",command=charts)
btnExport1=Button(root, text="Export PDF", width=10,font=('arial',18,'bold'),activebackground="lightblue",command=export)


#packbuttons
btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnCharts.pack(pady=10)
btnExport1.pack(pady=10)


#add widget
add_st=Toplevel(root)
add_st.title("Add Student Details")
add_st.geometry("400x600+500+70")
add_st.withdraw()
add_st.configure(bg="lightblue")

#add label
add_st_lblrno=Label(add_st, text="Enter Roll No: ", font=('arial',18,'bold'),bg="lightblue")
add_st_entrno=Entry(add_st, bd=5, font=('arial',18,'bold'))
add_st_lblname=Label(add_st, text="Enter Name: ", font=('arial',18,'bold'),bg="lightblue")
add_st_entname=Entry(add_st, bd=5, font=('arial',18,'bold'))
add_st_lblmarks=Label(add_st, text="Enter Marks: ", font=('arial',18,'bold'),bg="lightblue")
add_st_entmarks=Entry(add_st, bd=5, font=('arial',18,'bold'))

#add button
add_st_btnsave=Button(add_st, text="Save", font=('arial',18,'bold'),activebackground="lightblue",command=f5)
add_st_btnback=Button(add_st, text="Back", font=('arial',18,'bold'),activebackground="lightblue",command=f2)

#pack button label
add_st_lblrno.pack(pady=10)
add_st_entrno.pack(pady=10)
add_st_lblname.pack(pady=10)
add_st_entname.pack(pady=10)
add_st_lblmarks.pack(pady=10)
add_st_entmarks.pack(pady=10)
add_st_btnsave.pack(pady=10)
add_st_btnback.pack(pady=10)
add_st.withdraw()

#view widget
view_st= Toplevel(root)
view_st.title("View Stu.")
view_st.geometry("400x400+500+70")
view_st.configure(bg='lightblue')
view_st_data=ScrolledText(view_st,width=28,height=10,font=('arial',18,'bold'))
view_st_btnback=Button(view_st,text="Back",font=('arial',18,'bold'),activebackground='lightblue',command=f4)

view_st_data.pack(pady=5)
view_st_btnback.pack(pady=5)
view_st.withdraw()

#update widget
update_stu=Toplevel(root)
update_stu.title("Update Student Details")
update_stu.configure(bg='lightblue')
update_stu.geometry("400x600+500+70")

#update label
update_stu_lblrno=Label(update_stu, text="Enter Roll No: ", font=('arial',18,'bold'),bg='lightblue')
update_stu_entrno=Entry(update_stu, bd=5, font=('arial',18,'bold'))
update_stu_lblname=Label(update_stu, text="Enter Name: ", font=('arial',18,'bold'),bg='lightblue')
update_stu_entname=Entry(update_stu, bd=5, font=('arial',18,'bold'))
update_stu_lblmarks=Label(update_stu, text="Enter Marks: ", font=('arial',18,'bold'),bg='lightblue')
update_stu_entmarks=Entry(update_stu, bd=5, font=('arial',18,'bold'))

#update button
update_stu_btnsave=Button(update_stu, text="Save", font=('arial',18,'bold'),activebackground='lightblue',command=up3)
update_stu_btnback=Button(update_stu, text="Back", font=('arial',18,'bold'),activebackground='lightblue',command=up2)

#pack Update
update_stu_lblrno.pack(pady=10)
update_stu_entrno.pack(pady=10)
update_stu_lblname.pack(pady=10)
update_stu_entname.pack(pady=10)
update_stu_lblmarks.pack(pady=10)
update_stu_entmarks.pack(pady=10)

update_stu_btnsave.pack(pady=10)
update_stu_btnback.pack(pady=10)
update_stu.withdraw()


#delete widget
delete_stu=Toplevel(root)
delete_stu.title("Delete Student Details")
delete_stu.configure(bg='lightblue')
delete_stu.geometry("400x600+500+70")

#delete label
delete_stu_lblrno=Label(delete_stu, text="Enter Roll No: ", font=('arial',18,'bold'),bg='lightblue')
delete_stu_entrno=Entry(delete_stu, bd=5, font=('arial',18,'bold'))

#delete button
delete_stu_btnsave=Button(delete_stu, text="Save", font=('arial',18,'bold'),activebackground='lightblue',command=del2)
delete_stu_btnback=Button(delete_stu, text="Back", font=('arial',18,'bold'),activebackground='lightblue',command=del1)

#delete pack
delete_stu_lblrno.pack(pady=10)
delete_stu_entrno.pack(pady=10)
delete_stu_btnsave.pack(pady=10)
delete_stu_btnback.pack(pady=10)
delete_stu.withdraw()

root.mainloop()














