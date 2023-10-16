from Patienten_Daten import Warte_Nr

print(f"Der Patient hat die Nummer {Warte_Nr}")

if Warte_Nr <= 20:
    print("Der Patient Muss in Warteraum 10")

elif Warte_Nr <= 50:
    print("Der Patient Muss in Warteraum 20")

elif Warte_Nr <= 75:
    print("Der Patient Muss in Warteraum 30")

elif Warte_Nr <= 100:
    print("Der Patient muss in Warteraum 40")
