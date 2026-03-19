import random
import csv
import json


filmer = []

#Användaren får välja genre Programmet väljer slumpmässigt en film från den genren

def random_movie(genre):
    genre_list = []

    #Gå igenom alla filmer och leta efter rätt genre
    for film in filmer:
        if film["genre"].lower() == genre.lower().strip():
            genre_list.append(film)

    #Om vi hittade några filmer, slumpa en
    if len(genre_list) > 0:
        slumpad_film = random.choice(genre_list)
        print(f"\nDagens filmtips: {slumpad_film['titel']}")
    else:
        print(f"\nTyvärr, hittade inga filmer i genren {genre}.")

def guess_movie():
    #Välj en slumpmässig film ur hela listan
    slumpad_film = random.choice(filmer)

    print("\n--- GISSA FILMEN ---")
    print(f"Ledtråd: {slumpad_film['beskrivning']}")

    gissning = input("vilken film är det? ")

    #jämnför gissning med titeln (ignorerar små och stora bokstäver
    if gissning.lower().strip() == slumpad_film["titel"].lower():
        print("Rätt! Snyggt jobbat. ")
    else:
        print(f"Fel! Rätt svar var: {slumpad_film['titel']}")

#Funktion 3: Visa alla filmer
def print_all_movies():
    print("\n--- ALLA FILMER ---")
    for film in filmer:
        print(f"{film['titel']}({film['genre']})")

#Funktion 4: Funktionen för att ladda filmer från CSV
def load_movies_from_csv():
    try:

        filmer.clear()

        with open("movies.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for film in reader:
                filmer.append(film)

        save_movies_to_json()
        print("Filmerna har laddats från movies.csv och sparats till movies.json")

    except FileNotFoundError:
        print("kunde inte hitta filen movies.csv!")

#Funktion 5
def save_movies_to_json():
    try:
        with open("movies.json", "w", encoding="utf-8") as file:
            json.dump(filmer, file, indent=4, ensure_ascii=False)
        print("Filmerna sparades till movies.json!")
    except Exception as error:
        print(f"Ett fel uppstod: {error}")

#Funktion 6
def add_movie():
    print("\n--- LÄGG TILL NY FILM ---")
    titel = input("Ange filmens titel: ")
    genre = input("Ange filmens genre: ")
    beskrivning = input("Ange en kort beskrivning: ")

    ny_film = {
        "titel": titel,
        "genre": genre,
        "beskrivning": beskrivning
    }

    filmer.append(ny_film)
    print(f"Lade till '{titel}' i listan.")

    save_movies_to_json()

#Funktion 7

def remove_movie():
    print("\n--- TA BORT FILM ---")
    titel_att_ta_bort = input("Vilken film vill du ta bort: ")

    hittad = False
    for film in filmer:
        if film["titel"] == titel_att_ta_bort:
            filmer.remove(film)
            hittad = True
            print(f"Filmen '{film['titel']}' har tagits bort.")

            save_movies_to_json()
            break

    if not hittad:
        print(f"Kunde inte hitta filmen '{titel_att_ta_bort}'.")

#Funktion 8
def save_json_to_csv():
    try:
        with open("movies.csv", "w", encoding="utf-8", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=["titel", "genre", "beskrivning"])

            writer.writeheader()
            writer.writerows(filmer)

        print("Klart! Nu är movies.csv uppdaterad.")

    except Exception as error:
        print(f"Kunde inte spara till CSV: {error}")

try:
    with open("movies.json", "r", encoding="utf-8") as file:
        filmer.extend(json.load(file))
except FileNotFoundError:
    pass