from random import randint
from utils import clear, option_after_game


# logika game
def bot_pilhan():
    bgk = ["b", "g", "k"]
    random_pilihan = bgk[randint(0, len(bgk) - 1)]
    return random_pilihan


def game(fix_score):

    bot_menang = 0
    pemain_menang = 0

    while True:
        if fix_score != bot_menang and fix_score != pemain_menang:

            print(f"score {pemain_menang} {bot_menang}")
            pilihan = input("(b/g/k) : ").lower()
            random_pilihan = bot_pilhan()

            # kondidi menang
            if (
                (pilihan == "k" and random_pilihan == "b")
                or (pilihan == "b" and random_pilihan == "g")
                or (pilihan == "g" and random_pilihan == "k")
            ):
                clear()
                print("anda menang\n")
                pemain_menang += 1
            # kondidi kalah
            elif (
                (pilihan == "b" and random_pilihan == "k")
                or (pilihan == "k" and random_pilihan == "g")
                or (pilihan == "g" and random_pilihan == "b")
            ):
                clear()
                print("anda kalah\n")
                bot_menang += 1
            # kondisi seimbang
            elif (
                (pilihan == "k" and random_pilihan == "k")
                or (pilihan == "b" and random_pilihan == "b")
                or (pilihan == "g" and random_pilihan == "g")
            ):
                clear()
                print("anda seimbang\n")
            else:
                clear()
                print("input anda tidak valid\n")

        elif fix_score == pemain_menang:
            clear()
            print("Selamat Anda Menang Permainan Batu Gunting Kertas\n")
            if __name__ == "__main__":
                option_after_game(menu(), clear())

        elif fix_score == bot_menang:
            clear()
            print("Anda kalah dari probabilitas what a shame\n")
            if __name__ == "__main__":
                option_after_game(menu(), clear())


# menu game
def menu():
    while True:
        clear()
        print("===Batu Gunting Kertas===")
        print("1.Membuat Score sendiri")
        print("2.Score Hanya 1")
        print("3.Scrore sampai 3")
        print("4.Score Sampai 5\n")
        print("===Pilihan lain nya===")
        print("b.Kembali ke menu utama")
        print("q.Keluar\n")

        menu_option = input("(1-4/b/q) : ")

        if menu_option == "1":
            clear()
            pilihan = int(input("Score : "))
            game(pilihan)
        elif menu_option == "2":
            game(1)
        elif menu_option == "3":
            game(3)
        elif menu_option == "4":
            game(5)
        elif menu_option == "b":
            return
        elif menu_option == "q":
            break
        else:
            print("Input anda tidak valid")


if __name__ == "__main__":
    menu()
