from tkinter import *
import sqlite3


def submit():
    if ((SelID.get() == 'Enter ID No.') or (SelID.get() == '')):
        conn = sqlite3.connect('Address_Database.db')

        c = conn.cursor()

        c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:r_num)",
                  {
                      'f_name': fname.get(),
                      'l_name': lname.get(),
                      'r_num': rnum.get()})

        conn.commit()

        conn.close()
        fname.delete(0, END)
        lname.delete(0, END)
        rnum.delete(0, END)
        show()

    else:
        conn = sqlite3.connect('Address_Database.db')

        c = conn.cursor()

        c.execute("""UPDATE addresses SET
                        first_name=:f_name,
                        last_name=:l_name,
                        roll_num=:r_num
                        WHERE oid=:oid""",
                  {
                      'f_name': fname.get(),
                      'l_name': lname.get(),
                      'r_num': rnum.get(),
                      'oid': SelID.get()})

        conn.commit()

        conn.close()
        show()


def show():
    conn = sqlite3.connect('Address_Database.db')

    c = conn.cursor()

    c.execute("SELECT oid,* FROM addresses")
    records = c.fetchall()
    print_record = ''
    for record in records:
        print_record += str(record[0]) + '\t ' + str(record[1]) + ' ' + str(record[2]) + '\t' + str(record[3]) + '\n'

    Name = Label(root, text=print_record)
    Name.grid(row=6, column=1, columnspan=2, pady=10)

    conn.commit()

    conn.close()


def Del():
    conn = sqlite3.connect('Address_Database.db')

    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE oid=" + SelID.get())

    conn.commit()

    conn.close()

    SelID.delete(0, "end")

    show()


def Edit():
    conn = sqlite3.connect('Address_Database.db')

    c = conn.cursor()

    c.execute("Select * FROM addresses WHERE oid=" + SelID.get())
    records = c.fetchall()
    print_record = ''
    for record in records:
        print_record += str(record[0]) + '\t ' + str(record[1]) + '\n'

    def temp_fname(e):
        fname.delete(0, END)
    def temp_lname(e):
        lname.delete(0, END)
    def temp_rnum(e):
        rnum.delete(0, END)

    fname.insert(0, records[0][0])
    lname.insert(0, records[0][1])
    rnum.insert(0, records[0][2])
    fname.bind("<FocusIn>", temp_fname)
    lname.bind("<FocusIn>", temp_lname)
    rnum.bind("<FocusIn>", temp_rnum)

    conn.commit()

    conn.close()


if __name__ == '__main__':
    root = Tk()
    root.geometry('260x450+650+150')
    root.title('Main')

    '''
    c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text, 
    roll_num integer)""")
    '''

    f_name = Label(text='First Name')
    f_name.grid(row=1, column=1)
    fname = Entry()
    fname.grid(row=1, column=2)

    l_name = Label(text='Last Name')
    l_name.grid(row=2, column=1)
    lname = Entry()
    lname.grid(row=2, column=2)

    r_num = Label(text='Roll Number')
    r_num.grid(row=3, column=1)
    rnum = Entry()
    rnum.grid(row=3, column=2)

    Submit = Button(root, text='Submit', command=submit)
    Submit.grid(row=4, column=1, columnspan=2, ipadx=100)

    Show = Button(root, text='Show', command=show)
    Show.grid(row=5, column=1, columnspan=2, ipadx=105)

    SelectID = Label(root, text='Select ID')
    SelectID.grid(row=7, column=1)

    Delete = Button(root, text='Delete', command=Del)
    Delete.grid(row=8, column=1, columnspan=2, ipadx=102)

    SelID = Entry()


    def temp_text(e):
        SelID.delete(0, "end")


    SelID.insert(0, 'Enter ID No.')
    SelID.grid(row=7, column=2)
    SelID.bind("<FocusIn>", temp_text)

    Edit = Button(root, text='Edit', command=Edit)
    Edit.grid(row=9, column=1, columnspan=2, ipadx=110)

    mainloop()
