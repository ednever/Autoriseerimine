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