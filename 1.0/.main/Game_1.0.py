# 검 강화하기
# Made By DuBu.
# 제작시간 1일
# release version = 1.0
# clearCon() 함수는 인터넷을 참고함
# 출처는 23줄 참고

from ast import While
from asyncio.windows_events import NULL
from random import *
from math import *
from time import *
import os
from turtle import clear


def clearCon():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# https://www.delftstack.com/ko/howto/python/python-clear-console/

clearCon()

randomNum = randint(1,100)
percent = 0
mon = 0
getMoney = 100
stage = 1
t1 = 0
t2 = 0
t3 = 0
t4 = False
t5 = False
inGame = True
chtMoney = 0

if(t5 == True):
    gwag = 10
elif(t4 == True):
    gwag = 5
else:
    gwag = 1

print('\033[97m' + "\n\n\n\n\n\n        DuBu. PRESENT")
sleep(2)
clearCon()

print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0")
sleep(2)

clearCon()
print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n          LOADING\n           □□□□□")
sleep(0.7)

clearCon()
print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n          LOADING\n           ■□□□□")
sleep(0.3)

clearCon()
print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n          LOADING\n           ■■□□□")
sleep(0.5)

clearCon()
print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n          LOADING\n           ■■■□□")
sleep(0.4)

clearCon()
print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n          LOADING\n           ■■■■□")
sleep(0.2)

clearCon()
print('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n          LOADING\n           ■■■■■")
sleep(2)

clearCon()
startIn = "acmkdsmvjrinsinibnisrbakjv92j3nn2jsmdvncjasdnvkjanskjvbkldjswbv28fech92h8c4h9g8vh945hrjfvjndskjvnsndv,mnscvnihe9rh290930nre93nuvr09vub9vu309nu0r9uv30[V0RUIVNURIVUWEOITUBOU489YT"
startIn = input('\033[97m' + "\n\n\n\n        검 강화하기\n           v1.0\n\n>> PRESS" + '\033[32m' + " [ Enter ]" + '\033[97m' + " TO START <<")



clearCon()
print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[33m' + "\n보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

while True:
    if(stage == 1):
        if(InputT == "a"):
            if(randomNum > percent):
                inGame = True
                gwag = gwag + 1
                mon = floor(mon + (gwag / randint(1,2) * 100 * randint(1,3)))
                clearCon()
                print("검 강화하기! - Made By DuBu.\n\n" + '\033[92m' + "{0}강으로 강화 성공하셨습니다!".format(gwag))
                percent = percent + randint(1,5)
                randomNum = randint(1,100)
                print("\n" + '\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
                InputT = NULL
                sleep(0.0000001)
                InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")
            
            else:
                inGame = False
                clearCon()
                print('\033[97m' + "검 강화하기! - Made By DuBu." + '\033[31m' + "\n\n강화에 실패하셨습니다. - 기록 : {0}강 검 :: {1}원".format(gwag, mon))
                print('\033[36m' + "\n3초뒤 돌아갑니다..")
                InputT = NULL
                sleep(3)
                clearCon()
                randomNum = randint(1,100)
                percent = 0
                
                if(t5 == True):
                    gwag = 10
                    mon = 5000
                elif(t4 == True):
                    gwag = 5
                    mon = 2000
                else:
                    gwag = 1
                    mon = 0
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[33m' + "\n\n보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
                InputT = NULL
                sleep(0.0000001)
                InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

    
        if(InputT == "s"):
            inGame = True
            clearCon()
            print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[35m' + "{0}강 검을 {1}원에 판매하셨습니다.\n".format(gwag, mon))
            getMoney = getMoney + mon
            randomNum = randint(1,100)
            percent = 0
            mon = 0
            if(t5 == True):
                gwag = 10
            elif(t4 == True):
                gwag = 5
            else:
                gwag = 1
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

        if(InputT == "//ct/add/money/"):
            inGame = True
            clearCon()
            getMoney = getMoney + 100000000000000000000000
            print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[33m' + "\n\n보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

        if(InputT == "d"):
            inGame = True
            stage = 2
            clearCon()
            sleep(0.00000001)
            inputT = NULL
            sleep(0.00000001)
            print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[33m' + "< 상점 > - 괄호 안에 있는 숫자는 사용 횟수입니다.\n*주의 사항* 상품을 구매하는 즉시 발동됩니다.\n")
            print('\033[35m' + "| 1 | 파괴 확률 5% 감소 - 5,000원 " + '\033[97m' + "   ({0})".format(t1))
            print('\033[35m' + "| 2 | 파괴 확률 15% 감소 - 15,000원 " + '\033[97m' + " ({0})".format(t2))
            print('\033[35m' + "| 3 | 파괴 확률 초기화 - 35,000원 " + '\033[97m' + "   ({0})".format(t3))
            if(t4 == False):
                print('\033[35m' + "| 4 | 5강 검으로 시작 - 100,000원" + '\033[97m' + "  - "  + '\033[31m' + "[ 해금 전 ]")
            if(t4 == True):
                print('\033[35m' + "| 4 | 5강 검으로 시작 - 100,000원" + '\033[97m' + "  - "  + '\033[92m' + "[ 해금 완료 ]")
            if(t5 == False):
                print('\033[35m' + "| 5 | 10강 검으로 시작 - 500,000원" + '\033[97m' + " - " + '\033[31m' + "[ 해금 전 ]")
            if(t5 == True):
                print('\033[35m' + "| 5 | 10강 검으로 시작 - 500,000원" + '\033[97m' + " - "  + '\033[92m' + "[ 해금 완료 ]")
            
    
            stage2Exit = "acmkdsmvjrinsinibnisrbakjv92j3nn2jsmdvncjasdnvkjanskjvbkldjswbv28fech92h8c4h9g8vh945hrjfvjndskjvnsndv,mnscvnihe9rh290930nre93nuvr09vub9vu309nu0r9uv30[V0RUIVNURIVUWEOITUBOU489YT"
            stage2Exit = input('\033[97m' + "\n >> 돌아가려면 아무 거나 입력하세요. << ")
            if(stage2Exit != "acmkdsmvjrinsinibnisrbakjv92j3nn2jsmdvncjasdnvkjanskjvbkldjswbv28fech92h8c4h9g8vh945hrjfvjndskjvnsndv,mnscvnihe9rh290930nre93nuvr09vub9vu309nu0r9uv30[V0RUIVNURIVUWEOITUBOU489YT"):
                clearCon()
                stage = 1
                sleep(0.00000001)
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[33m' + "\n\n보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
                InputT = NULL
                sleep(0.0000001)
                InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")
            

        if(InputT == "d1"):
            inGame = True
            clearCon()
            if(getMoney >= 5000):
                if(percent < 5):
                    percent = 0
                else:
                    percent = percent - 5
                t1 = t1 + 1
                getMoney = getMoney - 5000
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[94m' + "파괴 확률이 5% 감소됩니다.\n")
            else:
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "돈이 부족합니다.\n")
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")
        
        if(InputT == "d2"):
            inGame = True
            clearCon()
            if(getMoney >= 15000):
                if(percent < 15):
                    percent = 0
                else:
                    percent = percent - 15
                t2 = t2 + 1
                getMoney = getMoney - 15000
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[94m' + "파괴 확률이 15% 감소됩니다.\n")
            else:
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "돈이 부족합니다.\n")
            
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")
        
        if(InputT == "d3"):
            inGame = True
            clearCon()
            if(getMoney >= 35000):
                percent = 0
                t3 = t3 + 1
                getMoney = getMoney - 35000
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[94m' + "파괴 확률이 초기화 됩니다.\n")
            else:
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "돈이 부족합니다.\n")
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

        if(InputT == "d4"):
            inGame = True
            clearCon()
            if(getMoney >= 100000):
                if(t4 != True):
                    t4 = True
                    gwag = 5
                    mon = 2000
                    print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[94m' + "기본검이 5강이 됩니다.\n")
                    getMoney = getMoney - 1000000
                else:
                    print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "이미 구매하셨습니다.\n")
            else:
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "돈이 부족합니다.\n")
            
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")
        
        if(InputT == "d5"):
            inGame = True
            clearCon()
            if(getMoney >= 500000):
                if(t5 != True):
                    t5 = True
                    gwag = 10
                    mon = 5000
                    print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[94m' + "기본검이 10강이 됩니다.\n")
                    getMoney = getMoney - 1000000
                else:
                    print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "이미 구매하셨습니다.\n")
            else:
                print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "돈이 부족합니다.\n")
            
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

        if(InputT == "DuBu."):
            inGame = True
            clearCon()
            print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[35m' + "예, 제작잡니다.. 예..\n(이스터에그 만들어보고 싶어서요..ㅠ)\n")
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

        if(InputT == "fuck"):
            inGame = True
            clearCon()
            print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[35m' + "모르는 사이에 어디서 욕이야.\n이런 싸가ㅈ없ㄴ**가\n")
            print('\033[33m' + "보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
            InputT = NULL
            sleep(0.0000001)
            InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")

        if(inGame == False):
            inputT = NULL

        if(InputT != "a"):
            if(InputT != "s"):
                if(InputT != "d"):
                    if(InputT != "d1"):
                        if(InputT != "d2"):
                            if(InputT != "d3"):
                                if(InputT != "d4"):
                                    if(InputT != "d5"):
                                        if(InputT != "DuBu."):
                                            if(InputT != "fuck"):
                                                if(InputT == "//ct/add/money/"):
                                                    clearCon()
                                                    inGame = True
                                                    print('\033[97m' + "검 강화하기! - Made By DuBu.\n\n" + '\033[31m' + "재대로 된 게임 명령어를 입력해주세요.")
                                                    print('\033[33m' + "\n보유 자금 : " + str(getMoney) + "원\n\n" + '\033[97m' + "{0}강검 :: 실패 확률 : {1}% :: {2}원\n".format(gwag, percent, mon))
                                                    InputT = NULL
                                                    sleep(0.0000001)
                                                    InputT = input('\033[97m' + "강화 하시려면 " + '\033[32m' + "[ a ]" + '\033[97m' + " / 판매하려면 " + '\033[32m' + "[ s ] " + '\033[97m' + " / 상점을 열려면 " + '\033[32m' + "[ d ] " + '\033[97m' + " / 구매하려면 " + '\033[32m' + "[ d(상품번호) ] " + '\033[97m' + "를 입력하세요. >> ")