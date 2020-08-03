import tkinter
import sqlite3



conn = sqlite3.connect('mydb.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books
   (
    b_name TEXT,
    b_author TEXT,
    isbn NUMBER,
    pub_date TEXT
    
    )''')
cur.close()
conn.commit()
conn.close()

def addBook():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES('%s','%s','%s','%s')"%(b_name.get(),b_author.get(),isbn.get(),pub_date.get()))
    cur.close()
    conn.commit()
    conn.close()
    display.set('Book Has Been Added !!')

def delete():
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute("DELETE FROM books")
    c.close()
    conn.commit()
    conn.close()

def query():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    records = cur.fetchall()
   # print_records = tkinter.StringVar()
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "|" + str(record[1]) + "|" + str(record[2]) + "|" + str(record[3]) + "\n"


    tkinter.Label(m, text=print_records).grid(row=18, columnspan=2)
    cur.close()
    conn.commit()
    conn.close()


m = tkinter.Tk()
m.title('books adding and removing')
m.geometry('400x400')
b_name = tkinter.StringVar()
b_author = tkinter.StringVar()
isbn = tkinter.StringVar()
pub_date = tkinter.StringVar()
display = tkinter.StringVar()
delete_box = tkinter.StringVar()
tkinter.Label(m, text='Add / Remove Book').grid(row=1, columnspan=2)
tkinter.Label(m, text='Book Name').grid(row=2, column=0)
tkinter.Label(m, text='Author').grid(row=3, column=0)
tkinter.Label(m, text='ISBN').grid(row=4, column=0)
tkinter.Label(m, text='Publication Date').grid(row=5, column=0)
#tkinter.Label(m, text='Delete ID').grid(row=6, column=0)
x = tkinter.Label(m, text="", textvariable=display).grid(row=10, columnspan=3)

tkinter.Label(m, text="Delete").grid(row=11, column=0)

#add text boxes
tkinter.Entry(m, textvariable=b_name, width=30).grid(row=2, column=1)
tkinter.Entry(m, textvariable=b_author, width=30).grid(row=3, column=1)
tkinter.Entry(m, textvariable=isbn, width=30).grid(row=4, column=1)
tkinter.Entry(m, textvariable=pub_date, width=30).grid(row=5, column=1)
tkinter.Entry(m, textvariable=delete_box, width=30).grid(row=11, column=1)

#add button
tkinter.Button(m, text='Add Book', command=addBook, width=30).grid(row=8, columnspan=2)
tkinter.Button(m, text='Delete a book', command=delete, width=30).grid(row=13, columnspan=2)
tkinter.Button(m, text='Show Books', command=query, width=30).grid(row=15, columnspan=2)


m.mainloop()
