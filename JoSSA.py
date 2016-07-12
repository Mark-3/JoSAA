import requests
import time
import winsound
from termcolor import colored
c1=True
url="http://josaa.nic.in/webinfo/Public/home.aspx"
start='N'
x=0
def display():
    print colored('//////////////////////////////////////////////////////////////////////////////////////////','red')
    print colored('//                                                                                      //','red')
    print colored('//        11  11111  11111  11111  11111          11111   11111  11  11111              //','red')
    print colored('//        11  11 11  11     11 11  11 11             11   11 11  11  11                 //','red')
    print colored('//        11  11 11  11111  11111  11111  -----   11111   11 11  11  11111              //','red')
    print colored('//        11  11 11     11  11 11  11 11          11      11 11  11  11 11              //','red')
    print colored('//    111111  11111  11111  11 11  11 11          11111   11111  11  11 11              //','red')
    print colored('//                                                                                      //','red')
    print colored('//////////////////////////////////////////////////////////////////////////////////////////','red')
    print colored('//  Designed By :- Mark-III                                                             //','red')
    print colored('//  E-mail :- xtreme.research@gmail.com                                                 //','red')
    print colored('//////////////////////////////////////////////////////////////////////////////////////////\n\n', 'red')
    print colored('//////////////////////////////////////////////////////////////////////////////////////////','green')
    print colored('//  -> This Program will Check every 8 seconds if the JoSSA 2016 Website has Declared   //','green')
    print colored("//  Result of the Next Round or not . If Declared , it Will Make the Computer 'Beep'    //",'green')
    print colored('//////////////////////////////////////////////////////////////////////////////////////////','green')
    print colored('//  For Source Code And Information , See :- https://github.com/Mark-3/JoSSA            //','green')
    print colored('//  App Written in Python 27 , JoSAA Website :-http://josaa.nic.in                      //','green')
    print colored('//////////////////////////////////////////////////////////////////////////////////////////','green')



display()
delay=8
'''The Time Delay Thingy '''
def alarm():
    '''The Stuff That Makes the Alarming Sound !'''
    winsound.Beep(500, 1000)
    time.sleep(2)

while(c1 is True):
    t1=requests.get(url)
    t2=t1.content
    t3=str(t2)
    pos=t3.find('Click here for Seat Allotment Result : Round ')
    pos=pos+45
    ex=t3[pos:1+pos]
    if(x is 0):
        start=ex
        txt="\n\nCurrent Round in JoSSA 2016 = Round "+str(ex)
        print colored(txt,'green')
    x+=1
    if(ex is start):
        c1=True
    else:
        c1=False
        print "\n\n"
        print colored("Round Upgraded - Check Now ! Click Here To Go To Login Page :- http://josaa.nic.in/Result/Root/ResultLogin.aspx ",'yellow')
        alarm()
    time.sleep(delay)
 
