import Modules

def main():


    while True:
        print("\n--- MENU ---")
        print("1. Läs in filmer från CSV och spara i JSON")
        print("2. Visa alla filmer")
        print("3. Lägg till en film")
        print("4. Ta bort film")
        print("5. Spara JSON till CSV")
        print("6. Få ett slumpmässigt filmförslag")
        print("7. Gissa filmen")
        print("8. Avsluta")

        val = input("\nGör ditt val (1-8): ")

        if val == "1":
            Modules.load_movies_from_csv()

        elif val == "2":
            Modules.print_all_movies()

        elif val == "3":
            Modules.add_movie()

        elif val == "4":
            Modules.remove_movie()

        elif val == "5":
            Modules.save_json_to_csv()

        elif val == "6":
            vald_genre = input("Vilken genre vill du se? (t.ex. Action, Komedi: ")
            Modules.random_movie(vald_genre)

        elif val == "7":
            Modules.guess_movie()

        elif val == "8":
            print("Avslutar programet. Hej då!")
            break

        else:
            print("Ogiltigt val, försök igen.")

#Detta startar programmet
if __name__ == "__main__":
    main()