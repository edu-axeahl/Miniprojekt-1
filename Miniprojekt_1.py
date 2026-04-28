#import random


def ladda_citat_fran_fil(filnamn): #klar
    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            cit_lst = fil.readlines()
        return cit_lst
    except:
        return []

def spara_citat_till_fil(citatlista, filnamn):

    with open (filnamn, "w", encoding ="utf-8") as fil:
        for citat in citatlista:
            fil.write(citat + "\n")


    """
    Sparar alla citat till en textfil.



    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    # TODO: Implementera funktionen
    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    print("hello there")
    pass


def visa_alla_citat(citatlista):
    """
    Skriver ut alla citat med numrering.

    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Använd enumerate() för att få index
    # Tips: Använd strip() för att ta bort radbrytningar
    for num, citat in enumerate(citatlista, 1):
        print(f"{num}: {citat.strip()}")


def lagg_till_citat(citatlista):

    nytt_citat = input("Mata in ett nytt citat på formen <citat - författare>:")
    citatlista.append(nytt_citat)
    if citatlista[-1] == nytt_citat:
        return True
    return False
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.

    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i

    Returnerar:
        bool: True om citatet lades till, False annars
    """
    # TODO: Implementera funktionen
    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "Citatet - Författare"



def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.

    Parametrar:
        citatlista (list): Listan att välja citat från
    """
    # TODO: Implementera funktionen
    # Tips: Använd random.randint() eller random.choice()
    # Tips: Kontrollera att listan inte är tom först
    pass


def huvudprogram():
    while True:
        available_files = ["citattexter.txt"]
        print("Hello user")
        for i in range(0, len(available_files)):
            print(f"{i+1}: {available_files[i]}")
        valda_fil = int(input("Choose your designated file: "))

        cit_lst = ladda_citat_fran_fil(available_files[valda_fil - 1]) # den här bestämer vilken fil att ladda in
        while True:
            print("1:Open new file, 2:Show current quotes, 3:Add quote, 4:Remove quote, 5:Save current file, 6:Radera content")
            choice = input("Type action here: ")
            if int(choice) == 1:
                break
            elif int(choice) == 2:
                visa_alla_citat(cit_lst)
            elif int(choice) == 3:
                lagg_till_citat(cit_lst)
            elif int(choice) == 5:
                spara_citat_till_fil(cit_lst, available_files[valda_fil - 1])
            else:
                print("please write valid control")


    """
    Huvudprogrammet som styr menyn och programflödet.
    """


    # 3. Hantera användarens val med if/elif/else
    # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
    # 5. Vid val 4: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()

#import random


def ladda_citat_fran_fil(filnamn): #klar
    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            cit_lst = fil.readlines()
        return cit_lst
    except:
        return []

def spara_citat_till_fil(citatlista, filnamn):

    with open (filnamn, "w", encoding ="utf-8") as fil:
        for citat in citatlista:
            fil.write(citat + "\n")


    """
    Sparar alla citat till en textfil.



    Parametrar:
        citatlista (list): Listan med citat som ska sparas
        filnamn (str): Namnet på filen att skriva till
    """
    # TODO: Implementera funktionen
    # Tips: Använd open() med "w"
    # Tips: Loop'a igenom listan och skriv varje citat + "\n"
    print("hello there")
    pass


def visa_alla_citat(citatlista):
    """
    Skriver ut alla citat med numrering.

    Parametrar:
        citatlista (list): Listan med citat som ska visas
    """
    # TODO: Implementera funktionen
    # Tips: Använd enumerate() för att få index
    # Tips: Använd strip() för att ta bort radbrytningar
    for num, citat in enumerate(citatlista, 1):
        print(f"{num}: {citat.strip()}")


def lagg_till_citat(citatlista):

    nytt_citat = input("Mata in ett nytt citat på formen <citat - författare>:")
    citatlista.append(nytt_citat)
    if citatlista[-1] == nytt_citat:
        return True
    return False
    """
    Lägger till ett nytt citat i listan.
    Användaren får mata in citat och författare.

    Parametrar:
        citatlista (list): Listan som citatet ska läggas till i

    Returnerar:
        bool: True om citatet lades till, False annars
    """
    # TODO: Implementera funktionen
    # Tips: Använd input() för att fråga efter citat och författare
    # Tips: Formatet bör vara "Citatet - Författare"



def slumpa_citat(citatlista):
    """
    Visar ett slumpmässigt citat från listan.

    Parametrar:
        citatlista (list): Listan att välja citat från
    """
    # TODO: Implementera funktionen
    # Tips: Använd random.randint() eller random.choice()
    # Tips: Kontrollera att listan inte är tom först
    pass


def huvudprogram():
    while True:
        available_files = ["citattexter.txt"]
        print("Hello user")
        for i in range(0, len(available_files)):
            print(f"{i+1}: {available_files[i]}")
        valda_fil = int(input("Choose your designated file: "))

        cit_lst = ladda_citat_fran_fil(available_files[valda_fil - 1]) # den här bestämer vilken fil att ladda in
        while True:
            print("1:Open new file, 2:Show current quotes, 3:Add quote, 4:Remove quote, 5:Save current file, 6:Radera content")
            choice = input("Type action here: ")
            if int(choice) == 1:
                break
            elif int(choice) == 2:
                visa_alla_citat(cit_lst)
            elif int(choice) == 3:
                lagg_till_citat(cit_lst)
            elif int(choice) == 5:
                spara_citat_till_fil(cit_lst, available_files[valda_fil - 1])
            else:
                print("please write valid control")


    """
    Huvudprogrammet som styr menyn och programflödet.
    """


    # 3. Hantera användarens val med if/elif/else
    # 4. Vid val 2: lägg till citat och spara med spara_citat_till_fil()
    # 5. Vid val 4: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()