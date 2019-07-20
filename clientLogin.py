import tkinter as tk
from tkinter import messagebox
import requests
import json

Window_login = tk.Tk()

inputID = tk.StringVar()
inputPassword = tk.StringVar()


사용자ID = ""

def login():
    getUserInput()



def getUserInput():
    # 라벨을 생성함
    label = tk.Label(Window_login, text='정렬서비스')
    ID_label = tk.Label(Window_login, text='ID')
    Password_label = tk.Label(Window_login, text='Password')
    # 이름표시


    # 입력창을 생성한다
    ID = tk.Entry(Window_login, textvariable=inputID)
    # 아이디 입력창
    Password = tk.Entry(Window_login, textvariable=inputPassword)
    # 패스워드 입력창

    # 버튼을 생성한다
    login_button = tk.Button(Window_login, text='login',command=loginButton)
    # 로그인 버튼

    # 라벨,입력창,버튼을 배치한다
    label.grid(row=0,column=0)
    ID.grid(row=1,column=1)
    Password.grid(row=2,column=1)
    login_button.grid(row=3,column=1)
    ID_label.grid(row=1,column=0)
    Password_label.grid(row=2,column=0)
    # 창에서 위치 지정

    # 창을 띄운다
    Window_login.mainloop()

KEY = ''
id = ''

def loginButton():
        global KEY
        global id
        id = inputID.get()
        PassWord = inputPassword.get()
        data = {'ID': id, 'password': PassWord}
        URL = 'http://35.187.208.237:4999/login'
        res = requests.post(URL,data=data)
        KEY =res.text
        if KEY == 'ACK':
            Window_login.destroy()
        elif KEY =='Expiration':
            messagebox.askyesno(title="로그인 실패", message='계정유효기간이\n만료되었습니다')
        else:
            messagebox.askyesno(title="로그인 실패", message='아이디 혹은 비밀번호가 \n틀렸습니다')


if __name__ == "__main__":
   login()
