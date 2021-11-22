import pickle

filename = 'WorkingGUI/betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item)

def menu(): #Her er vores menu som viser de forskellige valgmuligheder gutterne har
    print("MENU")
    print("1: Print liste")
    print("2: Ændre beløbet på en af gutterne")
    print("3: Hvor meget vi skal have samlet")
    print("4: Hvor meget mangler gutterne at betale")
    print("5: Programmet bliver afsluttet")
    print("6: Legenden")

    valg = input("Indtast dit valg:") #Det første valg man møder er print liste. Man kan ikke gøre så meget der inde, udover at se de forskellige personer
    if (valg == '1'):
        printliste()
        menu()


    if (valg =='2'):# Hvis man vælger valget nummer 2. Kan man ændre beløbet på en af personerne
        print("Hvilket beløb skal redigeres?")
        printliste()
        navn = input("indtast navn")
        if navn in fodboldtur: #Her kalder jeg i vores fodboldstur mappe, efter et navn der inde
            beløb = int(input("hvor meget vil du ændre beløbet med"))
            if beløb == 0: #Hvis beløber man
                valg = input("Det her er et ugyldigt beløb, vil du fortsætte med at ændre?")
                if (valg =='ja'):#Her kommer der en if statement så brugeren kan fortsætte tilbage til menuen og programmet ikke lukker ned
                    menu()

                    afslut()
            else:
                fodboldtur[navn]+=beløb
                menu()

        else:
            print("Det indtastede navn er ikke i listen. Måske du mente: ")
            printliste() #Hvis man har tastet et navn som ikke er i listen, kommer listen op igen, så man kan se navner hvis man har set forkert
            valg = input("Var det en af navene du kunne bruge?")
            if (valg =='ja'):
                print("Skide godt. Du bliver sendt tilbage til menuen hvor du kan ændre beløbet på personen")
                menu()
            else:
                afslut()


        if (valg == '3'):
            print(" Der skal betales 4500kr i alt til turen") #Dette valg er lavet så man kan se det fulde beløb man skal betale hvis man nu har glemt det
            menu()


    if (valg =='4'): #I denne statement kan man se hvor meget de forskellige personer mangler at betale
        printliste()
        print("Hvem vil du undersøge?")
        navn = input("indtast navn")
        if navn in fodboldtur:
            print(navn,"mangler",fodboldtur[navn]+-562,5,"kr") #Her er det beløb alle starter med at mangle

            Valg=input("vil du lukke programmet? Ja/Nej")
            if Valg == 'ja':
                afslut()
            else:
                menu()

        else:
            print("Navnet du søger er ikke i listen. Husk efternavn og store bogstaver")
            menu()

    if (valg =='5'):
       print("Du må have en dejlig dag skattemus") #Her er valget nr.5. Man får denne dejlige besked når man lukker programmet ned
       afslut()

    if (valg =='6'):
        print("Mark får turen gratis fordi han er dejlig") #Her er legenden Marks gratis tur
        afslut()





infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

menu()
