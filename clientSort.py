import datetime
import clientLogin
import clientInput
import requests
class 정렬하기:

    # 현재 날짜와시간을가진 datetime객체를 생성한다
    now = datetime.datetime.now()
    # datetime객체의 함수로 시간과 날짜를 문자열로 변환한다
    nowdate = datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S')

    # 입력:self,정렬하기위해 입력받은 수,유저의 id
    # 출력:정렬된 값
    def bj_sort(self,ia,유저id):
        icount = len(ia)
        ib = [0] * icount
        for i in range(icount):
            count = 0
            dc = 1
            for j in range(icount):
                if ia[i] < ia[j]:
                    count += 1
                elif ia[i] == ia[j]:
                    dc += 1
            ib[count] = ia[i]
            if dc > 1:
                for k in range(dc-1):
                    ib[count + k] = ia[i]
        now = datetime.datetime.now()
        nowdate = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        data = {'userID': clientLogin.id,'nowdate':nowdate,'count':clientInput.키입력.n}
        URL = 'http://35.187.208.237:4999/writelog'
        res = requests.post(URL, data=data)
        result = res.text
        print(result)

        return ib

    # 사용자의 사용기록을 저장
    # 입력:self,유저아이디,입력받은 배열의 갯수


    # if __name__ == "__main__":
    #     param2 = [3,2,8]
    #     print(bj_sort(param2))
