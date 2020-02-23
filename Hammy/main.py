import tkinter as tk
import mysql.connector as m

db = m.connect(host='localhost', user='root', passwd='1qaz2wsx', database='syntechdb')

mycursor = db.cursor()

def quit_prompt():

    def quit_confirm():
        quit(root.destroy())

    def quit_decline():
        prompt.destroy()

    quit_msg = 'rly?'

    prompt = tk.Frame(canvas, bg='#E5FDF8')
    prompt.place(relheight=1, relwidth=1, relx=0, rely=0)

    text_prompt = tk.Label(prompt, font=('Quicksand', 20), text=quit_msg, bg='#E5FDF8')
    text_prompt.place(relheight=0.25, relwidth=0.8, relx=0.1, rely=0.25)

    button_yes = tk.Button(prompt, text='YEAH', font=('Quicksand', 15), command=quit_confirm, bd=2)
    button_yes.place(relheight=0.1, relwidth=0.1, relx=0.2, rely=0.5)

    button_no = tk.Button(prompt, text='NAH', font=('Quicksand', 15), command=quit_decline, bd=2)
    button_no.place(relheight=0.1, relwidth=0.1, relx=0.7, rely=0.5)


def ret_data():
    def back():
        canvas_ret.destroy()

    def next_():
        print(1)

    canvas_ret = tk.Canvas(root, bg='#E5FDF8')
    canvas_ret.place(relheight=1, relwidth=1, relx=0, rely=0)

    label_ret_title = tk.Label(canvas_ret, text='Retrieve Data', font=('Quicksand', 30), bg='#E5FDF8')
    label_ret_title.place(relheight=0.2, relwidth=1, relx=0, rely=0)

    button_retall = tk.Button(canvas_ret, text='Retrieve All Tables', font=('Quicksand', 15))
    button_retall.place(relheight=0.07, relwidth=0.5, relx=0.25, rely=0.25)

    button_select_tbl = tk.Button(canvas_ret, text='Select Tables to Retrieve', font=('Quicksand', 15), command=selectdata)
    button_select_tbl.place(relheight=0.07, relwidth=0.5, relx=0.25, rely=0.4)

    label_where = tk.Label(canvas_ret, text='Enter a Where Clause (Optional)', font=('Quicksand', 15), bg='#E5FDF8')
    label_where.place(relheight=0.05, relwidth=0.5, relx=0.25, rely=0.55)

    text_where = tk.Text(canvas_ret, font=('Quicksand', 21))
    text_where.place(relheight=0.065, relwidth=0.5, relx=0.25, rely=0.6)

    button_back = tk.Button(canvas_ret, text='< Back', font=('Quicksand', 15), command=back)
    button_back.place(relheight=0.05, relwidth=0.1, relx=0.05, rely=0.05)

    button_next = tk.Button(canvas_ret, text='Next >', font=('Quicksand', 15), command=next_)
    button_next.place(relheight=0.07, relwidth=0.1, relx=0.44, rely=0.8)


def ent_data():
    def back():
        canvas_ent.destroy()

    canvas_ent = tk.Canvas()
    canvas_ent.place(relheight=1, relwidth=1, relx=0, rely=0)

    label_ent_title = tk.Label(canvas_ent, text='Enter Data', font=('Quicksand', 30))
    label_ent_title.place(relheight=0.2, relwidth=1, relx=0, rely=0)

    button_newfile = tk.Button(canvas_ent, text='New Table', font=('Quicksand', 15))
    button_newfile.place(relheight=0.05, relwidth=0.15, relx=0.425, rely=0.2)

    frame_table = tk.Frame(canvas_ent)
    frame_table.place(relheight=0.7, relwidth=1, relx=0, rely=0.3)

    button_back_ent = tk.Button(canvas_ent, text='< Back', font=('Quicksand', 15), command=back)
    button_back_ent.place(relheight=0.05, relwidth=0.1, relx=0.05, rely=0.05)


def show_table(table):

    r = mycursor.execute(f'SELECT * FROM {table}')
    m = mycursor.fetchall()




def selectdata():

    def back():
        sel_canvas.destroy()

    mycursor.execute('SHOW TABLES')

    global sel_canvas

    sel_canvas = tk.Canvas()
    sel_canvas.place(relheight=1, relwidth=1, relx=0, rely=0)

    button_back = tk.Button(sel_canvas, text='< Back', font=('Quicksand', 15), command=back)
    button_back.place(relheight=0.05, relwidth=0.1, relx=0.05, rely=0.05)

    search = tk.Entry(font=('Quicksand', 28))
    search.place(relheight=0.07, relwidth=0.4, relx=0.295, rely=0.2)

    enter = tk.Button(text='Search', font=('Quicksand', 15), command=lambda: show_table(search.get()))
    enter.place(relheight=0.07, relwidth=0.1, relx=0.7, rely=0.2)

    tbls = [i for i in mycursor]
    btns = []

    dynamic_height = 1/(1.5* len(tbls))


    for table in tbls:

        opt = tk.Label(sel_canvas, text=table, font=('Quicksand', int(100 * dynamic_height)))
        btns.append(opt)


    for i in range(len(btns)):

        btns[i].place(relheight=dynamic_height, relwidth=1, relx=0, rely=dynamic_height*i + 0.3)


root = tk.Tk()

credit = 'Created By Harivishnu Parashar and Hammad Faizavi'

root.state('zoomed')
root.title('Hammy! v0.1')
root.geometry('900x700')

canvas = tk.Canvas(bg='#E5FDF8')
canvas.place(relheight=1, relwidth=1, relx=0, rely=0)

label_title = tk.Label(canvas, text='Hammy!', font=('Pacifico', 70), fg='#00C69F', bg='#E5FDF8')
label_title.place(relheight=0.3, relwidth=1, relx=0, rely=0)

label_credit = tk.Label(canvas, text=credit, font=('Quicksand', 15), bg='#E5FDF8')
label_credit.place(relheight=0.05, relwidth=1, relx=0, rely=0.3)

button_ret = tk.Button(canvas, text='Retrieve Data', font=('Quicksand', 30), bd=2, command=ret_data)
button_ret.place(relheight=0.2, relwidth=0.3, relx=0.15, rely=0.5)

button_ent = tk.Button(canvas, text='Enter Data', font=('Quicksand', 30), bd=2, command=ent_data)
button_ent.place(relheight=0.2, relwidth=0.3, relx=0.5, rely=0.5)

button_cust = tk.Button(canvas, text='Write Custom MySQL Query', font=('Quicksand', 15), bd=2)
button_cust.place(relheight=0.1, relwidth=0.4, relx=0.275, rely=0.8)

button_setting = tk.Button(canvas, text='Settings', font=('Quicksand', 15), bd=2)
button_setting.place(relheight=0.05, relwidth=0.15, relx=0.8, rely=0.025)

button_quit = tk.Button(canvas, text='Quit', font=('Quicksand', 15), bd=2, command=quit_prompt)
button_quit.place(relheight=0.05, relwidth=0.15, relx=0.05, rely=0.025)

root.mainloop()
