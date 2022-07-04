import socket
import random

HOST = '127.0.0.1'
PORT = int(input("port number: "))

#소켓 객체 생성(주소 체계 : IPv4, 소켓 타입 : TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#지정한 HOST, PORT를 사용하여 서버 접속
client_socket.connect((HOST, PORT))

def get_score(myanswer, answerlist):
    correct = 0
    miss = 0
    
    for i in range(len(myanswer)):
        if myanswer[i] == answerlist[i]:
            correct += 1
        else:
            miss += 1
    return correct, miss

number = input("choice number of digits : ( 2,3,4 )\n")
if number == '2':
    alist = [] #난수 리스트 저장 매개 리스트
    answerlist =[] #선정된 난수 정답 리스트
    sortedlist = [] #선정된 난수 사용자 힌트 리스트
    
    #난수 생성 부분
    for i in range(2):
        a = random.randint(0,9)
        while a in alist:
            a = random.randint(0,9)
        alist.append(a) #sortedlist를 위한 매개 리스트
        answerlist.append(a) #정답 리스트
    
    #사용자에 제공할 힌트 리스트
    alist.sort()
    sortedlist = alist
       
    count = 0 #정답 맞추기 시도한 횟수
    correct = 0
    miss = 0 #사용자에게 힌트로 제공할 s, b
    
    x = answerlist[0] #리스트의 요소를 변수에 저장하여 다른 리스트와 비교하는 방식
    y = answerlist[1]
    
    #숫자 맞추기 게임 부분(반복문)
    while True:
        myanswer = []
        print("answer list :", sortedlist)
        print("guess the answer!")
        a,b = map(int, input().split())
        myanswer.append(a)
        myanswer.append(b)

        if a != x or b != y:
            count += 1
            correct, miss = get_score(myanswer, answerlist)
            print("Wrong!")
            print("number of attempts:",count)
            print("Correct: ",correct, "Miss: ",miss)
            print("try again!")
            strike = 0
            ball = 0
        elif a == x and b == y:
            count += 1
            print("Congratulations! You Win!")
            print("Answer is", answerlist)
            print("number of attempts: ",count)
            print("\n")
            client_socket.send(bytes(count))
            data=client_socket.recv(1024)
            if data.decode('utf-8') == 'A': print("좋은 실력이네요")
            else: print("다음 기회에 더 잘 할 수 있어요")
            client_socket.close()
            break
        else:
            print("error!")
            client_socket.close()
            break
elif number == '3':
    alist = [] #난수 리스트 저장 매개 리스트 초기화
    answerlist =[] #선정된 난수 정답 리스트 초기화
    sortedlist = [] #선정된 난수 사용자 힌트 리스트 초기화
    
    #난수 생성 부분
    for i in range(3):
        a = random.randint(0,9)
        while a in alist:
            a = random.randint(0,9)
        alist.append(a) #sortedlist를 위한 매개 리스트
        answerlist.append(a) #정답 리스트
        
    #사용자에 제공할 힌트 리스트
    alist.sort()
    sortedlist = alist
    
    count = 0 #정답 맞추기 시도한 횟수
    correct = 0
    miss = 0 #사용자에게 힌트로 제공할 s, b
    
    x = answerlist[0] #리스트의 요소를 변수에 저장하여 다른 리스트와 비교하는 방식
    y = answerlist[1]
    z = answerlist[2]
    
    #숫자 맞추기 게임 부분(반복문)
    while True:
        myanswer = []
        print("answer list :", sortedlist)
        print("guess the answer!")
        a,b,c = map(int, input().split())
        myanswer.append(a)
        myanswer.append(b)
        myanswer.append(c)

        if a != x or b != y or c != z:
            count += 1
            correct, miss = get_score(myanswer, answerlist)
            print("Wrong!")
            print("number of attempts:",count)
            print("Correct: ",correct, "Miss: ",miss)
            print("try again!")
            correct = 0
            miss = 0
        elif a == x and b == y and c == z:
            count += 1
            print("Congratulations! You Win!")
            print("Answer is", answerlist)
            print("number of attempts: ",count)
            print("\n")
            client_socket.send(bytes(count))
            data=client_socket.recv(1024)
            if data.decode('utf-8') == 'A': print("좋은 실력이네요")
            else: print("다음 기회에 더 잘 할 수 있어요")
            client_socket.close()
            break
        else:
            print("error!")
            client_socket.close()
            break
elif number == '4':
    alist = [] #난수 리스트 저장 매개 리스트 초기화
    answerlist =[] #선정된 난수 정답 리스트 초기화
    sortedlist = [] #선정된 난수 사용자 힌트 리스트 초기화
    
    #난수 생성 부분
    for i in range(4):
        a = random.randint(0,9)
        while a in alist:
            a = random.randint(0,9)
        alist.append(a) #sortedlist를 위한 매개 리스트
        answerlist.append(a) #정답 리스트
        
    #사용자에 제공할 힌트 리스트
    alist.sort()
    sortedlist = alist
    
    count = 0 #정답 맞추기 시도한 횟수
    correct = 0
    miss = 0 #사용자에게 힌트로 제공할 s, b
    
    x = answerlist[0] #리스트의 요소를 변수에 저장하여 다른 리스트와 비교하는 방식
    y = answerlist[1]
    z = answerlist[2]
    t = answerlist[3]
    
    #숫자 맞추기 게임 부분(반복문)
    while True:
        myanswer = []
        print("answer list :", sortedlist)
        print("guess the answer!")
        a,b,c,d = map(int, input().split())
        myanswer.append(a)
        myanswer.append(b)
        myanswer.append(c)
        myanswer.append(d)

        if a != x or b != y or c != z or d != t:
            count += 1
            correct, miss = get_score(myanswer, answerlist)
            print("Wrong!")
            print("number of attempts:",count)
            print("Correct: ",correct, "Miss: ",miss)
            print("try again!")
            correct = 0
            miss = 0
        elif a == x and b == y and c == z and d == t:
            count += 1
            print("Congratulations! You Win!")
            print("Answer is", answerlist)
            print("number of attempts: ",count)
            print("\n")
            client_socket.send(bytes(count))
            if data.decode('utf-8') == 'A': print("좋은 실력이네요")
            else: print("다음 기회에 더 잘 할 수 있어요")
            client_socket.close()
            break
        else:
            print("error!")
            client_socket.close()
            break
        
