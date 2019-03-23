import requests
from lxml import etree
import itchat
import time

itchat.auto_login()
#login
def check():
    headers={
                "authority": "account.collegeboard.org",
                "scheme": "https",
                #"Host": "account.collegeboard.org",
                "origin": "https://www.collegeboard.org",
                "referer": "https://www.collegeboard.org/",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
            }
    post_data={
                "DURL": "https://www.collegeboard.org/",
                "appId":" 292",
                "formState": "1",
                "username": input("please input account: "),
                "password": input("please input passwd: "),
            }
    url="https://account.collegeboard.org/login/authenticateUser"
    session=requests.Session()
    response=session.post(url,data=post_data,headers=headers)

    if response.status_code==200:
        print("successfully logined")
    else:
        print("logined failed... quiting...")
        print(response.text)
        itchat.send("request failed",toUserName='filehelper')
        exit(1)

    #check process
    url2="https://nsat.collegeboard.org/satweb/satHomeAction.action"

    res = session.get(url2,headers=headers).text
    selector=etree.HTML(res)
    score=selector.xpath("//div[@class='score']//text()")
    if(len(score)>4):
        for item in score[0:2]:             
            itchat.send(item,toUserName='filehelper')
        exit(1)

if(__name__=="__main__"):
    while(True):
        check()
        time.sleep(60)
    
