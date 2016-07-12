import requests
import time
import winsound
c1=True
url="http://josaa.nic.in/webinfo/Public/home.aspx"
start='N'
x=0
def display():
    print '//////////////////////////////////////////////////////////////////////////////////////////'
    print '//                                                                                      //'
    print '//        11  11111  11111  11111  11111          11111   11111  11  11111              //'
    print '//        11  11 11  11     11 11  11 11             11   11 11  11  11                 //'
    print '//        11  11 11  11111  11111  11111  -----   11111   11 11  11  11111              //'
    print '//        11  11 11     11  11 11  11 11          11      11 11  11  11 11              //'
    print '//    111111  11111  11111  11 11  11 11          11111   11111  11  11 11              //'
    print '//                                                                                      //'
    print '//////////////////////////////////////////////////////////////////////////////////////////'
    print '//  Designed By :- Mark-III                                                             //'
    print '//  E-mail :- xtreme.research@gmail.com                                                 //'
    print '//////////////////////////////////////////////////////////////////////////////////////////\n\n'
    print '//////////////////////////////////////////////////////////////////////////////////////////'
    print '//  -> This Program will Check every 8 seconds if the JoSSA 2016 Website has Declared   //'
    print "//  Result of the Next Round or not . If Declared , it Will Make the Computer 'Beep'    //"
    print '//////////////////////////////////////////////////////////////////////////////////////////'
    print '//  For Source Code And Information , See :- https://github.com/Mark-3/JoSSA            //'
    print '//  App Written in Python 27 , JoSAA Website :-http://josaa.nic.in                      //'
    print '//////////////////////////////////////////////////////////////////////////////////////////'



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
        print txt
    x+=1
    if(ex is start):
        c1=True
    else:
        c1=False
        print "\n\n"
        print "Round Upgraded - Check Now ! Click Here To Go To Login Page :- http://josaa.nic.in/Result/Root/ResultLogin.aspx "
        alarm()
    time.sleep(delay)
