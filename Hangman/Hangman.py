from utils import clear, option_after_game
from .Data import hangman, words, sentences
from random import randint


def random(var):
    return var[randint(0, len(var) - 1)].lower()


# Logika game
def close(kata):
    close_kata = []

    for huruf in kata:
        if huruf.isalpha():
            close_kata.append("-")
        else:
            close_kata.append(huruf)

    return close_kata


def find_index(kata, tebakan):
    indexes = []
    for index, huruf in enumerate(kata, start=0):
        if huruf == tebakan:
            indexes.append(index)
    return indexes


def playgames(kata):
    clear()
    close_kata = close(kata)
    huruf_benar = []
    huruf_salah = []
    hangman_image = 0
    percobaan = 6

    while True:
        if percobaan != 0:
            clear()
            print(hangman[hangman_image])
            print("".join(close_kata))
            print(f"huruf salah ({', '.join(huruf_salah)})")
            print(f"huruf benar ({', '.join(huruf_benar)})")
            print(f"Sisa percobaan anda {percobaan}")
            tebakan = input("Masukan tebakan dari angka a-z : ").lower()
            if len(tebakan) != 1 or not tebakan.isalpha():
                print("Masukan 1 huruf saja dan itu harus huruf")
                continue
            index = find_index(kata, tebakan)

            if index:
                for i in index:
                    close_kata[i] = tebakan

                if tebakan not in huruf_benar:
                    huruf_benar.append(tebakan)

                if "-" not in close_kata:
                    clear()
                    print(hangman[hangman_image])
                    print("".join(close_kata))
                    print("selamat anda menang")
                    option_after_game()
                    break

            else:
                if tebakan not in huruf_salah:
                    huruf_salah.append(tebakan)

                percobaan -= 1
                hangman_image += 1

        elif percobaan == 0:
            clear()
            print(hangman[hangman_image])
            print(f"Kata yang di sembunyikan adalah : \n{kata}")
            print("Anda kalah what a shame")
            option_after_game()
            break


# Menu game


def menu():
    while True:
        clear()
        print("===Hangman===")
        print("1. Membuat kata sendiri")
        print("2. Tebak kalimat")
        print("3. Tebak Kata\n")
        print("===Option lain nya===")
        print("b. Kembali ke menu utama")
        print("q. Keluar dari permainan\n")

        menu_option = input("(1-3/b/q) : ")

        if menu_option == "1":
            clear()
            kata = input("Kalimat untuk di tebak : ").lower()
            playgames(kata)
        elif menu_option == "2":
            clear()
            playgames(random(sentences))
        elif menu_option == "3":
            clear()
            playgames(random(words))
        elif menu_option == "b":
            clear()
            return
        elif menu_option == "q":
            clear()
            exit()
        else:
            print("Option tidak valid coba lagi")


if __name__ == "__main__":
    menu()
