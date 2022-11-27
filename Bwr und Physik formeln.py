import time 

def alle_formeln():
    for clear in range(5):
        print("")
    print("WARNUNG:"" WENNN BUCHSTABEN IM ZAHLEN FELD SIND, WIRD ES ZU ABSTÜRZEN KOMMEN!")
    for clear in range(5):
        print("")
    time.sleep(0.5)
    while True:
        Auswahl = input("Aus welchen Fach brauchst du die Formeln? ")
        time.sleep(0.5)
        if Auswahl == "Bwr":
            while True:
                for clear in range(100):
                    print("")
                print("")
                print("AUSWAHL BWR")
                print("")
                time.sleep(0.5)
                formel = input("Welche Formel Brauchst du? ")
                if formel == "Steuer":
                    while True:
                        print("")
                        print("")
                        prozent = input("Wie viel prozent? ")
                        time.sleep(0.25)
                        if prozent == "19":
                                print("für alles was nicht dem mäßigten Steuersatz unterliegt oder nicht umsatzsteuerfrei ist.")
                                print("")
                                print("")
                                print("")
                                print("")
                                plus_minus = input("willst du '+' oder '-' rechnen? ")
                                time.sleep(0.25)
                                if plus_minus == "+":
                                    steuer_positiv = input("Auf welchen Betrag willst du '19%' addieren? ")
                                    steuer_positiv = float(steuer_positiv)
                                    if steuer_positiv > 0:
                                        ergebnis_positiv = (steuer_positiv * 19) / 100
                                        ergebnis_positiv = float(ergebnis_positiv)
                                        insgesamt_positiv = steuer_positiv + ergebnis_positiv
                                        ergebnis_positiv = round(ergebnis_positiv, 2)
                                        insgesamt_positiv = round(insgesamt_positiv, 2)
                                        time.sleep(0.15)
                                        print("")
                                        print(f"Es wurden {ergebnis_positiv} € Steuern hinzugerechnet")
                                        print("")
                                        time.sleep(0.25)
                                        print(f"Der neue Betrag ist {insgesamt_positiv} €")
                                        print("")
                                        quitt = input("Willst du Aufhören Steuern zu berechnen? (y um zu bestätigen) ")
                                        time.sleep(0.5)
                                        if quitt == "y":
                                            for clear in range(100):
                                                print()
                                            break
                                    else:
                                        print("Der Betrag muss über 0 sein")
                                        time.sleep(0.25)
                                elif plus_minus == "-":
                                    time.sleep(0.25)
                                    steuer_negativ = input("Auf Welchen Betrag willst du '19%' Abziehen?? ")
                                    steuer_negativ = float(steuer_negativ)
                                    if steuer_negativ > 0:
                                        ergebnis_negativ = (steuer_negativ * 19) / 100
                                        insgesamt_negativ = steuer_negativ - ergebnis_negativ
                                        ergebnis_negativ = round(ergebnis_negativ, 2)
                                        insgesamt_negativ = round(insgesamt_negativ, 2)
                                        time.sleep(0.25)
                                        print("")
                                        print(f"Es wurden {ergebnis_negativ} € abgezogen")
                                        print("")
                                        time.sleep(0.25)
                                        print(f"Der neue Betrag ist {insgesamt_negativ} €")
                                        print("")
                                        quitt = input("Willst du aufhören Steuern auszurechnen? (y um zu bestätige ) ")
                                        if quitt == "y":
                                            for clear in range(100):
                                                print("")
                                            break
                                    else:
                                     print("Der betrag muss über 0 sein")
                                     time.sleep(0.25)
                                else:
                                    print("Es kann nur '+' oder '-' sein")
                                    time.sleep(0.25)
                        elif prozent == "7":               
                                print("für Lebensmittel, Bücher und Zeitschriften, Personennahverkehr, Tickets für ein Konzert sowie Theater oder Museen, lebende Tiere")
                                print("")
                                print("")
                                print("")
                                print("")
                                plus_minus = input("willst du '+' oder '-'? rechnen ")
                                if plus_minus == "+":
                                    steuer_positiv = input("Auf welchen Betrag willst du auf '7%' Addieren? ")
                                    steuer_positiv = float(steuer_positiv)
                                    if steuer_positiv > 0:
                                        ergebnis_positiv = (steuer_positiv * 7) / 100
                                        insgesamt_positiv = steuer_positiv + ergebnis_positiv
                                        ergebnis_positiv = round(ergebnis_positiv, 2)
                                        insgesamt_positiv = round(insgesamt_positiv, 2)
                                        time.sleep(0.25)
                                        print("")
                                        print(f"Es wurden {ergebnis_positiv} € hinzugerechnet")
                                        print("")
                                        time.sleep(0.25)
                                        print(f"Der neue Betrag ist {insgesamt_positiv} € ")
                                        print("")
                                        quitt = input("Willst du aufhören Steuern auszurechnen? (y um zu bestätige ) ")
                                        if quitt == "y":
                                            for clear in range(100):
                                                print("")
                                            break
                                    else:
                                        print("Der Betrag muss über 0 sein")
                                elif plus_minus == "-": 
                                    steuer_negativ = input("Auf welchen betrag willst du auf '7%' Abziehen? ")
                                    steuer_negativ = float(steuer_negativ)
                                    if steuer_negativ > 0:
                                        ergebnis_negativ = (steuer_negativ * 7) / 100
                                        insgesamt_negativ = steuer_negativ - ergebnis_negativ
                                        time.sleep(0.25)
                                        print("")
                                        print(f"Es wurden {ergebnis_negativ} € abgezogen")
                                        time.sleep(0.25)
                                        print("")
                                        print(f"Der neue Betrag ist {insgesamt_negativ}")
                                        print("")
                                        time.sleep(0.25)
                                        quitt = input("Willst du Aufhören Steuern zu Berechen? (y um zu bestätigen) ")
                                        if quitt == "y":
                                            for clear in range(100):
                                                print("")
                                            break
                                    else:
                                        print("Der Betrag muss über 0 sein")
                                        time.sleep(0.25)
                                else:
                                    print("Es kann nur '+' oder '-' sein")
                                    time.sleep(0.25)
                        else:
                            steuer_prozent = prozent
                            steuer_prozent = float(steuer_prozent)
                            if steuer_prozent > 0:
                                 plus_minus = input("Willst du '+' oder '-' Rechnen? ")
                                 time.sleep(0.25)
                                 if plus_minus == '+':
                                     steuer_positiv = input(f"Auf Welchen Betrag willst du '{steuer_prozent} %' Addieren? ")
                                     time.sleep(0.25)
                                     steuer_positiv = float(steuer_positiv)
                                     if steuer_positiv > 0:
                                         ergebnis_positiv = (steuer_positiv * steuer_prozent) / 100
                                         insgesamt_positiv = steuer_positiv + ergebnis_positiv
                                         insgesamt_positiv = round(insgesamt_positiv, 2)
                                         ergebnis_positiv = round(ergebnis_positiv, 2)
                                         print("")
                                         print(f"Es wurden {ergebnis_positiv} € Addiert")
                                         print("")
                                         time.sleep(0.25)
                                         print(f"Der neue Betrag ist {insgesamt_positiv} €")
                                         print("")
                                         time.sleep(0.25)
                                         quitt = input("Willst du Aufhören Pozente zu Berechnen? (y um zu bestätigen) ") 
                                         if quitt == "y":
                                          for clear in range(100):
                                             print("")
                                          break
                                     else:
                                      print("Der Betrag muss über 0 sein")
                                 elif plus_minus == "-":
                                     steuer_prozent = prozent
                                     steuer_prozent = float(steuer_prozent)
                                     steuer_negativ = input(f"Auf welchen Betrag willst du '{steuer_prozent} %' Abziehen?? ")
                                     steuer_negativ = float(steuer_negativ)
                                     if steuer_negativ > 0:
                                             ergebnis_negativ = (steuer_negativ * steuer_prozent) / 100
                                             insgesamt_negativ = steuer_negativ - ergebnis_negativ
                                             ergebnis_negativ = round(ergebnis_negativ, 2)
                                             insgesamt_negativ = round(insgesamt_negativ, 2)
                                             time.sleep(0.25)
                                             print("")
                                             print(f"Es wurden {ergebnis_negativ} € abgezogen")
                                             print("")
                                             time.sleep(0.25)
                                             print(f"Der neue Wert ist {insgesamt_negativ} €")
                                             time.sleep(0.25)
                                             quitt = input("Willst du Aufhören Steuern zu Berechnen? (y um zu bestätigen) ")
                                             if quitt == "y":
                                                 for clear in range(100):
                                                     print("")
                                                 time.sleep(0.25)
                                                 break
                                     else:
                                      print("")
                                      print("Der Betrag muss über 0 sein")
                                      time.sleep(0.25)
                                 else:
                                    print("")
                                    print("Es kann nur '+' oder '-' sein")
                                    time.sleep(0.25)    
                elif formel == "Einkaufskalkulation":
                    for clear in range(100):
                        print("")
                    while True:
                        Listeneinkaufspreis = input("Was ist der Listeneinkaufspreis? ")
                        time.sleep(0.15)
                        anzahl = input("Wie viel Ware wird gekauft?")
                        time.sleep(0.15)
                        Liefererrabatt = input("Gibt es ein Lieferrabatt? (wenn ja wie viel? ")
                        time.sleep(0.15)
                        Lieferskonto = input("Gibt es ein Lieferskono? (wenn ja wie viel?) ")
                        time.sleep(0.15)
                        Bezugskosten = input("Gibt es Bezugskosten? (wenn ja wie viel?) ")
                        time.sleep(0.15)
                        Listeneinkaufspreis = float(Listeneinkaufspreis)
                        anzahl = float(anzahl)
                        Liefererrabatt = float(Liefererrabatt)
                        Lieferskonto = float(Lieferskonto)
                        Bezugskosten = float(Bezugskosten)
                        if Listeneinkaufspreis > 0:
                            if anzahl > 0:
                                preis = Listeneinkaufspreis * anzahl
                                preis = float(preis)
                                rabatt = (preis * Liefererrabatt) / 100
                                rabatt = float(rabatt)
                                Zieleinkaufspreis = preis - rabatt
                                Zieleinkaufspreis = float(Zieleinkaufspreis)
                                skonto = (Zieleinkaufspreis * Lieferskonto) / 100
                                skonto = float(skonto)
                                Bareinkaufspreis = Zieleinkaufspreis - skonto
                                Bareinkaufspreis = float(Bareinkaufspreis)
                                Einstandspreis = Bezugskosten + Bareinkaufspreis
                                Einstandspreis = float(Einstandspreis)
                                preis = round(preis, 2)
                                rabatt = round(rabatt, 2)
                                Zieleinkaufspreis = round(Zieleinkaufspreis, 2)
                                skonto = round(skonto, 2)
                                Bareinkaufspreis = round(Bareinkaufspreis, 2)
                                Bezugskosten = round(Bezugskosten, 2)
                                Einstandspreis = round(Einstandspreis, 2)
                                time.sleep(0.5)
                                for clear in range(100):
                                    print("")
                                print("____________________________________________________________________")
                                print(f"|Listeneinkaufspreis | {preis} €                                   ")
                                print(f"|Lieferrabatt        | {rabatt} €                                  ")
                                print(f"|____________________|_____________________________________________")
                                print(f"|Zieleinkaufspreis   | {Zieleinkaufspreis} €                       ")
                                print(f"|Lieferskonto        | {skonto} €                                  ")
                                print(f"|____________________|_____________________________________________")
                                print(f"|Bareinkaufspreis    | {Bareinkaufspreis} €                        ")
                                print(f"|Bezugskosten        | {Bezugskosten} €                            ")
                                print(f"|____________________|_____________________________________________")
                                print(f"|Einstandspreis      | {Einstandspreis} €                          ")
                                print("|____________________|_____________________________________________")
                                quitt = input("Willst aufhören die Einkaufskalkulation auzurechnen? (y um zu bestätigen) ")
                                for clear in range(50):
                                    print("")
                                if quitt == "y":
                                    for clear in range(100):
                                        print("")
                                    break
                            else:
                                print("Die Anzahl muss über 0 sein")
                                time.sleep(1)
                                for clear in range(100):
                                    print("")
                                time.sleep(0.15)
                        else:
                            print("Der Listeneinkaufspreis muss über 0 sein")
                            time.sleep(1)
                            for clear in range(100):
                                print("")
                            time.sleep(0.15)
                elif formel == "Verkaufskalkulation":
                    pass
                    while True:
                        selbstkostenpreis = input("Was ist der Selbstkostenpreis? ")
                        time.sleep(0.25)
                        gewinn = input("Was ist der Gewinn? ")
                        time.sleep(0.25)
                        rabatt = input("gibt es ein Rabatt? (wenn ja wie viel?) ")
                        time.sleep(0.25)
                        skonto = input("gibt es ein sknoto? (wenn ja wie viel?) ")
                        time.sleep(0.10)
                        selbstkostenpreis = float(selbstkostenpreis)
                        if selbstkostenpreis > 0:
                            gewinn = float(gewinn)
                            rabatt = float(rabatt)
                            skonto = float(skonto)
                            gewinn_add = (selbstkostenpreis * gewinn) / 100
                            gewinn_add = float(gewinn_add)
                            Barverkaufspreis = gewinn_add + selbstkostenpreis
                            Barverkaufspreis = float(Barverkaufspreis)
                            skonto_geteilt = 100 - skonto
                            skonto_geteilt = float(skonto_geteilt)
                            skonto_add = (Barverkaufspreis * skonto) / skonto_geteilt
                            skonto_add = float(skonto_add)
                            Zielverkaufspreis = skonto_add + Barverkaufspreis
                            Zielverkaufspreis = float(Zielverkaufspreis)
                            rabatt_geteilt = 100 - rabatt
                            rabatt_add = (rabatt * Zielverkaufspreis) / rabatt_geteilt
                            rabatt_add = float(rabatt_add)
                            Listenverkaufspreis = rabatt_add + Zielverkaufspreis
                            Listeneinkaufspreis = float(Listenverkaufspreis)
                            selbstkostenpreis = round(selbstkostenpreis, 2)
                            gewinn_add = round(gewinn_add, 2)
                            Barverkaufspreis = round(Barverkaufspreis, 2)
                            skonto_add = round(skonto_add, 2)
                            Zielverkaufspreis = round(Zielverkaufspreis, 2)
                            rabatt_add = round(rabatt_add, 2)
                            Listenverkaufspreis = round(Listenverkaufspreis, 2)
                            print(f"__________________________________________________________________")
                            print(f"|Selbstkostenpreis  | {selbstkostenpreis} €                       ")
                            print(f"|Gewinn             | {gewinn_add} €                              ")
                            print(f"|___________________|_____________________________________________")
                            print(f"|Barverkaufspreis   | {Barverkaufspreis} €                        ")
                            print(f"|Kundenskonto       | {skonto_add} €                              ")
                            print(f"|___________________|_____________________________________________")
                            print(f"|Zielverkaufspreis  | {Zielverkaufspreis} €                       ")
                            print(f"|Kundenrabatt       | {rabatt_add} €                              ")
                            print(f"|___________________|_____________________________________________")
                            print(f"|Listenverkaufspreis| {Listenverkaufspreis} €                     ")
                            print(f"|___________________|_____________________________________________")
                        else:
                            print("Der Selbstkostenpreis muss über 0 sein")
                        quitt = input("Willst aufhören die Einkaufskalkulation auzurechnen? (y um zu bestätigen) ")
                        for clear in range(50):
                            print("")
                        if quitt == "y":
                            for clear in range(100):
                                print("")
                            break
                elif formel == "hilfe":
                  print("Befehle:")
                  print("")
                  print("'Steuer' um die Steuer bzw Prozente auszurechnen")
                  print("")
                  print("'Einkaufskalkulation'")
                  print("") 
                  print("'Verkaufskalkulation'")
                  print("")
                  print("'quit' um zurückzukehren")
                  print("")
                  print("Rest kommt bald!")
                  skip = input("")
                elif formel == "quit":
                    for clear in range(100):
                        print("")
                    break
        elif Auswahl == "Physik":
            for clear in range(100):
                print("")
        print("PHYSIK")
        for clear in range(5):
                print("")
        while True:
                formel = input("Welche Formel brauchst du? ")
                for clear in range(100):
                    print("")
                if formel == "Gewichtsumrechnung":
                    time.sleep(0.15)
                    for clear in range(5):
                        print("")
                    while True:
                        
                        quitt = input("Willst du Aufhören Gewicht umzurechnen? (quit um zu bestätigen) ")
                        if quitt == "quit":
                            for clear in range(100):
                                print("")
                            break
                        print("von welcher einheit in welche einheit willst du Umrechnen? ")
                        for clear in range(10):
                            print("")
                        Einhheit_von = input("von welcher einheit? ")
                        time.sleep(0.15)
                        Einheit_in = input ("in welcher Einheit? ")
                        if Einhheit_von == "kg":
                         if Einheit_in == "t":
                            time.sleep(0.15)
                            Gewicht = input("Wie viel Kg? ")
                            Gewicht = float(Gewicht)
                            if Gewicht > 0:
                                ergebnis = Gewicht / 1000
                                print(f"Es sind {ergebnis} T")
                                wait = input("")
                            else:
                                print("Das Gewicht muss über 0 sein")
                                time.sleep(0.15)
                         elif Einheit_in == "g":
                            Gewicht = input("Wei viel Kg?")
                            Gewicht = float(Gewicht)
                            if Gewicht > 0:
                                ergebnis = Gewicht * 1000
                                print(f"Es sind {ergebnis} g ")
                                wait = input("")
                            else:
                                print("Das Gewicht muss über 0 sein")
                                time.sleep(0.15)
                        elif Einhheit_von == "t":
                         if Einheit_in == "kg":
                             Gewicht = input("Wie vielt t? ")
                             Gewicht = float(Gewicht)
                             if Gewicht > 0:
                                ergebnis =  1000 * Gewicht
                                print(f"Es sind {ergebnis} kg")
                                wait = input("")
                             else:
                                 print("Das Gewicht muss über 0 sein")
                                 time.sleep(0.15)
                         elif Einheit_in == "g":         
                            Gewicht = input("Wie vielt t? ")
                            Gewicht = float(Gewicht)
                            if Gewicht > 0:
                                ergebnis =  100_000_0 * Gewicht
                                print(f"Es sind {ergebnis} g")
                                wait = input("")
                            else:
                                print("Das Gewicht muss über 0 sein")
                        elif Einhheit_von == "g":
                            if Einheit_in == "kg":
                             Gewicht = input("Wie viel g? ")
                             Gewicht = float(Gewicht)
                             if Gewicht > 0:
                              ergebnis = Gewicht / 1000
                              print(f"Es sind {ergebnis} kg")
                              wait = input("")
                             else:
                                 print("Das Gewicht muss über 0 sein")
                            elif Einheit_in == "t":
                                Gewicht = input("Wie viel g? ")
                                Gewicht = float(Gewicht)
                                if Gewicht > 0:
                                    ergebnis = Gewicht / 100_000_0
                                    print(f"Es sind {ergebnis} t")
                                    wait = input(wait)
                                else:
                                    print("Das Gewicht muss über 0 sein")
                                    wait = input("")
                                    time.sleep(0.15)
                        else:
                            print("Es gibt nur 'g' 'kg' 't' zum umrechnen")
                            wait = input("")
                            time.sleep(0.15)
                elif formel == "Dichte":
                    for clear in range(100):
                        print("")
                    print("Alle Einheiten selber umrechnen")
                    while True:
                        volumen = input("Was ist das Volumen? (v) ")
                        time.sleep(0.15)
                        masse = input("was ist die masse? (m) ")
                        volumen = float(volumen)
                        masse = float(masse)
                        if volumen > 0:
                            if masse > 0:
                                ergebnis = masse / volumen
                                print(f"Die Dichte ist {ergebnis} p")
                                quitt = input("Willst du aufhören Dichte zuberechnen? (y um zu bestätigen) ")
                                if quitt == "y":
                                    for clear in range(100):
                                        print("")
                                    break
                            else:
                                print("Die Massee muss über 0 sein")
                        else:
                            print("Das Volumen muss über 0 sein")
alle_formeln()                  