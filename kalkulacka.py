import math #používání balíčku math, obsahuje mocniny a odmocniny


cislo1 = 0 #první číslo do vzorečku
cislo2 = 0 #druhé číslo do vzorečku
funkce = "" #sčítání, odčítání, násobení, dělení, mocnina, odmocnina 
n = 0 #Hodnota pro n-tou odmocninu či mocninu

while True: #Program se opakuje vždy dokola bez ukončení
    
    #neni udelana kontrola, zda-li je hodnota cislo1, cislo2 a n realne cislo
    
    cislo1 = float(input("Zadej první číslo do výpočtu: ")) #stanovení prvního čísla do vzorečku, pomoci funkce float() se text změní na !DESETINNÉ! číslo
    funkce = input("Zadej funkci \n Možnosti | [+] [-] [*] [/] [mocnina] [odmocnina]: ") #výběr funkce, \n napíše text na další řádek, pouze grafické
    
    if funkce == "+":
        cislo2 = float(input("Zadej druhé číslo do výpočtu: "))
        print(cislo1 + cislo2) #dělení
        
    elif funkce == "-":
        cislo2 = float(input("Zadej druhé číslo do výpočtu: "))
        print(cislo1 - cislo2) #odečítání
        
    elif funkce == "*":
        cislo2 = float(input("Zadej druhé číslo do výpočtu: "))
        print(cislo1 * cislo2) #násobení
        
    elif funkce == "/":
        cislo2 = float(input("Zadej druhé číslo do výpočtu: "))
        if cislo2 == 0: #kontrola
            print("Nulou nelze dělit!!")
        else:
            print(cislo1 / cislo2) #dělení
        
    elif funkce == "mocnina":
        n = int(input("Kolikátou mocninu čísla?: "))
        print(math.pow(cislo1, n)) #použití funkce math.pow pro mocniny, cislo1 je první zadaná hodnota, n je n-tá mocnina
        
    elif funkce == "odmocnina":
        if cislo1 < 0: #kontrola
            print("Odmocnina záporného čísla neexistuje...")
        else:
            n = int(input("Kolikátou odmocninu čísla?: "))
            print(math.pow(cislo1, 1/n))  #použití funce math.pow() pro odmocninu, např. 3 odmocnina je vlastně mocnina 1/3, proto tento výpočet
                                          #pro jednoduchou druhou odmocninu lze použít funkce math.sqrt()
                                        
