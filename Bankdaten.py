Bank = input("Bitte geben sie den Namen Ihrer Bank an: ")

Zahlung = input("Wollen sie mit Kreditkarte, Girokarte oder per Überweisung zahlen: ")

if Zahlung == "Kreditkarte":


    IBAN_Kredit = input("Bitte geben sie Ihre IBAN an: ")
    Gültig_Kredit = input("Bitte geben sie an bis wann die Karte gültig ist: ")
    Prüfnummer_Kredit = input("Bitte geben sie Ihre Prüfnummer an: ")



else:

    IBAN_Giro = input("Bitte geben sie Ihre IBAN an: ")
    Kartennummer_Giro = int(input("Bitte geben sie die Kartennummer an:  "))
    Bic_Giro = input("Geben sie bitte die Bic an: ")


if Zahlung == "Überweisung":
    print("Bitte füllen sie das Formular das sie am Empfang Kriegen aus")