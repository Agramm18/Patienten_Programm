import random
import datetime

Name = input("WWie heißen sie: ")
Geschlecht = input("Wie ist Ihr Geschlecht M oder W: ")
age = int(input("Wie alt sind sie: "))

def Birth():
    Day = int(input("Anwelchem Tag sind sie Geboren: "))
    Month = input("In Welchem Monat sind sie Geboren: ")
    Year = int(input("In Welchem Jahr sind sie Geboren: "))


    Birth_Date = str(Day) + " " + Month + " " + str(Year)

    print(Birth_Date)

Birth()

#Adresse
def Adresse ():


    Straßen_Name = input("Geben sie den Namen Ihrer Stra0e ein: ")
    Straßen_Nummer = (input("Geben sie Ihre Hausnnummer an: "))
    Postleitzahl = (input("Geben sie Ihre Postleitzahl ein: "))

    Adresse = Straßen_Name + Straßen_Nummer

    print(Adresse)

Adresse()



#Adresse

EMail = input("Geben sie bitte Ihre EMail Adresse an: ")
Telefonnummer = int(input("Geben sie bitte Ihre Telefonnummer an: "))


Status = input("Sind sie ein neuer Patient: ")
is_new = input("Waren sie schonmal Patient hier?: ")
Warte_Nr = random.randint(1,100)

