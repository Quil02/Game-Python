import os
import sys


# clear terminal
def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


# option_after_game
def option_after_game():
    while True:
        print()
        print("1.Kembali ke menu")
        print("q.keluar dari game")

        pilihan = input("(1/q) : ")

        if pilihan == "1":
            return
        elif pilihan == "q":
            clear()
            sys.exit()
        else:
            clear()
            print("Input anda tidak valid")
