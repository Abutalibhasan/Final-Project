import tkinter
import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()
c.close()
conn.commit()
conn.close()

def submit():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES ('%s','%s','%s','%s')"%(f_name.get(),l_name.get(),e_mail.get(),password.get()))
    tkinter.Label(m, text='New Member has Been Added !!').grid(row=10, columnspan=2)
    c.close()
    conn.commit()
    conn.close()



def delete():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("DELETE FROM members WHERE oid =" + delete_box.get())
    c.close()
    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    records = cur.fetchall()
   # print_records = tkinter.StringVar()
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "  " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + "\n"


    tkinter.Label(m, text=print_records).grid(row=25, columnspan=2)
    cur.close()
    conn.commit()
    conn.close()

m = tkinter.Tk()
m.title('Sign Up/ Remove')
m.geometry("500x500")
f_name = tkinter.StringVar()
l_name = tkinter.StringVar()
e_mail = tkinter.StringVar()
password = tkinter.StringVar()
delete_box = tkinter.StringVar()
tkinter.Label(m, text='Member SIGN UP/ Remove').grid(row=0,columnspan=3)
tkinter.Label(m, text='User ID').grid(row=3,column=0)
tkinter.Label(m, text='User name').grid(row=4,column=0)
tkinter.Label(m, text='Email').grid(row=5, column=0)
tkinter.Label(m, text='Password').grid(row=6,column=0)

tkinter.Label(m, text="Delete User Id").grid(row=16, column=0)
#tkinter.Label(m, text="Last name").grid(row=10, column=1)
#tkinter.Label(m, text="Email").grid(row=10, column=2)
#tkinter.Label(m, text="password").grid(row=10, column=4)


tkinter.Entry(m, textvariable=f_name, width=30).grid(row=3, column=1)
tkinter.Entry(m, textvariable=l_name, width=30).grid(row=4,column=1)
tkinter.Entry(m, textvariable=e_mail, width=30).grid(row=5, column=1)
tkinter.Entry(m, textvariable=password, width=30).grid(row=6,column=1)
tkinter.Entry(m,textvariable=delete_box, width=30).grid(row=16,column=1)



tkinter.Button(m, text='SUBMIT',command=submit, width=30).grid(row=9, columnspan=2)
tkinter.Button(m, text='DELETE', command=delete, width=30).grid(row=18, columnspan=2)
tkinter.Button(m, text='Show Members', command=query, width=30).grid(row=23, columnspan=2)


m.mainloop()
