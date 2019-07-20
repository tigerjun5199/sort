import clientLogin
import clientSort
import clientInput


import requests

clientLogin.login()

if clientLogin.KEY == 'ACK':
    kinput = clientInput.키입력()
    # 키입력 인스턴스를 생성한다
    kiinput = clientInput.kindInput()
    # kindinput 인스턴스를 생성한다
    q = kiinput.bj_input()
    # 입력받는 함수를 수행한다
    keysort = clientSort.정렬하기()
    # 정력하기 인스턴스를 생성한다
    ret = keysort.bj_sort(q, clientLogin.사용자ID)
    # 정렬하는 함수를 실행한다
    print(clientLogin.사용자ID + "님이 요청한 정렬결과입니다.")
    print(clientInput.키입력.n)
    print(ret)


#test for web


