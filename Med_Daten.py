from Patienten_Daten import age
from Patienten_Daten import Geschlecht
groesse = int(input("Wie groß sind sie: "))
gewicht = int(input("Wie schwer sind sie "))

def BMI():
    BMI = gewicht/ (groesse*groesse)
    return BMI

number = BMI()
rounded_number = round(number, 5)
print(f"Ihr BMI ist {rounded_number}")


#Herzschlag


def Herzschlag():

    age_Neugeborene = 0 - 1
    age_Kleinkind = 2 - 3
    age_Vorschulkind = 4 - 7
    age_Kind = 8 - 13
    age_Jugendliche = 14 - 17
    age_EFrau = 18 - 64
    age_EMann = 16 - 64

    Gesunder_Ruhepuls_Neugeborne = 120
    Gesunder_Ruhepuls_Kleinkind = 110
    Gesunder_Ruhepuls_Vorschulkind = 100
    Gesunder_Ruhepuls_Kind = 90
    Gesunder_Ruhepuls_Jugendliche = 85
    Gesunder_Ruhepuls_EFrau = 75
    Gesunder_Ruhepuls_EMann = 70

    if age == 0 - 1:
        print(f"Der Normale Herzschlag liegt bei: {Gesunder_Ruhepuls_Neugeborne}")

    elif age == 2 - 3:
        print(f"Der Normale Herzschlag liegt bei: {Gesunder_Ruhepuls_Kleinkind}")

    elif age == 4 - 7:
        print(f"Der Normale Herzschlag liegt bei: {Gesunder_Ruhepuls_Vorschulkind}")

    elif age == 8 - 13:
        print(f"Der Normale Herzschlag liegt bei: {Gesunder_Ruhepuls_Kind}")

    else:
        print(f"Der Normale Herzschlag liegt bei: {Gesunder_Ruhepuls_Jugendliche}")



Herzschlag()

#Herzschlag