from flask import Flask
from flask import request
import csv
import datetime


app = Flask(__name__)

Id = ''

PassWord = ''

userID = ''

count = ''

nowdate = ''

@app.route('/login',methods=['POST'])
def login():
    Id = request.form.get('ID')
    PassWord = request.form.get('password')
    ret = checkuser()
    return ret


def CheckDate(userdate):
    now = datetime.datetime.now()
    if now.year < userdate.year:
        return 1
    elif now.year == userdate.year:
        if now.month < userdate.month:
            return 1
        elif now.month == userdate.month:
            if now.day <= userdate.day:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def loadCsv():
    f = open('/~~~/apps/python_app/userdata.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        User = {'userNum': line[0], 'userID': line[1], 'userPassword': line[2], 'userAge': line[3], 'Date': line[4]}
        userList.append(User)
    f.close()


def checkuser():
    loadCsv()
    Id = request.form.get('ID')
    PassWord = request.form.get('password')
    USER = 0
    validity = 0
    for line in userList:
        if Id == line['userID'] and PassWord == line['userPassword']:
            USER = 1
            userID = line['userID']
            userdate = line['Date']
            timestr = datetime.datetime.strptime(userdate,'%Y-%m-%d %H:%M:%S')
            validity = CheckDate(timestr)
            print('date is '+userdate)
            break
    if USER == 1:
        if validity == 1:
            return 'ACK'
        else:
            return 'Expiration'
    else:
        return 'NACK'








@app.route('/writelog',methods=['POST'])
def writeLogCsv():
    userID = request.form.get('userID')
    count = request.form.get('count')
    nowdate = request.form.get('nowdate')
    f = open('/~~~/apps/python_app/serviceLog.csv', 'a', encoding='utf-8')
    wr = csv.writer(f)
    wr.writerow([userID,nowdate,count])
    f.close()
    return 'writelog succed'

app.run(host='0.0.0.0', port=4999, debug=True)