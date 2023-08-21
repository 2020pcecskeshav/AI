import tkinter as ttk
from tkinter import font

app=ttk.Tk()
app.title('Attendence system')
app.geometry('400x400')
font_=font.Font(size=20)

ttk.Label(
    app,
    text='face recofnigition system',
    font=font_
).pack()

def register():
    app.destroy()
    import login_admin
    with open('opr','w')as f:
        f.write('register')
    import login_admin
    
    print('register')
def attendence():
    print('attendence') 
    import attendence
    attendence.attendence()
def clear_data():
    print('clear all data ')
ttk.Button(
    app, text='Register',command=register,font=font_,height=3,width=15,bg='#03fcfc').pack(expand=True)
ttk.Button(
    app, text='Attendence',command=attendence,font=font_,height=3,width=15,bg='#42f563').pack(expand=True)
ttk.Button(
    app, text='clear data',command=clear_data,font=font_,height=3,width=15,bg='#cfcf0a').pack(expand=True)

app.mainloop()