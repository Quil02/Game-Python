from Hangman.Hangman import menu as hangman_menu
from tebak_angka.tebak_angka import menu as tebak_angka_menu
from bgk.bgk import menu as bgk_menu
import Hangman.Data
from utils import clear
from sys import exit


def main_menu():
    while True:
        clear()
        print("===Main Menu===")
        print("1. Hangman")
        print("2. Tebak angka")
        print("3. Batu Gunting Kertas\n")
        print("===Option lain nya===")
        print("q. Keluar")
        print()

        menu_option = input("((1-3)/q) : ")

        if menu_option == "1":
            hangman_menu()
        elif menu_option == "2":
            tebak_angka_menu()
        elif menu_option == "3":
            bgk_menu()
        elif menu_option == "q":
            exit()


if __name__ == "__main__":
    main_menu()
