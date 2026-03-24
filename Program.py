import Modules

def main():
    Modules.load_data()

    while True:
        print("\n--- MENU ---")
        print("1. Få ett slumpmässigt filmförslag")
        print("2. Gissa filmen")
        print("3. Visa alla filmer")
        print("4. Lägg till en film")
        print("5. Ta bort film")
        print("6. Spara JSON till CSV")
        print("7. Avsluta")

        val = input("\nGör ditt val (1-7): ")

        if val == "1":
            vald_genre = input("Vilken genre vill du se? (t.ex. Action, Komedi: ")
            Modules.random_movie(vald_genre)

        elif val == "2":
            Modules.guess_movie()

        elif val == "3":
            Modules.print_all_movies()

        elif val == "4":
            Modules.add_movie()

        elif val == "5":
            Modules.remove_movie()

        elif val == "6":
            Modules.save_json_to_csv()

        elif val == "7":
            print("Avslutar programet. Hej då!")
            break

        else:
            print("Ogiltigt val, försök igen.")

#Detta startar programmet
if __name__ == "__main__":
    main()