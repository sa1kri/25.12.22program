import random as r
def kaibun():
    kirjuinp = int(input("Number of letters "))
    sГµnad = int(input("Number of words "))
    ABCCons = "qwrtpsdfghjklzxcvbnm"
    ABCVow = "eyuioaГµ"
    if kirjuinp < 3 and sГµnad < 0:
        print("3 letter and 1 word minimum")
    else:
        if kirjuinp % 2 == 0:
            kirju //= 2
        else:
            kirju = kirjuinp//2 + 1
        while sГµnad != 0:
            palindrom = ''    
            kirjucons = 0
            kirjucount = kirju
            while kirjucount != 0:
                kiriBegin = r.randint(0, 1)
                if kiriBegin == 0:
                    kiri = r.choice(ABCCons)
                    kirjucons += 1
                else:
                    kiri = r.choice(ABCVow)
                    kirjucons = 0
                if kirjucons < 3:    
                    palindrom += kiri
                    kirjucount -= 1 
            if kirjuinp % 2 == 0 and kirju != 2:
                print(palindrom[kirju::-1])
                palindrom = palindrom + palindrom[kirju::-1]
            else:
                palindrom = palindrom + palindrom[kirju-2::-1]
            sГµnad -= 1
            print(palindrom) 
kaibun()
