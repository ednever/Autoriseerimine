from random import*
from time import*
def alustus():
    """Saidi menuu
    """
    userNames = ["Edgar"]
    userPasswords = ["12345"]
    vastus = vastus2 = vastus3 = True
    print("""
        Tere, olete sisenenud meie saiti Example.net!
        Kas te olete meie saidis esimest korda või olete juba registreeritud?""")
    while vastus:
        print("""
        1. Sisse minna
        2. Registreerida
        3. Välja minna""")
        vastus = input() 
        if vastus == "1":
            if autoriseerimine() == False:
                print("Olete sisenenud meie saidis!")
                SystemExit
        elif vastus == "2":
            if registreerimine() == False:
                print("...Palun oodake...")
                s = "/"
                for i in range(101):
                    sleep(0.05)
                    print("\r","Load",i*s,str(i),"%",end = " ")
                print("Olete registreerinud meie saidis, palun autoriseerige")
        elif vastus == "3":
            SystemExit
        else:
            print("Vale andmetüüp!")

def autoriseerimine()->bool:
    """Kasutaja mineb sisse oma nimega ja oma parooliga
    :rtype: bool
    """
    while vastus3:
        userName = input("Palun sisetage oma nimi => ")
        if userName not in userNames:
            print("Sellist nime pole registreeritud")
        else:
            print("Olete sisenenud nimega: ",userName)
            userPassword = input("Palun siseta oma parool => ")
            if userPassword not in userPasswords:
                print("Sellist parooli ei ole")
            else:
                vastus3 = False
    return vastus3

def registreerimine()->bool:
    """Lisame kasutaja nimi ja parool loenditesse
    :rtype: bool
    """
    while True:
        NewUserName = input("Palun sisetage oma nimi -> ")               
        if NewUserName not in userNames: 
            userNames.append(NewUserName)
            break
        else:
            print("Selline nimi on juba kasutamas")
    while vastus2:
        print("""
        1. Luua parooli ise
        2. Juhuslikult genereerida parooli""")
        if vastus2 == "1":
            while True:
                NewUserPassword = input("""
                Paroolis peab olema vähemalt 1 sümbol erinevatest tüüpidest
                ->""")
                if kontroll(NewUserPassword) == False: 
                    print("""
                    Parool ei vasta nõuetele""")
                else:
                    userPasswords.append(NewUserPassword)
                    vastus2 = False
        elif vastus2 == "2":
            print("Sinu uus parool on: ",randomPassword())
            usersPasswords.append(randomPassword())
            vastus2 = False
        else:
            print("Vale andmetüüp!")
    return vastus2

def randomPassword()->str:
    """Juhuslikult genereerime parooli
    :rtype: str
    """
    
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = "0123456789"
    str2 = "qwertyuiopasdfghjklzxcvbnm"
    str3 = str2.upper() 
    str4 = str0+str1+str2+str3
    loend = list(str4)
    shuffle(loend)
    password = ''.join([choice(loend) for x in range(12)])
    return password

def kontroll(userPassword:str)->bool:
    """Parooli kontroll: paroolis peab olema vähemalt 1 sümbol erinevatest tüüpidest.
    :param str userPassword: Parool, mis sisetab kasutaja
    :rtype: bool
    """
    str0 = ".,:;!_*-+()/#¤%&"
    alpha = digit = upper = special = False
    while True:
        for i in range(len(userPassword)):
            if userPassword[i].isalpha():
                alpha += 1 
            if userPassword[i].isdigit():
                digit += 1 
            if userPassword[i].isupper():
                upper += 1
            if userPassword[i] in str0:
                special += 1
        if alpha >=  1 and digit >= 1 and upper >= 1 and special >= 1:
            tulemus = True
        else:
            tulemus = False
    return tulemus