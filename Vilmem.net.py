from MyModule import*
alustus()
from module1 import *

users=["Denis"]
passwords=["12345"]

while True:
    print("������������������-1, ��������������-2, �����-3")
    ch=int(input())
    if ch==1:
        print("�� ������� �����������")
        while 1:
            log=input("������� ���� ���: ")
            if log not in users:
                print("������ ��� �� ���� ������, ������ ��� ����������� ���.")
                break
            else:
                print("������ ��� ��� ��� �� ������������.")
        ch=input("����� �������� ������(S) ��� ����� ���������(R)? ")
        if ch.upper()=="R":
            pas=randompass()
            print(pas)
        elif ch.upper()=="S":
            while 1:
                pas=input("������� ���� ������: ")
                result=control(pas)
                if result==True:
                    users.append(log)
                    passwords.append(pas)
                    break
    elif ch==2: 
        print("�� ������� �����������")
        user=input("������� ���� ���: ")
        pas=input("������� ���� ������: ")
        if users.index(user)==passwords.index(pas):
            print("����� ����������")
    elif ch==3:
        print("����� �� ���������")
        break
