from utils import clear
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
            print(f"huruf salah ({", ".join(huruf_salah)})")
            print(f"huruf benar ({", ".join(huruf_benar)})")
            print(f"Sisa percobaan anda {percobaan}")
            tebakan = input("Masukan tebakan dari angka a-z : ")
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
            print("anda kalah")
            break


# Menu game


def about():
    print("=====About The Game=====\n")
    print("===Tentang Hangman===")
    print(
        "Game Hangman adalah permainan tebak kata di mana satu\npemain (atau komputer) memikirkan sebuah kata, dan pemain\nlainnya mencoba menebak kata tersebut huruf demi huruf\ndalam jumlah kesempatan yang terbatas."
    )

    back = input("masukan (b) untuk kembali : ")
    if back == "b":
        clear()
        menu()
    else:
        print("goblog")


def menu():
    clear()
    print("===Hangman===\n")
    print("===Play option===")
    print("1.Membuat kata sendiri")
    print("2.Tebak kalimat")
    print("3.Tebak Kata\n")
    print("===About game===")
    print("?.tentang game\n")
    print("Pilihlah salah satu dari menu di atas")

    menu_option = input("(1/2/3/?) : ")

    if menu_option == "1":
        clear()
        kata = input("Kalimat untuk di tebak : ")
        playgames(kata)
    elif menu_option == "2":
        clear()
        playgames(random(sentences))
    elif menu_option == "3":
        clear()
        playgames(random(words))
    elif menu_option == "?":
        clear()
        about()
    else:
        print("Option tidak valid coba lagi")
        menu()


if __name__ == "__main__":
    menu()
