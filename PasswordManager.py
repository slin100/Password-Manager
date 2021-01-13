import hashlib
global MainHash
MainHash = None
def Hashing():
    global MainHash
    UserName = input("Enter your username:\n")
    UserPassword = input("Enter your password:\n")
    TheHash = hashlib.new('whirlpool')
    TheHash.update(bytes(UserPassword, 'utf-8'))
    PasswordHash = TheHash.hexdigest()
    TheHash.update(bytes(UserName, 'utf-8'))
    UserHash = TheHash.hexdigest()
    MainHash = (PasswordHash + UserHash)*300
    

Hashing()

while True:
    action = input("Encrypt|1|   Decrypt|2|   Chance user|3|   Exit|4|\n")

    def otp_encrypt(message: str, key:str):
            assert(len(message) <= len(key))
            m = message.encode()
            k = key.encode()
            l = []
            for counter, i in enumerate(m):
                l.append(i ^ k[counter])
            return bytes(l)

    if action == "1":
        import string
        zahl1 = string.ascii_letters + string.digits + string.punctuation
        from random import randint
        def pick(words):
            num_words = len(words)
            num_picked = randint(0, num_words -1)
            word_picked = words[num_picked]
            return word_picked

        def pick_new(long):
            for _ in range(int(long)):
                global Password
                Password += pick(zahl1)
            print(Password)
            GoodPassw(long)

        def GoodPassw(long):
            askME = input("Ist das Password gut? (y/no) ")
            if askME == "no":
                global Password
                Password = ""
                print("ok")
                pick_new(long)

        def newPassword():
            long = input("Wie lang soll das Passwort sein? ")
            global Password
            Password = ""
            pick_new(long)
            


        print('Mit "skip" überspringst du den Punkt')
        NameOfProgramm = input("Wie heißt das Programm? ")
        if NameOfProgramm == "skip" or NameOfProgramm == "":
            NameOfProgramm = ""
        else: NameOfProgramm = NameOfProgramm + ": "
        Name = input("Wie lautet dein Name? ")
        if Name == "skip" or Name == "":
            Name = ""
        else: Name = "|Name:" + Name + "|"
        Username = input("Wie lautet dein Username? ")
        if Username == "skip" or Username == "":
            Username = ""
        else: Username = "|Username:" + Username + "|"
        Mail = input("Wie lautet die E-Mail?")
        if Mail == "skip" or Mail == "":
            Mail = ""
        else: Mail = "|E-Mail : " + Mail + "|"
        Password = input("Wie lautet das Password? 'neu' generiert ein neues: ")
        if Password == "skip" or Password == "":
            Password = ""
        elif Password == "neu":
            newPassword()
            Password = "|Password:" + Password + "|"
        else: Password = "|Password:" + Password + "|"
        Date = input("Wie lautet dein Geburtstag? ")
        if Date == "skip" or Date == "":
            Date = ""
        else: Date = "|Data:" + Date + "|"
        with open("Test_Password", "a") as f:
            passw =  NameOfProgramm +Password + Name + Username + Mail + Date
            cipher = str(otp_encrypt(passw, MainHash).decode())
            f.write(cipher.replace("\n","")+ "\n")

    elif action == "2":
        def opt_decrypt(ciphertext:bytes, key:str):
            k = key.encode()
            l = []
            for counter, i in enumerate(ciphertext):
                l.append(i ^ k[counter])
            return bytes(l).decode('utf-8')
        with open("Test_Password", "rb") as f:
            f = f.readlines()
            for i in range(len(f)):
                cipher = f[i]
                print(opt_decrypt(cipher, MainHash))
    
    elif action == "3":
        Hashing()

    elif action == "4":
        break
        
