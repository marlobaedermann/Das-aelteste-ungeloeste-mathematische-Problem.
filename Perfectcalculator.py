import os
def umständlicherweg():
    # 🔹 Basisordner (aktueller Ordner)
    BASISORDNER = os.path.dirname(os.path.abspath(__file__))

    # 🔹 Dateien für perfekte und nicht perfekte Zahlen
    PERFEKT_DATEI = os.path.join(BASISORDNER, "perfekte_zahlen.txt")
    NICHT_PERFEKT_DATEI = os.path.join(BASISORDNER, "nicht_perfekte_zahlen.txt")

    # 🔹 Datei sicher erstellen, falls sie nicht existiert
    def datei_sicher(pfad):
        if not os.path.exists(pfad):
            with open(pfad, "w", encoding="utf-8") as file:
                file.write("")

    # 🔹 Text in Datei einfügen, nur wenn noch nicht vorhanden
    def einfuegen_eindeutig(pfad, zahl):
        datei_sicher(pfad)
        
        # Dateiinhalt lesen
        with open(pfad, "r", encoding="utf-8") as file:
            zeilen = file.read().splitlines()  # Zeilen als Liste
        
        # Zahl prüfen
        if str(zahl) not in zeilen:
            with open(pfad, "a", encoding="utf-8") as file:
                file.write(str(zahl) + "\n")  # Zeilenumbruch anhängen

    # 🔹 Prüfen, ob Zahl perfekt ist
    def ist_perfekt(n):
        teiler_summe = 0
        for i in range(1, n):
            if n % i == 0:
                teiler_summe += i
        return teiler_summe == n

    # 🔹 Grenzen festlegen
    start = 2
    ende = 10000  # zum Testen lieber klein halten

    # 🔹 Dateien vorbereiten
    datei_sicher(PERFEKT_DATEI)
    datei_sicher(NICHT_PERFEKT_DATEI)

    # 🔹 Berechnung
    for zahl in range(start, ende + 1):
        if ist_perfekt(zahl):
            einfuegen_eindeutig(PERFEKT_DATEI, zahl)
        else:
            einfuegen_eindeutig(NICHT_PERFEKT_DATEI, zahl)

    print("Fertig!")

def schnellerweg():
    # 🔹 Basisordner (aktueller Ordner)
    BASISORDNER = os.path.dirname(os.path.abspath(__file__))

    # 🔹 Dateien für perfekte Zahlen
    PERFEKT_DATEI = os.path.join(BASISORDNER, "perfekte_zahlen.txt")

    # 🔹 Datei sicher erstellen
    def datei_sicher(pfad):
        if not os.path.exists(pfad):
            with open(pfad, "w", encoding="utf-8") as file:
                file.write("")

    # 🔹 Text in Datei einfügen, nur wenn noch nicht vorhanden
    def einfuegen_eindeutig(pfad, zahl):
        datei_sicher(pfad)
        with open(pfad, "r", encoding="utf-8") as file:
            zeilen = file.read().splitlines()
        if str(zahl) not in zeilen:
            with open(pfad, "a", encoding="utf-8") as file:
                file.write(str(zahl) + "\n")

    # 🔹 Prüfen, ob Zahl prim ist (für Mersenne-Primzahlen)
    def ist_prim(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    # 🔹 Perfekte Zahlen berechnen (Formel)
    def perfekte_zahlen_mit_formel(max_p):
        for p in range(2, max_p + 1):
            mersenne = 2**p - 1
            if ist_prim(mersenne):
                perfekt = (2**(p-1)) * mersenne
                einfuegen_eindeutig(PERFEKT_DATEI, perfekt)
                print(f"Gefunden: {perfekt}")

    # 🔹 Dateien vorbereiten
    datei_sicher(PERFEKT_DATEI)

    # 🔹 Perfekte Zahlen bis p=31 (dann ist die letzte bekannte in diesem Bereich 2^31-1)
    perfekte_zahlen_mit_formel(100)

    print("Fertig!")
