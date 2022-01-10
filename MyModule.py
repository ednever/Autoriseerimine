def alustus():
    """Saidi menuu
    """
    vastus = True
    print("""
        Tere, olete sisenenud meie saiti Vilmem.net!
        Kas te olete meie saidis esimest korda või olete juba registreeritud?
         """)
    while vastus:
        print("""
        1. Minna sisse
        2. Registreerida
             """)
        vastus = input() 
        if vastus=="1":
            print("GG")
            vastus = "autoriseerimine"
            break
        elif vastus=="2":
            print("GGWP")
            vastus = "registreerimine"
            break
        else:
            print("Vale andmetüüp!")


#def login():
#    """User nickname'i ilmumine ja kontroll
#    """
#    user_login = "admin"
#    while True:
#        try:
#            new_user_login=str(input("Sisetage oma nickname vähemalt viiest sümbolist, ning kasutage ainult tähti -> "))
#            if type(new_user_login) == str and len(new_user_login) >= 5:
#                break
#            elif new_user_login == user_login: #2
#                print("Selline nickname on juba hõivatud, palun kirjutage uuesti")
#            else:
#                print("Teie nickname sisetab ebakorrektset sümbolit või ta on liiga lühike")
#    print(new_user_login)

#def password():
#    """User password'i ilmumine ja kontroll
#    """
#    user_password = 0
#    while True:
#        try:
#            user_password=int(input("Sisetage oma password vähemalt viiest sümbolist, ning kasutage ainult numbri -> "))
#            if type(user_password) == int and len(user_password) >= 5: #3
#                break
#            else:
#                print("Teie password sisetab ebakorrektset sümbolit või ta on liiga lühike")
#    print(user_password)

import random

def randompass()->str:
    """Пароль создаётся рандомно
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls) #перемешиваются все символы
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword

def control(passwords:str)->str:
    """Проверка пароля, самое главное чтобы в личном пароле присутсвовал хотя 1 тип символов.
    """
    str0=".,:;!_*-+()/#¤%&"
    alpha=digit=upper=sprcial=0
    ls=list(str0)
    pas=list(passwords)
    for i in range(len(pas)):
        if pas[i].isupper():
            upper=1
        if pas[i].isalpha():
            alpha=1
        if pas[i].isdigit():
            digit=1
        if pas[i] in ls:
            special=1
    if alpha==1 and digit==1 and upper==1 and special==1:
        control=True
    else:
        control=False
    return control