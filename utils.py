import os


# clear terminal
def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


# option after game
def option_after_game(menu, clear):
    while True:
        print()
        print("1.Kembali ke menu")
        print("q.keluar dari game")

        pilihan = input("(1/q) : ")

        if pilihan == "1":
            return
        elif pilihan == "q":
            break
        else:
            clear
            print("Input anda tidak valid")
