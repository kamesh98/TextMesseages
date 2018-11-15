import argparse
import urllib.request, urllib.error, urllib.parse
import http.cookiejar

parser = argparse.ArgumentParser(description='Collecting message number username and password of way2sms')
parser.add_argument('--message', type=str, help='Message for the SMS', required=True, dest='message')
parser.add_argument('--number', type=str, help='Enter the number to which it has to be sent', required=True, dest='number')
parser.add_argument('--user', type=str, help='The User name of way2sms', required=True, dest='user')
parser.add_argument('--pass', type=str, help='Password of the account of user', required=True, dest='paswd')
data = parser.parse_args()

def collect():
    
    message = data.message
    number = data.number
    username = data.user
    passwd = data.paswd
    return username,passwd,number,message

def send_sms(username,passwd,number,message=''):

    url = 'http://www.way2sms.com/re-login'
    data = 'mobileNo='+username+'&password='+passwd+'&CatType'
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]             
    try:
        opener.open(url, data.encode('utf-8'))
    except:
        print('Cannot connect a connection')
        return False
    
    session_id = str(cj).split('~')[1].split(' ')[0]
    smsurl = 'http://www.way2sms.com/smstoss'
    data = 'ssaction=ss&Token='+session_id+'&toMobile='+number+'&message='+message
    opener.addheaders = [('Referer', 'http://www.way2sms.com/send-sms+'+session_id)]             
    try:
        opener.open(smsurl,data.encode('utf-8'))
        print('Success')
    except:
        print('SMS cannot be sent')
        return False            
    return True

if __name__ == "__main__":
    username,passwd,number,message = collect()
    choice = send_sms(username,passwd,number,message)
    print(choice)
