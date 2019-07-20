# tkinter에서 messagebox부분을 로딩한다
from tkinter import messagebox
import requests
import clientLogin
# 키입력이라는 클래스를 정의한다
class 키입력:
    n = 0
    # 외부에서 정렬기능을 사용하기 위해 호출되는 함수
    # 입력:클래스에 의해 생성된 인스턴스(self)
    # 출력:입력된 정렬할 데이터들
    def bj_input(self):
        return self.key_input()

    # 정렬을 할 값을 입력받는다
    # 입력:self
    # 출력:입력된 정렬할 데이터들
    def key_input(self):
        global n
        n = int(input("배열 수를 입력:"))
        b = [0] * n

        for i in range(n):
            a = int(input())
            b[i] = a

        return (b)

# kindInput클래스를  키입력 클래스로부터 상속받아 정의한다
class kindInput(키입력):
    # 입력방식을 선택할수 있도록 수정한 함수(오버라이드)
    # 입력:클래스에 의해 생성된 인스턴스(self)
    # 출력:입력된 정렬할 데이터들
    def bj_input(self):
        data = messagebox.askyesno(title="입력방식선택", message='키보드로 입력하시겠습니까?')
        if data == True:
            return self.key_input()
        else:
            self.uiinput()
            exit()

    # ui를 통해 정렬할 데이터를 입력받는 클래스의 맴버변수
    def uiinput(self):
        messagebox.showinfo(title="개발중", message='개발중입니다')
