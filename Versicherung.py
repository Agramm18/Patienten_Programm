import random

# Versicherungen

# Versicherungs Informationen

Versicherungsart = input("Sind sie Gesetzlich/Privat versichert: ")
Versicherungs_ID = int(input("Geben sie Ihre Versicherung ID an: "))
Versichert_Bei = input("Geben sie Ihren Versicherer an (AOK/ Allianz... ): ")


#Art Versicherung
print("Geben sie Ihre Versicherungen an")
print("Wenn sie schonmal hierwaren drücken sie ende")



#Arzt

Arzt_Privat = input("Geben sie einen verfügbaren Arzt an: ")
Arzt_Gesetzlich = input("Geben sie einen Verfügbaren Arzt an: ")

if Versicherungsart == "Privat":
    Arzt = Arzt_Privat
else:
    Arzt = Arzt_Gesetzlich

#Arzt

#Art Versicherungen
favs = []

while True:

    Versicherungen = input()
    if str.lower(Versicherungen) == "ende":
        break

    favs.append(Versicherungen)


for Versicherungen in favs:
    print(f"Deine Versicherungen sind, {Versicherungen}")
#Art Versicherung




#Zimmernummer
if Versicherungsart == "Privat":
    Zimmernummer_Privat = random.randint(1,50)
    Station = random.randint(1,10)

else:
    Zimmernummer = random.randint(51,100)
    Station = random.randint(11,20)

#Zimmernummer

# Versicherungen